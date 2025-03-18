#!/bin/python

import os

# Директория с шагами
STEPS_DIR = "install"

# Переход в директорию с шагами
try:
    os.chdir(STEPS_DIR)
except FileNotFoundError:
    print(f"Error: The {STEPS_DIR} directory was not found.")
    exit(1)

# Получаем список всех .sh файлов, отсортированных по имени
script_files = sorted([f for f in os.listdir() if f.endswith(".sh")])

# Собираем все скрипты в одну строку
combined_script = "#!/bin/bash\n\n"  # Добавляем shebang
for script_file in script_files:
    print(f"Adding script: {script_file}")
    with open(script_file, "r") as file:
        combined_script += f"# --- {script_file} ---\n"
        combined_script += file.read() + "\n\n"

# Добавляем проверку кода завершения
combined_script += """
# Проверка кода завершения
if [ $? -ne 0 ]; then
    echo "Error: One of the scripts failed with an error. Execution stopped."
    exit 1
fi
"""

# Сохраняем объединенный скрипт во временный файл
temp_script_path = "combined_script.sh"
with open(temp_script_path, "w") as temp_script:
    temp_script.write(combined_script)

# Делаем временный скрипт исполняемым
os.chmod(temp_script_path, 0o755)

# Запускаем объединенный скрипт
print("Running the combined script...")
exit_code = os.system(f"./{temp_script_path}")

# Удаляем временный скрипт
os.remove(temp_script_path)

# Проверяем код завершения
if exit_code != 0:
    print("Error: The combined script failed with an error. Execution stopped.")
    exit(1)

print("All the steps are completed successfully.")