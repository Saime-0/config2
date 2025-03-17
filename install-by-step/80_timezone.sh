#!/bin/bash

# timezone
ln -sf /usr/share/zoneinfo/Europe/Moscow /etc/localtime 
hwclock --systohc
