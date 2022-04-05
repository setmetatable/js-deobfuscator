import PyInstaller.__main__
import os
from shutil import make_archive

args = ["src/__main__.py",
        "-p", "src",
        "-n", "JS-Deobfuscator",
        "-F",
        "--icon", "./assets/icon.ico"]

PyInstaller.__main__.run(args)

try:
    os.remove("JS-Deobfuscator.zip")
except OSError:
    pass
make_archive("JS-Deobfuscator", "zip", "dist")
