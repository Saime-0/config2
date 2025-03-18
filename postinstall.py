#!/bin/python

import pkgs
# import lib
# import os

pkgs.pacman.setup()
pkgs.pacman.install(pkgs.base_pkg_names)

# login="okg0"
# lib.create_user(
#     login=login,
#     groups=["sudo", "networkmanager", "uinput"]
# )

pkgs_for_install = [
    pkgs.vscode,
]
pkgs.paru.get()
pkgs.paru.setup()
pkgs.paru.install([p.pkg_name for p in pkgs_for_install])

for p in pkgs_for_install:
    if hasattr(p, 'setup') and callable(getattr(p, 'setup')):
        p.setup()
