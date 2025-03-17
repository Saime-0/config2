#!/bin/bash

set -e

chroot_scripts_dir=/root/tmp/install$(date +%s)
scripts_dir=/mnt$chroot_scripts_dir
mkdir -p $scripts_dir
parent_dir=$(dirname -- "$(readlink -f -- "$BASH_SOURCE")")
cp $parent_dir/065_chroot/* $scripts_dir
arch-chroot /mnt bash -c "chmod +x ${chroot_scripts_dir}/*"
arch-chroot /mnt bash -c "${chroot_scripts_dir}/*"
