#! /bin/bash

for tst in $(ls test_*.py)
do
    coverage run -p "${tst}"   
done

coverage combine
