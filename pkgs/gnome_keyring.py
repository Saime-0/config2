import subprocess



class gnome_keyring:
    pkg_name = "gnome-keyring"

    def setup():
        subprocess.run('echo "password	optional	pam_gnome_keyring.so" | sudo tee -a /etc/pam.d/passwd', stdout=subprocess.DEVNULL, check=True)
        subprocess.run("sudo sed -i '/^auth.*/a auth       optional     pam_gnome_keyring.so' /etc/pam.d/login", shell=True, check=True, text=True)
        subprocess.run("sudo sed -i '/^session.*/a session    optional     pam_gnome_keyring.so auto_start' /etc/pam.d/login", shell=True, check=True, text=True)
