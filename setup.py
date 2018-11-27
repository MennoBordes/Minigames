import cx_Freeze
executables = [cx_Freeze.Executable("Intro.py")]

cx_Freeze.setup(
    name="Return to Eden",
    options={"build_exe": {"packages": ["pygame"]}},
    executables=executables
)
