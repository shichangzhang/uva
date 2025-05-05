#! /bin/bash
# Add new test

cd $(dirname ${BASH_SOURCE[0]})

if [ $# != 2 ]
then
	echo "Usage: $0 [PROBLEM_NUMBER] [TEST_NUMBER]"
	exit 1
fi

touch tests/$1_test$2_input.txt tests/$1_test$2_output.txt
