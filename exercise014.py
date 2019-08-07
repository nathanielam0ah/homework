#!/usr/bin/env python

import re
string = "the quick brown fox jumps over the lazy dog"
match = re.search(r"the", string)

if match:
	print("Found"),match.group()
else:
	print("Cannot find")
