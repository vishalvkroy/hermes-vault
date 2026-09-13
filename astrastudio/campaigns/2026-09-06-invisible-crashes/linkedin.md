Our desktop app runs on a shopkeeper's Windows machine, often with patchy internet, no IT person nearby, and nobody watching a log file. Until this week, if it crashed there, we found out only if the owner noticed, remembered, and described it well enough for us to reproduce. Their console, the one thing that would have explained it, is gone the moment they close the app.

The backend has had Sentry for a while. Desktop never did. So we added it: one call in the error boundary that already wraps every screen, hooks into the window.onerror and unhandledrejection handlers that already catch what happens before React even mounts, and a tag on login/logout so we know which shop and which user hit it.

Building that last part caught a real bug. A returning session loads its saved user straight into the store, skipping the normal login step entirely. That's the common case, someone opening the app they were already signed into, not the rare one. Without the fix, a crash there would report with no shop and no user attached, on exactly the restart that happens most.

It scrubs the Authorization header before anything leaves the machine. Separate Sentry project from the backend, since a desktop stack trace means something different from a server one.

We talk a lot about offline-first as the reason Astra Atlas fits tier-2/3 retail better than cloud-first tools built for reliable connections. This is the other half of that promise: working without internet is only useful if we also find out when it breaks, instead of a shop owner switching back to a notebook and pen without telling us.

#buildinpublic #IndianSMB #POS #SaaS
