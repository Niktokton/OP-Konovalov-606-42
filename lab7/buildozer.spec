[app]

# Required
title = My Kivy App
package.name = mykivyapp
package.domain = org.test
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 0.1

# Android specific
android.arch = armeabi-v7a,arm64-v8a
android.api = 21
android.minapi = 21
android.ndk = 19c
android.sdk = 20
android.permissions = INTERNET

# Requirements
requirements = python3,kivy
