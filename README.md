# Tamatem

## The Traget Project:
https://play.google.com/store/apps/details?id=com.soum.sa

## Recoded Video https://www.loom.com/share/9ed9355462d44116a4159a5b4880f3d0




## Pre-requisites:

1. Install Appium 

2. Install Java

3. Install Python

4. Install Python requirments:  `python -m pip install -r .\requirements.txt`

5. Install android SDK

6. set the JAVA_HOME and ANDOIRD_HOME paths to the OS 




## Setup

1. Install Python requirments:  `python -m pip install -r .\requirements.txt`

2. make sure you connected the emulator or the real device and it listed by that command `adb devices`

3. replace the APK at the build folder with your APK Adnroid  



## Running Scripts

1. run `python -m pytest --html=report.html --self-contained-html` in terminal 


## Generate test report

The tests are integrated with pytest-html reporting tools. In order to see test reports you can find it at ./report.html


## Structure:

## Where to put what

This section aims to give a hint on the usage of each file/directory

1. `build`: contains the APK file.
2. `fixtures`:  to manage fixtures and hooks (contain the driver configuration and settings)
3. `pages`: store page object classes, each representing a page or screen in the mobile app.
4. `tests`: contains the E2E test files.
5. `selectors`: contains the selectors that been used at pages.
6. `utilities`: to store utility scripts

