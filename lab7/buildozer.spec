[app]

# Название вашего приложения
title = Физические расчеты

# Версия приложения
version = 1.0

# Описание приложения
description = Приложение для физических расчетов

# Пакет, который содержит main.py
package.domain = org.test
package.name = physicalcalculations

# Имя основного скрипта
source.dir = .

# Минимально поддерживаемая версия Android
requirements = kivy==2.0.0,psycopg2,openpyxl

# Нужные зависимости
application = main.py

# Иконка приложения
icon.filename = %(source.dir)s/icon.png

# Ориентация экрана
orientation = portrait

# Поддерживаемые разрешения экрана
fullscreen = 0

# Список разрешений для камеры и т.п.
android.permissions = INTERNET

# Параметры компиляции
log_level = 2
osx.python_version = 3
osx.kivy_version = 2.0.0

# Архитектуры для компиляции
android.arch = armeabi-v7a,arm64-v8a,x86,x86_64

# Требуемая версия SDK
android.sdk = 24

# Путь до NDK
android.ndk_path = /path/to/ndk

# Флаги компиляции
android.gradle_dependencies = 'com.android.support:design:27.1.1','com.android.support:support-v13:27.1.1'

# Другие параметры
p4a.branch = master
