import subprocess

cmd = "python --version"

print(subprocess.check_output(cmd, shell=True, text=True))


# OR


import platform

print("Python Version:")

print(platform.python_version_tuple())