"""
Run this script to generate `gtc.exe`

B. D. Hall, August 2020
"""
import os 
import PyInstaller.__main__

# UPX makes the executable significantly smaller, but slows the build

PyInstaller.__main__.run([
    '--name={!s}'.format('gtc'),
    '--onefile',
    # '--upx-dir={!s}'.format( os.path.join(r'c:/usr', r'upx-3.96-win64') ),
    '--icon={!s}'.format( os.path.join(r'../icon', r'gtc.ico') ),
    'gtc.py'
])
