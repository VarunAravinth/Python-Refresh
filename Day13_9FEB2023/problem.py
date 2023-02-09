li = [1,2,3,4,5]
li2 = [6,7,8,9,10]

for item1,item2 in zip(li,li2):
    print(item1,'- ', item2)

for index,value in enumerate(li2):
    print(index,'- ', value)