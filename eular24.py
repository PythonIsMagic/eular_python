#!/usr/bin/env python3
import itertools

perms = list(itertools.permutations(str('0123456789'), len('0123456789')))
print(''.join(perms[999999]))
