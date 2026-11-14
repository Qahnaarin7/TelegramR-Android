from pathlib import Path
import re

# Run from the root of the pinned Telegram for Android checkout.
FILES = ('TMessagesProj/config/release/AndroidManifest_standalone.xml', 'TMessagesProj/google-services.json', 'TMessagesProj/src/main/java/org/telegram/messenger/BuildVars.java', 'TMessagesProj_App/google-services.json', 'TMessagesProj_AppHockeyApp/google-services.json', 'TMessagesProj_AppHuawei/google-services.json', 'TMessagesProj_AppStandalone/google-services.json')
for name in FILES:
    path = Path(name)
    data = path.read_bytes()
    path.write_bytes(re.sub(rb"AIza[0-9A-Za-z_-]{35}", b"GOOGLE_API_KEY_FROM_UPSTREAM", data))
