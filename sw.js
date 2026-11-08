/*
 * Punch Planner - service worker
 * Version 1.4.3 (2026-11-08) - Mickael Cauberghs
 *
 * Mickael Cauberghs, 2026-11-07: keeps a copy of the app on my phone so it
 * opens even with no internet. It always tries the network first, so a new
 * version on GitHub Pages is picked up the next time I open the app online.
 * Change CACHE_NAME with every new version.
 */
"use strict";

const CACHE_NAME = "punch-planner-1.4.3";
const APP_FILES = [
  "./",
  "index.html",
  "manifest.webmanifest",
  "icon-192.png",
  "icon-512.png",
  "icon-maskable-512.png"
];

self.addEventListener("install", event => {
  event.waitUntil(caches.open(CACHE_NAME).then(cache => cache.addAll(APP_FILES)));
  self.skipWaiting();
});

self.addEventListener("activate", event => {
  event.waitUntil(
    caches.keys()
      .then(keys => Promise.all(keys.filter(k => k !== CACHE_NAME).map(k => caches.delete(k))))
      .then(() => self.clients.claim())
  );
});

// Network first, then the saved copy when offline.
self.addEventListener("fetch", event => {
  const req = event.request;
  if (req.method !== "GET" || new URL(req.url).origin !== self.location.origin) return;
  event.respondWith(
    fetch(req)
      .then(res => {
        const copy = res.clone();
        caches.open(CACHE_NAME).then(cache => cache.put(req, copy));
        return res;
      })
      .catch(() => caches.match(req).then(hit => hit || caches.match("index.html")))
  );
});
