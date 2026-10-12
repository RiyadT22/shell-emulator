#!/bin/sh
cd "$(dirname "$0")/.." || exit 1
python3 src/main.py --vfs vfs/demo --script scripts/missing.txt
