#!/usr/bin/env python
import argparse

def proc(infile):
    rows = []
    columns = []
    curr_column = []
    with open(infile) as f:
        for line in f:
            line = line.strip().decode('utf8', 'ignore')
            if line.startswith('%'):
                line = line.replace('%', '').strip()
                columns.append(list(curr_column))
                curr_column = []
            if line.startswith('#'):
                line = line.replace('#', '').strip()
                columns.append(list(curr_column))
                rows.append(list(columns))
                columns = []
                curr_column = []
            curr_column.append(line)
        columns.append(list(curr_column))
        rows.append(list(columns))

    # unify rows
    unified_columns = []
    for row in rows:
        for (i, col) in enumerate(row):
            try:
                unified_columns[i] += col
            except IndexError:
                unified_columns.append(col)

    columns = unified_columns
    max_widths = [ max([ len(line) for line in col ]) for col in columns ]
    max_rows = max([ len(col) for col in columns ])

    s = []
    for i in xrange(max_rows):
        r = ''
        for (j, col) in enumerate(columns):
            width = max_widths[j]
            try:
                val = col[i]
            except IndexError:
                val = ''
            padding = width + 3 - len(val)
            r += val
            r += ' ' * padding

        s.append(r)
    print '\n'.join(s)
    print 'MAXLEN:%d' % max([len(r) for r in s])
            

a = argparse.ArgumentParser()
a.add_argument('infile')
p = a.parse_args()

proc(p.infile)
