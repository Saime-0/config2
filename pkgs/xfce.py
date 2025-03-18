import subprocess
import os
import shutil

script_parent = os.path.dirname(os.path.abspath(__file__))
config_src = os.path.join(script_parent, "../dotfiles/.config/xfce4")
config_dst=os.path.expanduser("~/.config/xfce4")

class xfce:
    pkg_names = [
        "exo", # Библиотеки и утилиты для управления файлами и приложениями
        "garcon", #	Меню-система для XFCE (интеграция с приложениями)	Да
        # thunar	Файловый менеджер по умолчанию для XFCE	Да
        # thunar-volman	Автоматическое монтирование съёмных носителей для Thunar	Нет (рекомендуется)
        "tumbler", # Сервис для генерации превью файлов (миниатюры)	Да
        "xfce4-appfinder", # Поиск и запуск установленных приложений	Нет
        "xfce4-panel", # Панель управления XFCE (основной элемент интерфейса)	Да
        "xfce4-power-manager", # Управление питанием (яркость, спящий режим и т.д.)	Нет (рекомендуется)
        "xfce4-session", # Менеджер сессий (автозагрузка, сохранение сеанса)	Да
        "xfce4-settings", # Центр настроек XFCE (внешний вид, устройства и т.д.)	Да
        # xfce4-terminal	Терминал по умолчанию	Нет
        "xfconf", # Система хранения настроек XFCE	Да
        "xfdesktop", # Менеджер рабочего стола (обои, значки)	Да
        "xfwm4", # Оконный менеджер XFCE	Да
        "xfwm4-themes", # Дополнительные темы для оконного менеджера	Нет
        # Дополнительные пакеты (группа xfce4-goodies)
        # Пакет	Описание	Обязателен для XFCE?
        # mousepad	Текстовый редактор для XFCE	Нет
        # parole	Медиаплеер для XFCE	Нет
        "ristretto", # Просмотр изображений	Нет
        # thunar-archive-plugin	Интеграция с архивами (ZIP, RAR и т.д.) в Thunar	Нет
        # thunar-media-tags-plugin	Поддержка медиатегов в Thunar	Нет
        # xfburn	Утилита для записи дисков	Нет
        # xfce4-artwork	Обои и графика для XFCE	Нет
        "xfce4-battery-plugin", # Плагин для отображения уровня заряда батареи	Нет
        "xfce4-clipman-plugin", # Менеджер буфера обмена	Нет
        "xfce4-cpufreq-plugin", # Мониторинг частоты CPU	Нет
        "xfce4-cpugraph-plugin", # График загрузки CPU	Нет
        # xfce4-dict	Словарь (поиск слов через интернет)	Нет
        "xfce4-diskperf-plugin", # Мониторинг производительности диска	Нет
        # xfce4-eyes-plugin	Плагин с анимированными "глазами"	Нет
        "xfce4-fsguard-plugin", # Мониторинг свободного места на диске	Нет
        "xfce4-genmon-plugi", # 	Плагин для вывода произвольных команд в панель	Нет
        # xfce4-mailwatch-plugin	Уведомления о новой почте	Нет
        "xfce4-mount-plugin", # Быстрое монтирование устройств	Нет
        "xfce4-mpc-plugin", # Управление медиаплеером MPD	Нет
        "xfce4-netload-plugin", # Мониторинг сетевой нагрузки	Нет
        # xfce4-notes-plugin	Заметки на панели	Нет
        "xfce4-notifyd", # Система уведомлений	Нет
        # xfce4-places-plugin	Быстрый доступ к часто используемым папкам	Нет
        "xfce4-pulseaudio-plugin", # Управление звуком через PulseAudio	Нет
        "xfce4-screensaver", # Хранитель экрана	Нет
        "xfce4-screenshooter", # Утилита для создания скриншотов	Нет
        "xfce4-sensors-plugin", # Мониторинг температуры компонентов	Нет
        # xfce4-smartbookmark-plugin	Поиск через закладки в браузере	Нет
        "xfce4-systemload-plugin", # Мониторинг загрузки системы	Нет
        "xfce4-taskmanager", # Диспетчер задач	Нет
        # xfce4-time-out-plugin	Таймеры для перерывов	Нет
        # xfce4-timer-plugin	Таймер/секундомер	Нет
        # xfce4-verve-plugin	Командная строка в панели	Нет
        "xfce4-wavelan-plugin", # Мониторинг Wi-Fi-соединения	Нет
        # xfce4-weather-plugin	Погода на панели	Нет
        "xfce4-whiskermenu-plugin", # Альтернативное меню приложений (аналог меню Windows)	Нет
        "xfce4-xkb-plugin", # Переключение раскладки клавиатуры	Нет
        "network-manager-applet", # Графический интерфейс для управления сетевыми подключениями в Linux
    ]
    pkg_name = ' '.join(pkg_names)
    
    def setup():
        # Скопировать конфиг
        shutil.copytree(config_src, config_dst, dirs_exist_ok=True)