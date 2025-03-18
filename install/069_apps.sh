#!/bin/bash

pacman -Sy git vim networkmanager python sudo --noconfirm --needed --sysroot /mnt

arch-chroot /mnt bash -c "systemctl enable --now NetworkManager.service"
echo "%wheel  ALL=(ALL:ALL)    NOPASSWD:SETENV: ALL" > /mnt/etc/sudoers.d/wheel