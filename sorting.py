import time

def insertion(inpList):
    # Will try to write the Good ol' Insertion Sort code without searching on the internet
    i =0
    fulllength = len(inpList)

    while (i< fulllength-1):
        j = i+1
        while(j>0 and inpList[j]<inpList[j-1]):
            inpList[j],inpList[j-1] = inpList[j-1],inpList[j]
            j-=1
        i +=1
    return inpList

if __name__ == "__main__":
    input_list = [int(x) for x in input("Enter a space separated, non-empty, numerical sequence to sort:\n").split()]
    output_list = insertion(input_list)
    print("Here is the sorted list: ", *output_list)