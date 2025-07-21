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
osx.python_version = 3
osx.kivy_version = 1.11.1

# Permissions (optional: only if your app needs them)
android.permissions = INTERNET,WAKE_LOCK

# Icon settings (optional)
icon.filename = %(source.dir)s/icon.png

[buildozer]
log_level = 2
warn_on_root = 1
target = android
android.api = 34
android.minapi = 21
android.sdk = 34
android.ndk = 25b
android.build_tools = 34.0.0
android.accept_sdk_license = True
android.arch = armeabi-v7a
android.packaging = apk
copy_to = aviator_predictor.apk
p4a.branch = master
p4a.bootstrap = sdl2

# Set Python version and Android versions
android.api = 34
android.minapi = 21
android.sdk = 34
android.ndk = 25b
android.build_tools = 34.0.0
android.ndk_path = 
android.sdk_path = 
android.accept_sdk_license = True

# Set architecture
android.arch = armeabi-v7a

# Package format
android.packaging = apk

# Whether to copy the APK to the project root after build
copy_to = aviator_predictor.apk

# Extra settings
p4a.branch = master
p4a.bootstrap = sdl2

# Exclude files (optional)
exclude_dirs = tests, bin, venv, __pycache__
