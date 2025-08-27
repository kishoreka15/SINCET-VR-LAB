const CACHE_NAME = 'app-cache-v1'; // increment this string when you want force-clear caches
const ASSETS = [
  '/',
  '/index.html',
  '/manifest.json',
  '/icons/icon-192.png',
  '/icons/icon-512.png'
  // add your css/js/image files here
];

self.addEventListener('install', (event) => {
  // take control quickly
  self.skipWaiting();
  event.waitUntil(
    caches.open(CACHE_NAME).then(cache => cache.addAll(ASSETS))
  );
});

self.addEventListener('activate', (event) => {
  event.waitUntil(
    caches.keys().then(keys =>
      Promise.all(keys.map(k => (k !== CACHE_NAME ? caches.delete(k) : null)))
    ).then(() => self.clients.claim())
  );
  // notify clients if needed (optional)
  event.waitUntil(
    self.clients.matchAll().then(clients => {
      clients.forEach(client => client.postMessage({ type: 'SW_ACTIVATED' }));
    })
  );
});

self.addEventListener('fetch', (event) => {
  // network-first strategy
  event.respondWith((async () => {
    try {
      const networkResponse = await fetch(event.request);
      // update cache (optional)
      const cache = await caches.open(CACHE_NAME);
      cache.put(event.request, networkResponse.clone().catch(()=>{}));
      return networkResponse;
    } catch (err) {
      const cached = await caches.match(event.request);
      return cached || caches.match('/index.html');
    }
  })());
});

// listen for messages from the page
self.addEventListener('message', (event) => {
  if (event.data && event.data.type === 'SKIP_WAITING') {
    self.skipWaiting();
  }
});