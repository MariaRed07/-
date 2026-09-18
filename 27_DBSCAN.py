f = open('27_B_1_YA_ZNAK.txt')
f.readline()

data = []
for s in f:
    s = s.replace(',', '.')
    p = [float(c) for c in s.split()]
    data.append(p)

from math import dist

def DBSCAN(p0):
    cluster = [p for p in data if dist(p0, p) < 1]
    if len(cluster) > 0:
        for p in cluster: data.remove(p)
        next_cluster = [DBSCAN(p) for p in cluster]
        cluster = cluster + sum(next_cluster, [])
    return cluster

clusters = []
while len(data) > 0:
    p0 = data.pop()
    cluster = [p0] + DBSCAN(p0)
    clusters.append(cluster)

def centr(cl):
    m = []
    for p in cl:
        s = sum(dist(p, p1) for p1 in cl)
        m.append([s, p])
    return min(m)[1]

# c0 = centr(clusters[0])
# c1 = centr(clusters[1])
# print(c0, c1)
# print(int((c0[0]+c1[0])/2 * 10000))
# print(int((c0[1]+c1[1])/2 * 10000))
# print(int(((2.67836329019008 + -0.530720837096502)/2) * 10000))
# print(int(((4.82882470874288 + 1.31719050307274)/2) * 10000))

c0 = centr(clusters[0])
c1 = centr(clusters[1])
C2 = centr(clusters[2])
print(int((c0[0]+c1[0]+C2[0])/3 * 10000))
print(int((c0[1]+c1[1]+C2[1])/3 * 10000))