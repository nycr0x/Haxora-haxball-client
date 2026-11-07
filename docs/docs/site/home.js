/* Each language has its own HTML URL. Old shared ?lang=en links still work. */
(function () {
  var url = new URL(window.location.href);
  if (url.searchParams.get("lang") === "en") {
    url.pathname = url.pathname.replace(/(?:index\.html)?$/, "en/");
    url.searchParams.delete("lang");
    // These sections have different IDs on the English page.
    var sections = { "#ozellikler": "#features", "#kurulum": "#install", "#sss": "#faq" };
    url.hash = sections[url.hash] || "";
    window.location.replace(url.href);
  }
})();
