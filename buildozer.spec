[app]

# (str) Title of your application
title = Aviator Predictor

# (str) Package name
package.name = aviatorpredictor

# (str) Package domain (needed for android/ios packaging)
package.domain = org.example

# (str) Source code where the main.py lives
source.dir = .

# (str) The main .py file to use as the main entry point
source.main = main.py

# (list) Permissions
android.permissions = INTERNET

# (str) Supported orientation (one of: landscape, portrait or all)
orientation = portrait

# (bool) Indicate if the application should be fullscreen or not
fullscreen = 0

# (str) Supported platforms
osx.kivy_version = 2.1.0

# (list) List of inclusions using pattern matching
source.include_exts = py,png,jpg,kv,atlas

# (list) Application requirements
requirements = python3,kivy

# (str) Application icon
icon.filename = icon.png

# (str) Android entry point, default is ok
android.entrypoint = org.kivy.android.PythonActivity

# (str) Android app theme
android.theme = @android:style/Theme.NoTitleBar

# (str) Path to build artifact (APK) output
android.archive_path = bin/aviatorpredictor.apk
