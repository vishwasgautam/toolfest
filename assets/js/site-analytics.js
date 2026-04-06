/* ToolFest — AdSense + GA4 (single place to update IDs) */
(function () {
  var ADSENSE_CLIENT = 'ca-pub-1957013406466053';
  var GA_MEASUREMENT_ID = 'G-Y6CJS2NH91';

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
