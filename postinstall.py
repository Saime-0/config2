#!/bin/python

from pkgs import *

pacman.setup()

# Install base packages
pacman.install(base_pkg_names)

# Get pacman wrapper
pacman.install([rustup.pkg_name])
rustup.setup()
paru.get()
paru.setup()

#fonts
paru.install(fonts_pkg_names)

# de
paru.install(xfce.pkg_names)
xfce.setup()

# Install opt packages
opt_pkgs = [
    vscode,
    terminus_font,
    alacritty,
    helix,
    ly,
    bluetooth,
    xdg_user_dirs,
    bash,
    gnome_keyring,
]
opt_pkgs_names = [
    # Внешний вид:
    "fluent-gtk-theme", # Тема оконного менеджера
    "gruvbox-dark-icons-gtk", # Иконки
    "elementary-icon-theme", # Курсор

    "go",
    "delve",
    "mockery",
    "gopls",
    "jdk-openjdk",

    "pcmanfm",
    "gvfs",

    "xarchiver",
    "qbittorrent",
    "golangci-lint",
    "obs-studio",
    "libreoffice-still",
    "telegram-desktop",
] + [p.pkg_name for p in opt_pkgs]
paru.install(opt_pkgs_names)

# Setup opt packages
for p in opt_pkgs:
    if hasattr(p, 'setup') and callable(getattr(p, 'setup')):
        p.setup()


# TODO: Переписать на декларативный вариант:
# def get_or_install_and_setup(*package_groups: list[str | object] | object | str):
#     def one(p: object | str):
#         if 'p has get()':
#             'p.get()' 
#         elif 'p is str':
#             'lib.get_package_manager.install(p)'
#         elif 'p has pkg_name':
#             'lib.get_package_manager.install(p.pkg_name)'

#         if 'p has setup()':
#             pass

#     for pg in package_groups:
#         if 'pg is itarble':
#             for p in pg:
#                 one(p)
#         else:
#             one(p)


# get_or_install_and_setup(
#     pacman,
#     base_pkg_names,
#     rustup,
#     paru,
#     [vscode, terminus_font]
# )