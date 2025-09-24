#!/bin/bash


BASE_DIR="./allure"
RESULTS_DIR="$BASE_DIR/allure-results"
REPORT_DIR="$BASE_DIR/allure-report"

mkdir -p "$BASE_DIR"


if [ -d "$RESULTS_DIR" ]; then
    rm -rf "$RESULTS_DIR"
fi

if [ -d "$REPORT_DIR" ]; then
    rm -rf "$REPORT_DIR"
fi


pytest --alluredir="$RESULTS_DIR"


if [ -d "$RESULTS_DIR" ] && [ "$(ls -A $RESULTS_DIR)" ]; then
    allure generate "$RESULTS_DIR" --clean -o "$REPORT_DIR"
    allure open "$REPORT_DIR"
else
    echo "No test results were found to generate a report."
fi