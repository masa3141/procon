# -*- coding: utf-8 -*-
import re

s = input()
s = re.sub('eraser?', '1', s)
s = re.sub('dream(er)?', '1', s)
print('YES' if len(s) == s.count('1') else 'NO')