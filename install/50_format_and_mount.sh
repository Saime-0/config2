#!/bin/bash

echo " Проверка, существует ли устройство ..."
if [ ! -e "$DEVICE" ]; then
  echo "Ошибка: Устройство $DEVICE не найдено."
  exit 1
fi

echo "Очистка таблицы разделов ..."
sfdisk --delete $DEVICE

echo "Создание разделов ..."
sfdisk $DEVICE << EOF
label: gpt
,512M,EF00
,,8300
EOF

echo "Форматирование разделов ..."
mkfs.fat -F 32 ${DEVICE}1  # EFI раздел
fatlabel /dev/sda1 BOOT
mkfs.ext4 ${DEVICE}2 -L ROOT      # Root раздел

echo "Монтирование разделов ..."
mount ${DEVICE}2 /mnt
mount --mkdir ${DEVICE}1 /mnt/boot

echo "Разметка диска завершена. Разделы смонтированы в /mnt."