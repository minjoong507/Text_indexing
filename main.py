import os
import makeresult as MR
import preprocess as PP
import operator
from matplotlib import pyplot as plt

searchwords = PP.Preprocessing().preprocess(input())
searchVector = {}
VectorList = []
DocFreq = {}
for i in searchwords.keys():
    searchVector[i] = searchwords[i]
    DocFreq[i] = 0

FileList = []

for file in os.listdir("C:\\Users\\82109\\PycharmProjects\\Text_Indexing"):
    if file.endswith(".txt"):
        FileList.append(file)

for i in FileList:
    f = open(i, 'r')
    data = f.read()
    result = PP.Preprocessing().preprocess(data)
    datalist = list(result.keys())
    Vector = {}
    for j in searchwords:
        if j in datalist:
            Vector[j] = result[j]
            DocFreq[j] += 1
        else:
            Vector[j] = 0
    VectorList.append(Vector)

DocFreq = MR.multifunction().makeIdf(DocFreq, len(FileList))
IDF = list(DocFreq.keys())
for i in VectorList:
    for j in IDF:
        if j in i.keys():
            i[j] = DocFreq[j] * i[j]

for i in IDF:
    if i in searchVector.keys():
        searchVector[i] = searchVector[i] * DocFreq[i]

Result = {}
for i in range(0, len(VectorList)):
    Result[FileList[i]] = MR.multifunction().CosSimilarity(list(VectorList[i].values()), list(searchVector.values()))

sortedArr = sorted(Result.items(), key=operator.itemgetter(1), reverse=True)
printList = []
printValue = []
restList = []

for i in sortedArr:
    if i[1] != 0:
        printList.append(i[0])
        printValue.append(i[1])
        print(i)
    else:
        restList.append(i[0])

plt.plot(printList, printValue)
plt.title("Similarity Result")
plt.xlabel("Text name")
plt.ylabel("Similarity")
plt.show()
print("유사도가 없는 파일: %s" % restList)