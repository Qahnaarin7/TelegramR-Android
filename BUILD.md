# TelegramR для Android

TelegramR — неофіційний клієнт на базі Telegram for Android 13.2.2, ревізія `21f7d109da6ab3506c9e9577f98c6a38771ab335`. Збережено повідомлення про авторство Telegram for Android у вихідному коді та ліцензію GNU GPL v2 або новішу. Код AyuGram та TelegramR Desktop у цей патч не переносився. [Зафіксована ревізія Telegram for Android](https://github.com/DrKLO/Telegram/tree/21f7d109da6ab3506c9e9577f98c6a38771ab335)

## Збірка

Потрібні Git, Python 3, JDK 17, Android SDK 36, Build Tools 36.0.0 і 35.0.0, NDK 27.2.12479018, CMake 3.22.1 і Platform Tools. Для `x86` та `x86_64` додайте NASM у `PATH`. На Windows оберіть короткий шлях до проєкту, щоб залишити місце для шляхів об'єктних файлів CMake.

Розпакуйте файли релізу в поточну папку. Команди PowerShell

```powershell
git init TelegramR
git -C TelegramR config core.longpaths true
git -C TelegramR config core.autocrlf false
git -C TelegramR remote add upstream https://github.com/DrKLO/Telegram.git
git -C TelegramR fetch --depth=1 upstream 21f7d109da6ab3506c9e9577f98c6a38771ab335
git -C TelegramR switch --detach FETCH_HEAD
Push-Location TelegramR
python ../prepare-upstream.py
Pop-Location
git -C TelegramR apply ../TelegramR-source.patch
git -C TelegramR submodule update --init --recursive --depth=1
Set-Location TelegramR
```

Укажіть Android SDK у `ANDROID_HOME` або в ігнорованому Git файлі `local.properties` (наприклад, `sdk.dir=C:/Android/Sdk`). Створіть ігнорований файл `.telegramr/api.properties` з власними значеннями:

```properties
apiId=ваш_числовий_api_id
apiHash=ваш_32_символьний_api_hash
```

Реквізити видає розділ **API development tools** в акаунті Telegram. Вони входять у зібраний APK. Для Firebase Cloud Messaging покладіть власний `google-services.json` для `app.telegramr.android` у `TMessagesProj_AppStandalone/`. Для перевірки входу з тестовими реквізитами Telegram опублікував окремі обмеження. [Реєстрація клієнта Telegram API](https://core.telegram.org/api/obtaining_api_id)

Для локальної тестової збірки створіть ключ один раз:

```powershell
New-Item -ItemType Directory -Force .telegramr
& "$env:JAVA_HOME/bin/keytool.exe" -genkeypair -keystore .telegramr/debug.keystore -storetype PKCS12 -storepass android -keypass android -alias androiddebugkey -keyalg RSA -keysize 2048 -validity 10000 -dname "CN=Android Debug,O=Android,C=US"
& "$env:JAVA_HOME/bin/java.exe" -classpath gradle/wrapper/gradle-wrapper.jar org.gradle.wrapper.GradleWrapperMain :TMessagesProj_AppStandalone:assembleAfatDebug -PtelegramrAbis=arm64-v8a
```

Тестовий APK з'явиться в `TMessagesProj_AppStandalone/build/outputs/apk/afat/debug/app.apk`. На Linux або macOS запустіть ті самі завдання через `./gradlew`. Параметр приймає ABI через кому. Приберіть його, щоб зібрати всі архітектури, які підтримує цей варіант.

Для підписаної збірки з власними реквізитами використайте `:TMessagesProj_AppStandalone:assembleAfatStandalone`. У `.telegramr/signing.properties` задайте `storeFile`, `storePassword`, `keyAlias` і `keyPassword`. Тримайте сховище ключа в `.telegramr/` або поза репозиторієм. Для оновлення встановленого APK Android вимагає той самий сертифікат підпису.
