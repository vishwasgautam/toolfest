/* ToolFest — AdSense + GA4 (single place to update IDs) */
(function () {
  var ADSENSE_CLIENT = 'ca-pub-1957013406466053';
  var GA_MEASUREMENT_ID = 'G-Y6CJS2NH91';
  var FAVICON_PATH = '/assets/icons/toolfest-favicon.svg';

  function ensureFavicon() {
    var hasIcon = document.querySelector('link[rel="icon"], link[rel="shortcut icon"]');
    if (hasIcon) return;

    var icon = document.createElement('link');
    icon.rel = 'icon';
    icon.type = 'image/svg+xml';
    icon.href = FAVICON_PATH;
    document.head.appendChild(icon);

    var shortcut = document.createElement('link');
    shortcut.rel = 'shortcut icon';
    shortcut.href = FAVICON_PATH;
    document.head.appendChild(shortcut);
  }

  ensureFavicon();

  var a = document.createElement('script');
  a.async = true;
  a.src =
    'https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=' +
    encodeURIComponent(ADSENSE_CLIENT);
  a.crossOrigin = 'anonymous';
  document.head.appendChild(a);

  window.dataLayer = window.dataLayer || [];
  function gtag() {
    dataLayer.push(arguments);
  }
  window.gtag = gtag;
  gtag('js', new Date());
  gtag('config', GA_MEASUREMENT_ID);

  var g = document.createElement('script');
  g.async = true;
  g.src = 'https://www.googletagmanager.com/gtag/js?id=' + encodeURIComponent(GA_MEASUREMENT_ID);
  document.head.appendChild(g);
})();
