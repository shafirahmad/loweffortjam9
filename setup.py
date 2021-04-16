import cx_Freeze

exe = [cx_Freeze.Executable("peashooter.py", base = "Win32GUI")] # <-- HERE

cx_Freeze.setup(
    name = "Mizatorian Peashooter",
    version = "1.0",
    options = {"build_exe": {"packages": ["pygame", "random", "math", "sys", "io", "time"],  
        "include_files": ["music.mid","sfxr_bounce.wav","sfxr_ohoh.wav",
        "sfxr_shoot.wav","sfxr_score.wav",
        "at01.ttf"]}},
    executables = exe
) 