"""
Finds all duplicated lines within each CSV file as well as across all files.
It outputs the duplicated line with a list of two or more filenames with
line numbers of the duplicated lines.

A sample line in the output looks like:
到未啊,dou3 mei6 aa3	[phrase_fragment.csv:1830, word.csv:11234]

This means that the line "到未啊,dou3 mei6 aa3" is duplicated
in phrase_fragment.csv on line 1830 and in word.csv on line 11234.
"""
from collections import defaultdict
from glob import iglob
import sys

line_to_locations = defaultdict(list)

for filename in iglob('*.csv'):
    with open(filename) as f:
        assert next(f).startswith('char,jyutping'), 'Invalid CSV header'
        
        for line_num, line in enumerate(f, 2):
            location = f'{filename}:{line_num}'
            line_to_locations[line].append(location)

has_error = False

for line, locations in line_to_locations.items():
    if len(locations) > 1:
        has_error = True
        locations_str = ' and '.join(locations)
        print(f'WARNING: {line.strip()} is duplicated in {locations_str}\n', file=sys.stderr)

if has_error:
    sys.exit(1)
