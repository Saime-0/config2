#!/bin/bash

# system
pacstrap /mnt base linux linux-firmware
genfstab -U /mnt >> /mnt/etc/fstab
arch-chroot /mnt

# locale
echo "en_US.UTF-8 UTF-8" > /etc/locale.gen
echo "ru_RU.UTF-8 UTF-8" > /etc/locale.gen
locale-gen
echo "LANG=en_US.UTF-8" > /etc/locale.conf

# timezone
ln -sf /usr/share/zoneinfo/Europe/Moscow /etc/localtime 
hwclock --systohc


#echo ${HOSTNAME} > /etc/hostname

# exec mkinitcpio -p linux for generate the initramfs image
# exec passwd and enter password for root

# grub
pacman -S grub efibootmgr
grub-install --target=x86_64-efi --efi-directory=/boot --bootloader-id=GRUB
grub-mkconfig -o /boot/grub/grub.cfg

passwd