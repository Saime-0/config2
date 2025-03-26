### install

```sh
git clone --depth 1 https://github.com/Saime-0/config2.git
cd config2
DEVICE=/dev/sdx ./install.sh
```

### postinstall

1. Скопировать директорию config2 в /mnt/home/okg0
2. Перезагрузиться в систему либо из arch-chroot выполнить

```sh
su okg0
./postinstall.py
```

#### todo

- [ ] Перезаписывать файлы конфигов в postinstall
- [ ] Настройка ssh
- [ ] Настройка git
- [ ] Создание структуры директорий
- [ ] Добавить help.sh
- [ ] Реализовать использование postinstall в cli для устнавки или настройки единичных пакетов