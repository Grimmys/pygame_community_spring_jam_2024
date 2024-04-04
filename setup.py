import sys
from cx_Freeze import setup, Executable

from src.constants import GAME_TITLE

build_exe_options = {"packages": ["pygame"], "excludes": ["tkinter", "test"], "include_files": ["assets/", "fonts/"]}

base = None
if sys.platform == "win32":
    base = "Win32GUI"

setup(
    name=GAME_TITLE,
    version="1.0",
    description="Game made for Pygame Community Spring Jam 2024",
    options={"build_exe": build_exe_options},
    executables=[Executable(script="main.py", base=base)],
)
