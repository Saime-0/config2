#!/bin/bash

pacman -Sy git vim networkmanager python sudo --noconfirm --needed --sysroot /mnt

arch-chroot /mnt /bash -c "systemctl enable --now NetworkManager.service"