import subprocess

def view():
    info = (subprocess.check_output("lscpu", shell=True).strip()).decode()
    return info

