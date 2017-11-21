#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Copyright 2017 Sebastian Schmittner

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.

"""
import re
import sys


def shorten_tofu_blocks(input):
    pattern = r"(?s)gpg: Verified ([0-9]+) .*bad\."
    replace = r"gpg: TOFU \1"
    return re.sub(pattern, replace, input)


def main():
    input = sys.stdin.read()
    input = shorten_tofu_blocks(input)
    sys.stdout.write(input)


# goto main
if __name__ == "__main__":
    main()
