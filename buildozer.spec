[app]
title = Aviator Predictor
package.name = aviatorpredictor
package.domain = org.example
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 1.0
requirements = python3,kivy,requests
orientation = portrait
fullscreen = 1
osx.python_version = 3.11
android.api = 34
android.minapi = 21
android.build_tools = 34.0.0
android.sdk = 34
android.ndk = 25b
android.ndk_api = 21
android.private_storage = True
android.logcat_filters = *:S python:D
android.permissions = INTERNET

# Uncomment this if you use JNI or other native modules
# android.use_android_native_api = 1

[buildozer]
log_level = 2
warn_on_root = 1
use_git = 0

[python]
version = 3.11

[hostpython]
# Leave empty to use the default

[globals]
# Ensure compatibility with Build Tools and SDK
android.accept_sdk_license = True
