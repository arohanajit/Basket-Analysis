'''
1. Convert CSV file into a list format
2. Update frequency of each item of item by making dictionary
3. Remove elements have less frequency than requiredand save them in a new dictionary
4. Make all combinations of the elements above the given fequency
5. Calculate support of each combination
6. Remove all combination having less support than required and save remaining in dictionary
7. Calculate confidence of the entire combination with respect to each element in the
combination.
8. Remove all the combinations having individual confidence lower than required confidence.
9. Print the remaining combinations.

'''


import numpy as np
import collections
import itertools
import csv
with open('basket analysis.csv','r') as csvfile:
    csv_reader=csv.reader(csvfile)
    item=collections.Counter()
    item_list=[]
    for row in csv_reader:
        #2. Update frequency of each item of item by making dictionary
        item.update(row)
        #1. Convert CSV file into a list format
        item_list.append(row)
    #Remove empty spaces
    del item['']
    item_freq=collections.OrderedDict(sorted(item.items()))
frequency=int(input("Enter Item Frequency: "))
support=int(input("Enter Support: "))
combination=int(input("Enter Combination: "))
confidence=int(input("Enter Confidence: "))
dict2={}
dict1={}
#3. Remove elements have less frequency than requiredand save them in a new dictionary
for i in item_freq:
    if(item_freq[i]>=frequency):
        dict1.update({i:item_freq[i]})
#4. Make all combinations of the elements above the given fequency
item=itertools.combinations(dict1.keys(),combination)
dict2.clear()
dict3={}
for i in item:
    dict2.update({(i):0})
#5. Calculate support of each combination
for i in dict2:
    for j in item_list:
        if(i[0] in j and i[1] in j):
            dict2[i]+=1
#6. Remove all combination having less support than required and
#save remaining in dictionary
for i in dict2:
    if(dict2[i]>=support):
        dict3[i]=dict2[i]
conf=[]
dict4={}
#7. Calculate confidence of the entire combination with respect to each element in the
#combination (individual confidence)
for i in dict3:
    for j in range(combination):
        conf.append((dict3[i]/dict1[i[j]])*100)
    #8. Remove all the combinations having individual confidence
    #lower than required confidence.
    if all(x>confidence for x in conf):
        dict4[i]=dict3[i]
    conf.clear()
#9. Print the remaining combinations.
print('------------------------------------------------------------------\n')
for i in range(combination):
    print("Item",i+1," "*25,end='')
print("Frequency")
for i in dict4:
    for j in i:
        space = " "*(30-len(str(j)))
        print(str(j)+space,end='')
    print("        ",dict4[i])

'''
ASSIGNMENT: Find out average confidence and print new results based on it
'''
