#!/bin/bash

# Крок 1: Очищуємо папку з результатами перед кожним запуском.
if [ -d "./test_results" ]; then
    rm -rf ./test_results
fi

# Крок 2: Запускаємо тести, які згенерують нові JSON-файли.
pytest --alluredir=./test_results

# Крок 3: Перевіряємо, чи були згенеровані результати, перш ніж генерувати звіт.
if [ -d "./test_results" ]; then
    # Генеруємо HTML-звіт і зберігаємо його в папці allure_report.
    allure generate ./test_results --clean -o ./allure_report

    # Крок 4: Автоматично відкриваємо звіт в браузері.
    allure open ./allure_report
else
    # Якщо тести не створили результатів, виводимо відповідне повідомлення.
    echo "No test results were found to generate a report."
fi