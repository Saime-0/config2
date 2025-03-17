#!/bin/bash

# Директория с шагами
STEPS_DIR="install-by-step"

# Переход в директорию с шагами
cd "$STEPS_DIR" || { echo "Error: The $STEPS_DIR directory was not found."; exit 1; }

gen_script=""

# Проход по всем файлам в директории, отсортированным по имени
for script_file in $(ls -v *.sh); do
    script=$(cat $script)
    gen_script="
    ${gen_script}
    echo "Running the script: $script_file"
    ${script}
    # Проверка кода завершения
    if [ $? -ne 0 ]; then
        echo "Error: the $script_file script failed with an error. Execution stopped."
        exit 1
    fi
    "
done

# Выполнение скрипта
bash "$gen_script"

echo "All the steps are completed successfully."