#!/bin/bash
pip freeze > .requirements.tmp
if ! cmp -s .requirements.tmp requirements.txt; then
    mv .requirements.tmp requirements.txt
    git add requirements.txt
fi
