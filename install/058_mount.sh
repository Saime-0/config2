#!/bin/bash

set -e

echo "Checking if the device exists ..."
if [ ! -e "$DEVICE" ]; then
  echo "Error: Device '$DEVICE' (\$DEVICE) not found."
  exit 1
fi

echo "Mounting partitions ..."
mount ${DEVICE}2 /mnt
mount --mkdir ${DEVICE}1 /mnt/boot

echo "The partitions are mounted in /mnt."