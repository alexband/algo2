f = open('jobs.txt', 'r')
num = int(f.readline().strip())
jobs = []
for l in f:
    l = l.strip().split()
    jobs.append((long(l[0]), long(l[1])))
jobs.sort(key=lambda x:x[0])

def keyfun1(a, b):
    val1 = a[0] - a[1]
    val2 = b[0] - b[1]
    if val1 == val2:
        return int(a[0] - b[0])
    else:
        return int(val1 - val2)

def compare(jobs, factor):
    if factor == 'd':
        jobs = sorted(jobs, cmp=keyfun1, reverse=True)
    elif factor == 'r':
        jobs = sorted(jobs, key=lambda x: x[0]/float(x[1]), reverse=True)
    return jobs
    
def ws(jobs):
    val = 0
    acc = 0
    for index, j in enumerate(jobs):
        value = j[0] * (acc+j[1])
        acc += j[1]
        val += value
    return  val


jobs = compare(jobs, 'd')
print ws(jobs)
jobs = compare(jobs, 'r')
print ws(jobs)
f.close()
