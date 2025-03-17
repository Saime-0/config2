#!/bin/bash

set -e

# Создаем временную директорию для скриптов
chroot_scripts_dir=/root/tmp/install$(date +%s)
scripts_dir=/mnt$chroot_scripts_dir
mkdir -p $scripts_dir

# Копируем скрипты из родительской директории
parent_dir=$(dirname -- "$(readlink -f -- "$BASH_SOURCE")")
cp $parent_dir/065_chroot/* $scripts_dir

# Делаем скрипты исполняемыми
arch-chroot /mnt bash -c "chmod +x ${chroot_scripts_dir}/*"

# Запускаем все скрипты по очереди
for script in $(arch-chroot /mnt bash -c "ls ${chroot_scripts_dir}"); do
    echo "Running script: ${script}"
    arch-chroot /mnt bash -c "${chroot_scripts_dir}/${script}"
done