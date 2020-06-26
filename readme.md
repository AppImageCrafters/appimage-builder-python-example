# Python AppImage packaging example

This project contains an appimage-builder recipe for
a Python3 application. To recreate the package use
a modern Debian/Ubuntu system and appimage-builder.

## Instructions

Packaging a Python3 application into an AppImage is quite
similar to packaging a regular compiled application. Just
a few adjustments are required:

1. Use the Python main binary as entry point: 
    `exec: usr/bin/python3`

2. Install the pip requirements using the AppDir as root:
    `python3 -m pip install --root=AppDir -r ./requirements.txt`

3. Set the PYTHONHOME environment variable in the AppImage runtime:
    `PYTHONHOME: '${APPDIR}/usr'`
    
4. Copy your app source code into the AppDir:
    `cp ./src  AppDir/usr -r`
 
 That's all! 
 
 Check the appimage-builder.yml file for the complete recipe.