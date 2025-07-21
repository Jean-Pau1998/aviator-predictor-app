[app]

title = Aviator Predictor
package.name = aviatorpredictor
package.domain = org.example

source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 0.1

requirements = python3,kivy
orientation = portrait

fullscreen = 1
android.api = 34
android.minapi = 21
android.sdk = 34
android.ndk = 25b
android.private_storage = true
android.permissions = INTERNET

android.build_tools = 34.0.0

[buildozer]

log_level = 2
warn_on_root = 1

[app.android]

# (Optional) Presplash, Icon, etc., can be added here
