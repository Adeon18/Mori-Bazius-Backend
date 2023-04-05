#! /bin/bash

echo "Running tests..."
for tst in $(ls test_*.py)
do
    coverage run -p "${tst}"   
done

echo "Combining results..."
coverage combine

echo "Results:"
coverage report
