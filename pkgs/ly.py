import subprocess

class ly:
    pkg_name="ly"

    def setup():
        subprocess.run(["sudo", "systemctl", "enable", "ly.service"], shell=True, check=True, text=True)