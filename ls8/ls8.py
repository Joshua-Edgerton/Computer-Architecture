#!/usr/bin/env python3

"""Main."""

import sys
from cpu import CPU
print("sys.argv", sys.argv)
cpu = CPU()

cpu.load(sys.argv[1])
cpu.run()