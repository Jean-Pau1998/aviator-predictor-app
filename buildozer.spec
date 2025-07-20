[app]

title = Aviator Predictor
package.name = aviatorpredictor
package.domain = org.jeanpau
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 0.1
requirements = python3,kivy
orientation = portrait
android.permissions = INTERNET,VIBRATE
android.api = 33
android.minapi = 23
android.sdk = 24
android.ndk = 23b
android.build_tools_version = 34.0.0
android.archs = arm64-v8a,armeabi-v7a
android.ndk_path = 
android.private_storage = True

# (str) Custom package data files
presplash.filename = %(source.dir)s/data/presplash.png
icon.filename = %(source.dir)s/data/icon.png

# (bool) Indicate if the application should be fullscreen or not
fullscreen = 1

# (str) Supported orientation (one of landscape, sensorLandscape, portrait or all)
orientation = portrait

# (bool) Android logcat filters to use
log_level = 2

# (str) Entry point
entrypoint = main.py

# (str) Android entry point, default is ok
#android.entrypoint = org.kivy.android.PythonActivity

# (list) Permissions
android.permissions = INTERNET,VIBRATE

# (bool) Include SQLite3 support
android.sqlite3 = True

# (bool) Copy library instead of making a libpymodules.so
android.copy_libs = 1

# (str) List of inclusions using pattern matching
source.include_patterns = *.py,*.kv,*.png,*.jpg,*.wav,*.ogg

# (str) Path to a custom Java class that acts as the main activity
#android.activity_class_name = org.kivy.android.PythonActivity

# (str) Path to custom Java classes
#android.add_src = src

# (list) Java .jar files to add to the libs so that pyjnius can access
#android.add_jars = libs/*.jar

# (str) Custom Java package for generated code
#android.javac_options = -Xlint:deprecation -Xlint:unchecked

# (str) Custom Java arguments
#android.java_src = java

# (list) Shared libraries to add to APK
#android.add_shared_libs = libs/*.so

# (bool) Add Android Auto support
#android.auto = 0

# (str) The filename of the main .py file
# (NOTE: Do not include the .py extension here)
#source.main_py = main

[buildozer]

log_level = 2
warn_on_root = 1
