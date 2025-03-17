#!/bin/bash

echo "Checking if the device exists ..."
if [ ! -e "$DEVICE" ]; then
  echo "Error: Device '$DEVICE' (\$DEVICE) not found."
  exit 1
fi

echo "Clearing the partition table ..."
sfdisk --delete $DEVICE

echo "Create partitions ..."
sfdisk $DEVICE << EOF
label: gpt
,512M,EF00
,,8300
EOF

echo "Formatting partitions ..."
mkfs.fat -F 32 ${DEVICE}1  # EFI раздел
fatlabel /dev/sda1 BOOT
mkfs.ext4 ${DEVICE}2 -L ROOT      # Root раздел

echo "Mounting partitions ..."
mount ${DEVICE}2 /mnt
mount --mkdir ${DEVICE}1 /mnt/boot

echo "The disk partition is complete. The partitions are mounted in /mnt."