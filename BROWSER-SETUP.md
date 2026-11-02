# Browser setup and preflight

Run this check after the initial questionnaire and BEFORE generating images or spending Flow credits. A fresh ChatGPT/Codex installation does not prove that browser control is connected. A website URL in chat, an open personal browser, web search, or terminal full access does not prove UI access.

## One-time user setup

Use the desktop app and a local session with an available browser-control integration. In ChatGPT desktop, open ChatGPT → Work → Plugins and set up Browser for the built-in browser, or Chrome for the user's regular Chrome browser. Follow the installed plugin's setup prompts. For Chrome, install its browser extension and approve the requested permissions. Review site access in Settings → Browser, or Settings → Computer use → Manage next to Chrome, as appropriate. If using desktop Computer Use on macOS, grant the required Screen Recording and Accessibility permissions. UI names and availability can vary by app version; follow the current app and official setup page rather than inventing settings.

Official OpenAI setup: https://developers.openai.com/training/walkthroughs/using-your-computer-and-browser

For Claude, use that client's supported browser integration and its own setup instructions; OpenAI plugins and permission steps are not interchangeable with Claude's. If no browser-control integration is available, pause here and explain the missing capability. Do not promise that changing a repository or enabling terminal full access can add it.

## Agent verification before production

1. Discover the currently exposed browser tools and read their setup/runtime documentation. Do not assume a tool name or an installed bundle path.
2. Use that integration to open or select Google Flow and read its actual rendered UI. Confirm that controls are accessible and that the intended account is signed in. The user handles login; never request passwords, cookies or session tokens.
3. Verify supported file upload and download capabilities from the integration documentation; create/select a project and confirm the frame composer and expected settings are accessible before image generation. Do not spend credits as a connectivity test. An unrelated website or web-search result is insufficient evidence.
4. Record `browser_preflight` in the project manifest: status, client/integration, checked timestamp, selected account, Flow URL, and any unresolved upload/download capability. Mark passed only when required capabilities are established; do not fabricate a successful transfer test. Recheck actual transfers when assets are ready.

## Connection or browser-bundle failures

Capture the exact error and distinguish a missing integration, denied permission, disconnected extension and stale runtime. Use only the integration's documented reconnect/reset procedure and rediscover tabs afterward. A single recovery attempt is appropriate; do not repeatedly issue the same failing call or duplicate generation jobs. If the error persists, save `browser_setup_required` and show one short checklist tailored to that error: complete plugin/extension setup, approve the necessary site/app permissions, reconnect or restart the affected client if its setup calls for it, then retry the preflight.

User clicks for login, installation and permission approval are a one-time setup exception to the initial-questionnaire-only typing rule. Ask for the minimum action needed, not another written brief. Never disable browser security, bypass organization restrictions, extract browser credentials, expose a debugging port, or patch bundled app files to force access. If policy or account availability blocks the integration, explain the limitation and offer a supported client instead. Do not claim the other PC is repaired without a successful preflight there.

On a mid-render disconnect, preserve job IDs, reconnect, inspect existing jobs and resume; never resubmit blindly.
