/*
 * Punch Planner - service worker
 * Version 1.4.4 (2026-11-08) - Mickael Cauberghs
 *
 * Mickael Cauberghs, 2026-11-07: keeps a copy of the app on my phone so it
 * opens even with no internet. It always tries the network first, so a new
 * version on GitHub Pages is picked up the next time I open the app online.
 * Change CACHE_NAME with every new version.
 *
 * Mickael Cauberghs, 2026-11-08 (v1.4.4): GitHub Pages tells phones to keep
 * a page for 10 minutes, so a new version did not show up right away. The
 * app now always asks GitHub for the newest copy ("no-cache") and the app
 * page reloads itself once when a new version is installed.
 */
"use strict";

const CACHE_NAME = "punch-planner-1.4.4";
const APP_FILES = [
  "./",
  "index.html",
  "manifest.webmanifest",
  "icon-192.png",
  "icon-512.png",
  "icon-maskable-512.png"
];

self.addEventListener("install", event => {
  // "reload" skips the phone's saved copies, so the new version is stored
  event.waitUntil(caches.open(CACHE_NAME).then(cache =>
    cache.addAll(APP_FILES.map(f => new Request(f, { cache: "reload" })))));
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
    fetch(req, { cache: "no-cache" })   // always check GitHub for a newer copy
      .then(res => {
        if (res.ok) {
          const copy = res.clone();
          caches.open(CACHE_NAME).then(cache => cache.put(req, copy));
        }
        return res;
      })
      .catch(() => caches.match(req).then(hit => hit || caches.match("index.html")))
  );
});
