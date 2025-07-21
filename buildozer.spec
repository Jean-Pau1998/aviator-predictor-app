[app]

title = Aviator Predictor
package.name = aviatorpredictor
package.domain = org.aviator.predictor
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 1.0
requirements = python3,kivy
orientation = portrait
fullscreen = 1

[buildozer]

log_level = 2
warn_on_root = 1
target = android
android.api = 34
android.minapi = 21
android.sdk = 34
android.ndk = 25b
android.build_tools = 34.0.0
android.build_tools_version = 34.0.0
android.accept_sdk_license = True
android.arch = armeabi-v7a
android.packaging = apk
copy_to = aviator_predictor.apk

[android]
android.permissions = INTERNET
