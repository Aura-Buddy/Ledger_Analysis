import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import time

storeLine = []
dataEntry = []
dataEntry1 = []
datEntry2 = []
ValidationTime = []
CommittingTime = []
CommitBlockandPrivateData = []
CommitBlockandPrivateDataTime = []
CommitStateData = []
CommitStateTime = []
BlockedTransactions = []
storeLineTime = []
Day = []
Month = []
Date = []
Time = []
Zone = []
Year = []
dataEntry1 = []
TimeEntry = []
Hours = []
HoursElements = []
Minutes = []
MinutesElements = []
Seconds = []
SecondsElements = []
TimeInSeconds = []
TimeDifference = []

def main():
    i = 0
    ValidationSum = 0
    TimeSum = 0
    BlockedTransactionsSum = 0
    CommittingTimeSum = 0
    CommitStateTimeSum = 0
    CommitBlockandPrivateDataSum = 0

    data = open("peerLog.txt", "r")
    for line in data:
        storeLine.append(line)

    data.close()

    #looking for Validation Time
    for i in range(len(storeLine)):
        dataEntry.append(storeLine[i].split("] in "))
        if len(dataEntry[i]) == 2:
            ValidationTime.append(eval(dataEntry[i][1].split("ms\n")[0]))
            #time is in milliseconds

    #Finding average validation time
    for i in range(len(ValidationTime)):
        ValidationSum = ValidationSum + ValidationTime[i]

    ValidationAverage = ValidationSum/len(ValidationTime)
    print("Average Validation Time: {} millisecond(s)").format(ValidationAverage)

    #Looking for number of transactions in each block
    for i in range(len(storeLine)):
        dataEntry1.append(storeLine[i].split("] with "))
        if len(dataEntry1[i]) == 2:
            BlockedTransactions.append(eval(dataEntry1[i][1].split(" transaction(s) ")[0]))

    #Finding average number of transactions in each block
    for i in range(len(BlockedTransactions)):
        BlockedTransactionsSum = BlockedTransactionsSum + BlockedTransactions[i]

    BlockedTransactionAverage = BlockedTransactionsSum/len(BlockedTransactions)
    print("Average Number of Transactions in a Block: {} transactions".format(BlockedTransactionAverage))

    #Looking for time to commit block to ledger, overall
    for i in range(len(storeLine)):
          if len(dataEntry1[i]) == 2:
            CommittingTime.append(eval(dataEntry1[i][1].split("transaction(s) in")[1].split("ms (")[0]))

    #Finding average time to commit block, overall
    for i in range(len(CommittingTime)):
          CommittingTimeSum = CommittingTimeSum + CommittingTime[i]

    CommittingTimeAverage = CommittingTimeSum/len(CommittingTime)
    print("Average Overall Committing Time: {} millisecond(s)".format(CommittingTimeAverage))

    #Looking for time to commit block and private data
    for i in range(len(storeLine)):
        CommitBlockandPrivateData.append(storeLine[i].split("block_and_pvtdata_commit="))
        if len(CommitBlockandPrivateData[i]) == 2:
            CommitBlockandPrivateDataTime.append(eval((CommitBlockandPrivateData[i][1].split("ms"))[0]))

    #Finding average time to commit block and private data
    for i in range(len(CommitBlockandPrivateDataTime)):
        CommitBlockandPrivateDataSum = CommitBlockandPrivateDataSum + CommitBlockandPrivateDataTime[i]

    CommitBlockandPrivateDataAverage = CommitBlockandPrivateDataSum/len(CommitBlockandPrivateDataTime)
    print("Average Time to Commit Block and Private Data: {} ms".format(CommitBlockandPrivateDataAverage))

    #Looking for time to commit state
    for i in range(len(storeLine)):
        CommitStateData.append(storeLine[i].split("state_commit="))
        if len(CommitStateData[i]) == 2:
            CommitStateTime.append(eval((CommitStateData[i][1].split("ms"))[0]))

    #Finding average time to commit a state
    for i in range(len(CommitStateTime)):
        CommitStateTimeSum = CommitStateTimeSum + CommitStateTime[i]

    CommitStateAverage = CommitStateTimeSum/len(CommitStateTime)
    print("Average Time to Commit State Data: {} ms".format(CommitStateAverage))

    #t = np.arange(0,len(TimeDifference),1)
    Vt = np.arange(0,len(ValidationTime),1)
    BTt = np.arange(0,len(BlockedTransactions),1)
    Ct = np.arange(0,len(CommittingTime), 1)
    BPt = np.arange(0,len(CommitBlockandPrivateDataTime),1)
    CSt = np.arange(0,len(CommitStateTime),1)
    fig,ax = plt.subplots(2,2)
    ax[0][0].plot(Vt,ValidationTime)
    ax[0][0].set_title("Validation Time during 1000 Transactions")
    ax[0][0].set(ylabel = "Time (ms)")
    #ax[1][0].plot(t,TimeDifference)
    #ax[1][0].set_title("Time Difference between each Transaction")
    #ax[1][0].set(ylabel="Time (s)")
    ax[0][1].plot(BTt, BlockedTransactions)
    ax[0][1].set_title("Transactions per Block")
    ax[0][1].set(xlabel="Number of Transactions", ylabel="Time (ms)")
    ax[1][1].plot(Ct,CommittingTime, label="overall")
    ax[1][1].set_title("Time to Commit Block")
    ax[1][1].set(ylabel="Time (ms)")
    ax[1][1].plot(BPt, CommitBlockandPrivateDataTime, label="block and private data")
    ax[1][1].plot(CSt, CommitStateTime, label = "state")
    
    plt.legend(bbox_to_anchor=(1.05, 1), loc='center', borderaxespad=0.)
    plt.show()
    time.sleep(10)
    plt.close()


main()
