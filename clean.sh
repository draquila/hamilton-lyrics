#!/bin/bash
find . -not \( -name .svn -prune -o -name .git -prune \) -name *.lrc -type f -print0 | xargs -0 dos2unix
find . -not \( -name .svn -prune -o -name .git -prune \) -name *.lrc -type f -print0 | xargs -0 /usr/bin/sed -i '' -E "s/[[:space:]]*$//"
