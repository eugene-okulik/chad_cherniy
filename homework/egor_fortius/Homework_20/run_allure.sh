#!/bin/bash
# run_allure.sh — запуск тестов с историей для Allure 2

RESULTS="./allure-results"
REPORT="./allure-report"

echo "🧪 Запуск тестов..."
pytest --alluredir=$RESULTS -v

echo "📦 Копирование истории..."
# Копируем историю из прошлого отчёта в результаты (если есть)
if [ -d "$REPORT/history" ]; then
    cp -r "$REPORT/history" "$RESULTS/"
    echo "✅ История скопирована"
else
    echo "ℹ️  Первый запуск — история будет создана после генерации"
fi

echo "📊 Генерация отчёта..."
allure generate "$RESULTS" -o "$REPORT" --clean

echo "🚀 Отчёт готов: $REPORT/index.html"
allure open "$REPORT"
