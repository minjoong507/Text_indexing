import math
import numpy as np

class multifunction:

    def __init__(self):
        pass

    def CosSimilarity(self, a, b):
        Set1 = np.array(a)
        Set2 = np.array(b)
        multi = sum(Set1 * Set2)
        x = math.sqrt(sum(Set1 * Set1))
        y = math.sqrt(sum(Set2 * Set2))
        if x * y != 0:
            result = multi / (x * y)

        else:
            result = 0

        return result

    def makeIdf(self, a, b):
        for i in a.keys():
            if a[i] != 0:
                a[i] = math.log(b / a[i], 2)

        return a

    def makeTfIdf(self, a, b):
        for i in a:
            for j in b.keys():
                if j in i.keys():
                    i[j] = b[j] * i[j]

        return a
