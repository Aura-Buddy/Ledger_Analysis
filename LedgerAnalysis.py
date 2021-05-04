storeLine = []
TransactionNumber = []

import matplotlib
import matplotlib.pyplot as plt
import numpy as np

def main():
    data = open("Ledger.txt", "r")
    i = 0
    for line in data:
        storeLine.append(line)
        i+=1
    data.close()

    #print(eval(storeLine[0]))
    for i in range(len(eval(storeLine[0]))):
	TransactionNumber.append(eval((eval(storeLine[0]))[i]["Key"].split("SensorRead")[1]))
	#print(TransactionNumber[i])

    print("Number of Transactions: {}".format(len(TransactionNumber)))
    t = np.arange(0,len(eval(storeLine[0])))
    fig,ax = plt.subplots(1)
    ax.plot(t, TransactionNumber)
    plt.show()
    plt.close()

main()
