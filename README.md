# TelegramR Android

TelegramR is an unofficial Telegram client for Android with a phone-style layout for dual-screen devices. Its separate package, `app.telegramr.android`, lets it run alongside the official client with its own sign-in session.

- **Chat layout.** One pane by default. The chat list and conversation open in turn. On dual-screen devices, TelegramR keeps the active pane within one usable display area when Android reports a separating hinge. Two-pane mode is available in Chat Settings.
- **Chat controls.** Adjust the font and avatar sizes in the chat list. The chat menu includes a Read All action.
- **Privacy and sending.** Extra Settings includes Ghost Mode, silent sending, a 12-second delay for text, and the last activity observed during the current session. You can also mark a chat as read after sending.
- **Message history.** An optional encrypted local archive shows deleted messages and earlier revisions in the chat. It can retain copies of media already downloaded on the device.
- **Notifications and updates.** A background connection helps receive messages and calls in builds without Firebase. Extra Settings shows the installed version and checks for public TelegramR releases on GitHub.

[Changelog](CHANGELOG.md) · [Build instructions](BUILD.md) · [Releases](https://github.com/Qahnaarin7/TelegramR-Android/releases)

## Source and license

`TelegramR-source.patch` contains the cumulative changes to Telegram for Android 13.2.2. The upstream source is pinned to revision `21f7d109da6ab3506c9e9577f98c6a38771ab335`. The upstream copyright notices are retained. Configure your own Telegram API credentials and Android signing key locally as described in the build guide. [Pinned upstream source](https://github.com/TelegramMessenger/Telegram-Android/tree/21f7d109da6ab3506c9e9577f98c6a38771ab335) · [GPL license](LICENSE)

[TelegramR for Windows](https://github.com/Qahnaarin7/TelegramR) has its own repository and release channel.
