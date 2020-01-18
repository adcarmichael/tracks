// var staticCacheName = 'djangopwa-v1';

// self.addEventListener('install', function (event) {
//     event.waitUntil(
//         caches.open(staticCacheName).then(function (cache) {
//             return cache.addAll([
//                 '/shell_top'
//             ]);
//         })
//     );
// });

// self.addEventListener('fetch', function (event) {
//     var requestUrl = new URL(event.request.url);
//     if (requestUrl.origin === location.origin) {
//         if ((requestUrl.pathname === '/')) {
//             event.respondWith(caches.match('/shell_top'));
//             return;
//         }
//     }
//     event.respondWith(
//         caches.match(event.request).then(function (response) {
//             return response || fetch(event.request);
//         })
//     );
// });