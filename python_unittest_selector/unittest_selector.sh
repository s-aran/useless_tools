#!/bin/bash

TEST=$(find . -type d | xargs -I {} python unittest_enumerator.py {} | fzf)
if [ $? -ne 0 ]; then
  exit 1
fi

python -m unittest $TEST $@
exit $?

