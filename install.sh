#!/bin/bash

scripts_dir="install"

cd "$scripts_dir" || { echo "Error: The '$scripts_dir' directory was not found."; exit 1; }

# Проход по всем файлам в директории, отсортированным по имени
for script in $(ls -v *.sh); do
    echo "Running the script: $script"
    bash "$script"
    # Проверка кода завершения
    if [ $? -ne 0 ]; then
        echo "Error: the $script script failed with an error. Execution stopped."
        exit 1
    fi
done

echo "All the steps are completed successfully."