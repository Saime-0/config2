import subprocess

def create_user(
    login:str,
    groups: list[str],
    switch: bool = False,
):
    subprocess.run(["useradd", login], shell=True, check=True, text=True) 
    # if len(groups) == 0:
    #     return
    # ' '.join(groups)
    for group in groups:
        subprocess.run(["usermod", "-aG", group, login], shell=True, check=True, text=True) 

    subprocess.run(["passwd", login], shell=True, check=True, text=True)

    if switch:
        pass
    