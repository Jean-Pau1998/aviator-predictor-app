[app]
title = Aviator Predictor
package.name = aviatorpredictor
package.domain = org.example
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 1.0
requirements = python3,kivy
orientation = portrait
fullscreen = 1

# Entry point
entrypoint = main.py

# Android permissions
android.permissions = INTERNET

# SDK and NDK configuration
android.api = 34
android.minapi = 21
android.sdk = 34
android.ndk = 23b
android.ndk_api = 21
android.build_tools = 34.0.0
android.use_aidl = False

# Disable AIDL to avoid missing aidl error
android.use_aidl = False

# Theme (optional)
android.theme = "@android:style/Theme.NoTitleBar"

# Optional resources
# icon.filename = %(source.dir)s/icon.png
# presplash.filename = %(source.dir)s/presplash.png
# android.add_assets = assets/

# Private storage
android.private_storage = 1

[buildozer]
log_level = 2
warn_on_root = 1
