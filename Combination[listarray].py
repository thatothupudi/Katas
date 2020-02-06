def Combination():
    list1 = []
    list2 = []
    sequence1 = input("Enter your your sequence ").split(" ")
    list1 = sequence1
    
    sequence2 = input("Enter your your sequence ").split(" ")
    list2 = sequence2
    
    t = len(list1)
    store_list = []
    for s in range(t):
        store_list.append(list1[s])
        store_list.append(list2[s])
    print(store_list)
Combination() 