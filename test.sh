#! /bin/bash
# Run all tests for UVa problem

cd $(dirname ${BASH_SOURCE[0]})

if [ $# != 1 ]
then
	echo "Usage: $0 [PROBLEM_NUMBER]"
	exit 1
fi

for test_file in $(ls tests/$1_test*_input.txt)
do
	echo $test_file
	output_file=${test_file/%_input.txt/_output.txt}
	diff -y <(python solutions/$1.py < $test_file) $output_file
	echo
done