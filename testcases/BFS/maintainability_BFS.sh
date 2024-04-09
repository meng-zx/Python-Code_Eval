#!/bin/bash

FILE="BFS.py" # Modify the file name
echo "======================================="
echo "Analyzing maintainability of $FILE"
echo "======================================="
echo ""
if ! command -v radon &> /dev/null
then
    echo "radon could not be found, please install it first."
    echo "You can install radon using: pip install radon"
    exit 1
fi

echo "====================================="
echo "Cyclomatic Complexity (CC)"
echo "-------------------------------------"
radon cc $FILE -a
echo "====================================="
echo ""

echo "====================================="
echo "Halstead Metrics"
echo "-------------------------------------"
radon hal $FILE
echo "====================================="
echo ""

echo "====================================="
echo "Raw Metrics"
echo "-------------------------------------"
radon raw $FILE
echo "====================================="
echo ""

echo "====================================="
echo "Maintainability Index (MI)"
echo "-------------------------------------"
radon mi $FILE -s
echo "====================================="
