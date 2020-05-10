def StalinSort(L):
    newL = []
    for ele in L:
        if (newL==[]):
            newL.append(ele)
        else :
            if (ele > newL[len(newL)-1]):

                newL.append(ele)
    return newL

print(StalinSort([1,2,0,4,3]))