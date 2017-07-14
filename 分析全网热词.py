import jieba.analyse
import pp


def fun(x):
    tmp = jieba.analyse.extract_tags(x, 0, withWeight=True)
    return tmp


def FileOpen(FileName):
    res = ""
    f = open(FileName, "r", encoding="UTF-8").read()
    for n in f:
        if n != "\n":
            res = res + n
    return res


def StatisticsWeigth(str, a):
    weigth = 0.0
    for y in a:
        for x in y:
            if str in x:
                weigth = weigth + float(x[1])
                break
    return weigth


def StatisticsAll(Intersection, Analyse):
    res = []
    for x in Intersection:
        weight = StatisticsWeigth(x[:-1], Analyse)
        if weight == 0.0:
            continue
        tmp = (x[:-1], weight)
        res = res + [tmp]
    return res


FileName = ["网易新闻new.txt", "新浪新闻new.txt", "搜狐新闻new.txt", "人民网new.txt", "凤凰资讯new.txt"]

DataList = {}
Data = []
for x in FileName:
    DataList[x] = open(x, "r", encoding="UTF-8").readlines()
for x in FileName:
    tmp = FileOpen(x)
    Data = Data + [tmp]

Assemble = []
for x in FileName:
    tmp = [set(DataList[x])]
    Assemble = Assemble + tmp
And = Assemble[0]
for x in Assemble:
    And = And & x
Intersection = list(And)
seq = 0
IntersectionCut = []
count = len(Intersection)
while 1:
    if seq + 1000 >= count:
        cut = IntersectionCut + [Intersection[seq:]]
        break
    IntersectionCut = IntersectionCut + [Intersection[seq:seq + 1000]]
    seq = seq + 1000

Analyse = []
job_server = pp.Server()
jobs = []
for x in Data:
    tmp = [job_server.submit(fun, args=(x,), modules=("jieba.analyse",))]
    jobs = jobs + tmp

for job in jobs:
    tmp = [job()]
    Analyse = Analyse + tmp

# ——————————————————————————————————————————————
# 分析网络热词
jobs.clear()
IntersectionWithWeigth = []
for x in IntersectionCut:
    tmp = [job_server.submit(StatisticsAll, (x, Analyse), (StatisticsWeigth,))]
    jobs = jobs + tmp
for job in jobs:
    tmp = job()
    IntersectionWithWeigth = IntersectionWithWeigth + tmp

final = []
while 1:
    weigth = 0.0
    world = ""
    for x in IntersectionWithWeigth:
        if x[1] >= weigth:
            if x not in final:
                world = x[0]
                weigth = x[1]
    final = final + [(world, weigth)]
    if len(final) >= 15:
        break

for x in final:
    print(x)
# ——————————————————————————————————————————————
