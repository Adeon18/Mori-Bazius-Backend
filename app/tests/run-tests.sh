#! /bin/bash

echo "Running tests..."

all_passed=0

for tst in $(ls test_*.py)
do
    coverage run -p "${tst}"

    if [ $? -eq 1 ]; then
        all_passed=1
    fi
done

if [ "${all_passed}" -eq 1 ]; then
    exit 1
fi

echo "Combining results..."
coverage combine

echo "Results:"
coverage report
