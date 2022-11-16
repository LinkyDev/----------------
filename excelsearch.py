import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df_excel = pd.read_excel(r'database.xlsx')
#print(df)
#print("\n", df.loc[[0, 1, 2],["name", "age"]])

#print(age, pquantity)
#plt.show()

def plotandshowArray():
    arr = [0,1,2,3,4,5,6,7]
    plt.plot(arr)
    plt.show()

#plotandshowArray()

#Return True if dictionary contains the value
def dicContV(dic, v):
    for i in dic:
        if dic[i] == v:
            #print(dic[i], "true")
            return True
        else:
            #print("false")
            return False

#Return True if dictionary contains the key
def dicContK(dic, k):
    for i in dic:
        if i == k:
            #print(i, "true")
            return True
    else:
        #print("false")
        return False


#test

#Add multiple values when keys are double, returns dictionary
def addMultiple(df, k1, k2):
    df_age = df.loc[:, k1]
    df_pq = df.loc[:, k2]
    tempDict = {}

    for i in df.index:
        if dicContK(tempDict, df_age[i]) == False:
            tempDict[df_age[i]] = df_pq[i]
            #print(tempDict)
        else:
            tempDict[df_age[i]] = tempDict[df_age[i]] + df_pq[i]
            #print(tempDict)
    
    return tempDict


#Sort a dictionary by value (Low to High)
def sortDictValue(dic):
    sorted_dic = list(dic.values())
    sorted_dic.sort()

    new_dic = {}
    for i in sorted_dic:
        for j in dic:
            if i == dic[j]:
               new_dic[j] = i
    
    #print(new_dic)
    return new_dic

#Get the age that purchases the most - k1 must be Age, k2 value to be checked
def getBestAge(df, k1, k2):
    dic = addMultiple(df, k1, k2)
    dic = sortDictValue(dic)
    return dic.popitem()[0]


tempDict = {23:2,80:5,96:4}

#dicContV(tempDict, 48)
#dicContK(tempDict, 80)
#addMultiple(df_excel, "age", "purchase quantity")
#sortDictValue(tempDict)
print("The best purchasing age is: ", getBestAge(df_excel, "age", "purchase quantity"))

#print(tempDict)
#tempDict[23] = tempDict[23] + 20
#print(tempDict)