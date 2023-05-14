#!/bin/bash

python -m unittest $(find . -type d | xargs -I {} python unittest_enumerator.py {} | fzf) -v
exit $?

