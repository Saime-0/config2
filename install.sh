#!/bin/bash

# Директория с шагами
STEPS_DIR="install-by-step"

# Переход в директорию с шагами
cd "$STEPS_DIR" || { echo "Error: The $STEPS_DIR directory was not found."; exit 1; }

# Проход по всем файлам в директории, отсортированным по имени
for script in $(ls -v *.sh); do
    echo "Running the script: $script"
    # Выполнение скрипта
    bash "$script"
    # Проверка кода завершения
    if [ $? -ne 0 ]; then
        echo "Error: the $script script failed with an error. Execution stopped."
        exit 1
    fi
done

echo "All the steps are completed successfully."