items=[]

while True:
    item=input('Add Items (type "done" to place the order)  :')
    if item.lower() =='done':
        break
    items.append(item)
print('selected items : ', items)