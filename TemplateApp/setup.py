import sys
from cx_Freeze import *

# Dependencies are automatically detected, but it might need fine tuning.
additional_modules = []

build_exe_options = {"includes": additional_modules,
                     "packages": ["tkinter", "shutil" ,"klembord", "sys"],
                     "excludes": [''],
                     "include_files": ['WebpageTemplate.html', 'newTemplate.html','newEbay.html','EbayTemplate.html']}

base = None
if sys.platform == "win32":
    base = "Win32GUI"

setup(name="TemplateApp",
      version="1.0",
      description="Forms for building item templates",
      options={"build_exe": build_exe_options},
      executables=[Executable(script="main.py", base=base)])