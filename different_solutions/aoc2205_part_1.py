a = []
op = []
# with open('test') as file:
with open('2205.0') as file:
    ok = False
    for s in file:
        s = s[:len(s) - 1]        
        if s == '':
            ok = True
        if not ok:
            a.append(s)
        else:
            op.append(s)
tt = int(list(a[-1])[-2])
a.pop()
aa = [[] for _ in range(tt)]
for s in a:
    for i in range(tt):
        c = s[1 + 4 * i]
        if ord('A') <= ord(c) <= ord('Z'):
            aa[i].insert(0, c)
op.pop(0)
for s in op:
    ss = s.split()
    m, f, t = int(ss[1]), int(ss[3]) - 1, int(ss[5]) - 1

    for i in range(m):
        if len(aa[f]) == 0:
            continue
        aa[t].append(aa[f].pop())

r = ''
for i in range(tt):
    r += aa[i][-1]

print(r)
