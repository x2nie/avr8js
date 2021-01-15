N = 0

with open('instruction-rep.ts') as f:
    lines = f.readlines()


def keep(l, i):
    l = l.rstrip()
    l = l.replace('} else if ', '')
    l = l.replace('{', '')
    global N
    N += 1
    next = lines[i+1]
    if next.strip() == ') {':
        next = lines[i+2]

    if next.startswith('    /*'):
        comment = next.rstrip()
    else:
        comment = ''
    if '0x' in l:
        s = l.find('0x')
        e = l.find(')')
        k = l[s:e]
    else:
        k = ''
    print '%03s %-7s' % (i+1, k), l.rstrip(), comment


# print lines[:3]
for i, l in enumerate(lines):
    if l.startswith('  } else if ((opcode ') or l.startswith('  } else if (opcode '):
        keep(l, i)
    elif l.startswith('    (opcode &') or l.startswith('    | ((opcode '):
        keep(l, i)

print 'total found:', N
