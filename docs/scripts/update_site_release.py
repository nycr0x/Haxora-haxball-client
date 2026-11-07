"""Refresh visible HTML release data from GitHub; no browser API call is needed.

Run from any directory: python scripts/update_site_release.py
For offline validation: python scripts/update_site_release.py --release-json FILE
Only stable published releases with a Windows installer are accepted.
"""
import argparse
import datetime as dt
import html
import json
from pathlib import Path
import re
import urllib.request

ROOT = Path(__file__).resolve().parents[1]
BASE = "https://nycr0x.github.io/Haxora-haxball-client/"
API = "https://api.github.com/repos/nycr0x/Haxora-haxball-client/releases/latest"


def replace_id(source, element_id, value):
    pattern = rf'(<[^>]+\bid="{element_id}"[^>]*>).*?(</[^>]+>)'
    result, count = re.subn(pattern, lambda m: m[1] + html.escape(value.replace("\r\n", "\n").replace("\r", "\n")) + m[2], source, flags=re.S)
    if count != 1:
        raise ValueError(f"Expected exactly one #{element_id}; found {count}")
    return result


def update(release):
    if release.get("draft") or release.get("prerelease"):
        raise ValueError("Expected a published stable release")
    tag = release["tag_name"]
    published = dt.datetime.fromisoformat(release["published_at"].replace("Z", "+00:00")).date().isoformat()
    installer = next(a for a in release["assets"] if a["name"] == "Haxora-Setup.exe")
    release_url = release["html_url"]
    if not release_url.startswith("https://github.com/nycr0x/Haxora-haxball-client/releases/tag/"):
        raise ValueError("Unexpected release URL")
    version = tag.removeprefix("v")
    # Parse and prepare every update before writing anything.
    updates = {}
    for relative, language in [("index.html", "tr"), ("en/index.html", "en")]:
        path = ROOT / "docs" / relative
        original = path.read_text(encoding="utf-8")
        source = original
        def schema(match):
            data = json.loads(match[1])
            if data.get("@type") == "SoftwareApplication":
                data["softwareVersion"] = version
                data.pop("screenshot", None)
            return '<script type="application/ld+json">\n' + json.dumps(data, ensure_ascii=False, indent=2) + '\n</script>'
        source = re.sub(r'<script type="application/ld\+json">(.*?)</script>', schema, source, flags=re.S)
        if language == "tr":
            values = {
                "heroVersion": tag, "releaseBoxTitle": "Haxora " + version,
                "boxVersion": tag, "boxSize": f'{installer["size"] / 1048576:.1f} MB',
                "boxDate": published, "releaseTag": tag, "releaseDate": published,
                "notesTitle": "Haxora " + version + " sürüm notları",
                "notes": re.sub(r"\[zorunlu\]", "", release.get("body") or "Bu sürüm için not eklenmemiş.", flags=re.I).strip(),
            }
            for element_id, value in values.items():
                source = replace_id(source, element_id, value)
        else:
            marker = r'<!-- release-summary:start -->.*?<!-- release-summary:end -->'
            block = ('<!-- release-summary:start -->\n<p class="hero-note">Release '
                     + html.escape(tag) + ' · <time datetime="' + published + '">' + published
                     + '</time> · <a href="' + html.escape(release_url, quote=True)
                     + '">Release notes and downloads</a></p>\n<!-- release-summary:end -->')
            if re.search(marker, source, re.S):
                source = re.sub(marker, lambda _: block, source, flags=re.S)
            else:
                needle = '<p class="hero-note">Haxora is independent.'
                if needle not in source:
                    raise ValueError("English release insertion point missing")
                source = source.replace(needle, block + '\n      ' + needle)
        if source != original:
            updates[path] = source

    sitemap = ROOT / "docs/sitemap.xml"
    sitemap_text = sitemap.read_text(encoding="utf-8")
    today = dt.datetime.now(dt.timezone.utc).date().isoformat()
    for path in updates:
        relative = path.relative_to(ROOT / "docs").as_posix().removesuffix("index.html")
        loc = re.escape(BASE + relative)
        sitemap_text = re.sub(r'(<loc>' + loc + r'</loc>.*?<lastmod>).*?(</lastmod>)',
                              lambda m: m[1] + today + m[2], sitemap_text, flags=re.S)
    for path, content in updates.items():
        path.write_text(content, encoding="utf-8")
    if updates:
        sitemap.write_text(sitemap_text, encoding="utf-8")
    (ROOT / "docs/site/sitemap.xml").write_text(sitemap_text, encoding="utf-8")
    print(f"{tag}: updated {len(updates)} HTML files")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--release-json", type=Path)
    args = parser.parse_args()
    if args.release_json:
        data = json.loads(args.release_json.read_text(encoding="utf-8"))
    else:
        request = urllib.request.Request(API, headers={"Accept": "application/vnd.github+json", "User-Agent": "Haxora-site-update"})
        with urllib.request.urlopen(request, timeout=30) as response:
            data = json.load(response)
    update(data)
