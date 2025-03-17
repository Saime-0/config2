#!/bin/bash

# Проверка наличия аргумента (устройства)
if [ -z "$1" ]; then
  echo "Ошибка: Укажите устройство в качестве первого аргумента."
  echo "Пример использования: $0 /dev/sda"
  exit 1
fi

# Устройство, переданное в качестве аргумента
DEVICE="$1"

# Проверка, существует ли устройство
if [ ! -e "$DEVICE" ]; then
  echo "Ошибка: Устройство $DEVICE не найдено."
  exit 1
fi

# Очистка таблицы разделов
sfdisk --delete $DEVICE

# Создание разделов
sfdisk $DEVICE << EOF
label: gpt
,512M,EF00
,,8300
EOF

# Форматирование разделов
mkfs.fat -F 32 ${DEVICE}1  # EFI раздел
fatlabel /dev/sda1 BOOT
mkfs.ext4 ${DEVICE}2 -L ROOT      # Root раздел


# Монтирование разделов
mount ${DEVICE}2 /mnt
mount --mkdir ${DEVICE}1 /mnt/boot

echo "Разметка диска завершена. Разделы смонтированы в /mnt."

swapfile="/mnt/.swapfile"

dd if=/dev/zero of=${swapfile} bs=1024 count=2097152 # 2GB size
chmod 600 ${swapfile}
mkswap ${swapfile}
swapon ${swapfile}

echo "Создан swapfile."
