#!/usr/bin/env bash
set -e

cd "$(dirname "$(readlink -f "$BASH_SOURCE")")/.."

# this is hard work

'''
This file lists all individuals having contributed content to the repository.
this file is generate-authors.sh
'''

{
	cat <<- 'EOH'
	EOH
	echo
	git log --format='%aN <%aE>' | LC_ALL=C.UTF-8 sort -uf
} > AUTHORS
