#!/bin/python

import pkgs
import lib
import os

pkgs.pacman.setup()
pkgs.pacman.install(
    packages=pkgs.base_packages,
    no_confirm=True,
    needed=True,
)

# login="okg0"
# lib.create_user(
#     login=login,
#     groups=["sudo", "networkmanager", "uinput"]
# )

pkgs.paru.get()
pkgs.paru.setup()
pkgs_for_install = [
    pkgs.vscode,
    # pkgs.dummy
]
pkgs.paru.install(
    packages=pkgs_for_install,
    no_confirm=True,
    needed=True,
)

for p in pkgs_for_install:
    if hasattr(p, 'setup') and callable(getattr(p, 'setup')):
        p.setup()
