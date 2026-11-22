# Tłumacz PL-TR

Static PWA (no build, no framework): a Polish-Turkish voice interpreter that calls the Claude API directly from the browser with your own key. Push-to-talk both ways, Polish text-to-speech, pronunciation in Turkish letters, offline phrasebook, private "ask me" mode.

## Deploy
Serve the folder as static files over HTTPS (speech recognition and service workers need it): GitHub Pages, Netlify, Cloudflare Pages, or any static host. `tools/` is not needed on the server. Open the URL, tap the gear, paste your API key (stored only in this browser's localStorage), press Test.

## iOS tips
- Use Safari; Share > Add to Home Screen for a full-screen app. Allow microphone and Speech Recognition when asked.
- If speech recognition fails, use the text box and the keyboard's dictation microphone.
- Better Polish voice: Settings > Accessibility > Spoken Content > Voices > Polish > download an Enhanced/Premium voice (e.g. Zosia), then pick it in the app settings.
- Turn off silent mode and raise the volume; iOS speaks only after a first tap in the page.
