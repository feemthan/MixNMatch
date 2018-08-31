import difflib
import random
from copy import deepcopy
import itertools


dict={"2":["A","B","C"],
      "3":["D","E","F"],
      "4":["G","H","I"],
      "5":["J","K","L"],
      "6":["M","N","O"],
      "7":["P","Q","R","S"],
      "8":["T","U","V"],
      "9":["W","X","Y","Z"]}

vow_dict={"2":"A",
          "3":"E",
          "4":"I",
          "6":"O",
          "8":"U"}

conso_dict={"2":["B","C"],
           "3":["D","F"],
           "4":["G","H"],
           "5":["J","K","L"],
           "6":["M","N"],
           "7":["P","Q","R","S"],
           "8":["T","V"],
           "9":["W","X","Y","Z"]}

def find_dupes(x):
    if x[0]==x[1]:
        return x[0]
    elif x[1]==x[2]:
        return x[1]
    elif x[2]==x[3]:
        return x[2]

def best_match(x):
    best_match=[]
    x=list(x)
    while x:
        a=x.pop()
        try:
            if (a in vow_dict.keys()) & (vow_dict[a] not in best_match):
                best_match.append(vow_dict[a])
            elif (a in vow_dict.keys())& (vow_dict[a] in best_match):
                test=deepcopy(dict)[a]
                test.remove(vow_dict[a])
                test1=test[0]
                if test1 not in best_match:
                    best_match.append(test1)
                else:
                    best_match.append(test[1])
        except:
            best_match.append(dict[a][random.randint(0,len(dict[a])-1)])
    if (best_match[0] not in vow_dict.values())&(best_match[1] not in vow_dict.values())&(best_match[2] not in vow_dict.values()):
            best_match=None
            return(best_match)
    return("".join(sorted(best_match, key=str)))

def check_vow_num(x):
    x=list(x)
    test=[]
    while x:
        a=x.pop()
        if a in vow_dict.keys():
            test.append(vow_dict[a])
    return list(set(test))

def matches(x):
    if len(check_vow_num(x))==0:
        return(None)
    elif len(check_vow_num(x))==1:
        test=best_match(x)
        conso=list(set(list(test)) - set(vow_dict.values()))
        final=list(map("".join, itertools.permutations(test)))[1:]
    elif len(check_vow_num(x))==2:
        dupe=find_dupes(x)
        test=check_vow_num(x)
        consolist=deepcopy(conso_dict[str(dupe)])
        final=[]
        for i in range(0,len(consolist)):
            b=consolist[i]
            test.append(str(b))
            final.append((map("".join,itertools.permutations(test))[1:]))
            test.pop()
        final1=final[0]
        final2=final[1]
        final=list(set(final1+final2))
    elif len(check_vow_num(x))==3:
        test=best_match(x)
        final=list(map("".join,itertools.permutations(test)))[1:]
    return final


z = 'ABCDEFGHIJKLMOPQRSTUVWXYZ'
z1 = [''.join(i) for i in itertools.permutations(z, 3)]

final=[]
finallist=[]
for i in range(0,len(z1)):
    a=z1[i][0]
    b=z1[i][1]
    c=z1[i][2]
    temp=[]
    for j in range(2,10):
        if a in dict[str(j)]:
            temp.append(str(j))
    for j in range(2,10):
        if b in dict[str(j)]:
            temp.append(str(j))
    for j in range(2,10):
        if c in dict[str(j)]:
            temp.append(str(j))
    final="".join(temp)
    if final not in finallist:
        finallist.append(final)

dict_final={}
for i in range(0,len(z1)):
    a=z1[i][0]
    b=z1[i][1]
    c=z1[i][2]
    temp=[]
    for j in range(2,10):
        if a in dict[str(j)]:
            temp.append(str(j))
    for j in range(2,10):
        if b in dict[str(j)]:
            temp.append(str(j))
    for j in range(2,10):
        if c in dict[str(j)]:
            temp.append(str(j))
    final="".join(temp)
    if final in dict_final.keys():
        dict_final[str(final)].append(str(z1[i]))
    else:
        dict_final[final]=[str(z1[i])]


print("Best Match for 222 is : ")
print(best_match("222"))
print("Matchs for 222 are : ")
print(matches("222"))

print("Best Match for 223 is :")
print(best_match("223"))
print("Matchs for 232 are : ")
print(matches("223"))

print("Best Match for 777 is :")
print(best_match("777"))
print("Matchs for 777 are :")
print(matches("777"))

