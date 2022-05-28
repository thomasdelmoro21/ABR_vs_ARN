"""
@author Thomas Del Moro
"""

import random
from timeit import default_timer as timer
from tabulate import tabulate
import numpy as np
import matplotlib.pyplot as plt
from ABR import ABR
from ARN import ARN


def movingAverage(a):
    return np.convolve(a, np.ones(10) / 10, 'valid')


def getAverages(i1, i2, s1, s2, h1, h2, w1, w2):
    avgI1 = movingAverage(i1)
    avgI2 = movingAverage(i2)
    avgS1 = movingAverage(s1)
    avgS2 = movingAverage(s2)
    avgH1 = movingAverage(h1)
    avgH2 = movingAverage(h2)
    avgW1 = movingAverage(w1)
    avgW2 = movingAverage(w2)
    return avgI1, avgI2, avgS1, avgS2, avgH1, avgH2, avgW1, avgW2


def main():
    tree = ABR()
    treeRN = ARN()
    height = []
    heightRN = []
    searchTime = []
    searchRNTime = []
    insertTime = []
    insertRNTime = []

    for k in range(1, 100):
        n = k * 10000
        print("n =", n)
        keys = np.arange(n)
        np.random.shuffle(keys)

        # Test inserimento

        start = timer()
        for i in range(n):
            tree.insert(keys[i])
        end = timer()
        insertTime.append(round(end - start, 3))

        start = timer()
        for j in range(n):
            treeRN.insert(keys[j])
        end = timer()
        insertRNTime.append(round(end - start, 3))

        # Test altezza

        print("ABR heigh:", tree.treeHeight())
        height.append(tree.treeHeight())
        print("ARN heigh:", treeRN.treeHeight())
        heightRN.append(treeRN.treeHeight())

        # Test ricerca

        r = random.randint(1, n)
        start = timer()
        tree.treeSearch(r)
        end = timer()
        searchTime.append(end - start)

        start = timer()
        treeRN.treeSearch(r)
        end = timer()
        searchRNTime.append(end - start)

        tree = ABR()
        treeRN = ARN()

    # Test caso peggiore ABR

    worstCaseTime = []
    insertTime2 = []

    for k in range(1, 100):
        n = k * 100
        print('n = ', n)
        tree = ABR()
        keys = np.arange(n)
        start = timer()
        for i in range(n):
            tree.insert(keys[i])
        end = timer()
        worstCaseTime.append(round(end - start, 3))
        tree = ABR()

        np.random.shuffle(keys)
        start = timer()
        for i in range(n):
            tree.insert(keys[i])
        end = timer()
        insertTime2.append(round(end - start, 3))

    insertAvg, insertRNAvg, searchAvg, searchRNAvg, heightAvg, heightRNAvg, worstAvg, insert2Avg = \
        getAverages(insertTime, insertRNTime, searchTime, searchRNTime, height, heightRN, worstCaseTime, insertTime2)

    x = np.arange(1, len(insertAvg) + 1) * 10000

    plot1 = plt.figure(1)
    plt.plot(x, insertAvg)
    plt.plot(x, insertRNAvg)
    plt.xlabel("Numero di nodi")
    plt.ylabel("Tempo di inserimento")
    plt.legend(["ABR", "ARN"])
    plt.title("Grafico 1")

    plot2 = plt.figure(2)
    plt.plot(x, insertTime)
    plt.plot(x, insertRNTime)
    plt.xlabel("Numero di nodi")
    plt.ylabel("Tempo di ricerca")
    plt.legend(["ABR", "ARN"])
    plt.title("Grafico 2")

    plot3 = plt.figure(3)
    plt.plot(x, heightAvg)
    plt.plot(x, heightRNAvg)
    plt.xlabel("Numero di nodi")
    plt.ylabel("Altezza albero")
    plt.legend(["ABR", "ARN"])
    plt.title("Grafico 3")

    x2 = np.arange(1, len(worstAvg)+1) * 100
    plot4 = plt.figure(4)
    plt.plot(x2, insert2Avg)
    plt.plot(x2, worstAvg, color='r')
    plt.xlabel("Numero di nodi")
    plt.ylabel("Tempo di inserimento")
    plt.legend(["Caso medio", "Caso peggiore"])
    plt.title("Grafico 4")

    plt.show()

    insertResults = {"Numero di nodi": x, "Tempo di inserimento ABR": insertTime,
                     "Tempo di inserimento ARN": insertRNTime}
    print(tabulate(insertResults, headers="keys", tablefmt="latex"))

    searchResults = {"Numero di nodi": x, "Tempo di ricerca ABR": searchTime,
                     "Tempo di ricerca ARN": searchRNTime}
    print(tabulate(searchResults, headers="keys", tablefmt="latex"))

    heightResults = {"Numero di nodi": x, "Altezza ABR": height, "Altezza ARN": heightRN}
    print(tabulate(heightResults, headers="keys", tablefmt="latex"))

    worstCaseResults = {"Numero di nodi": x2, "Caso medio": insertTime2, "Caso peggiore": worstCaseTime}
    print(tabulate(worstCaseResults, headers="keys", tablefmt="latex"))


if __name__ == "__main__":
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
