from switchs import *

def check(lineList):
    """
    It reads the file calend.txt and returns a list with the numbers of the lines that have the letter
    "i" in them
    
    :param lineList: list of the lines of the file
    :return: The list of the numbers of the processes that are in the calend.txt file.
    """
    contador=0
    lineList.append('FCFS')
    with open('calend.txt') as f:
        datafile = f.readlines()
    found = False  # This isn't really necessary
    for line in datafile:
        cont=0
        for char in line:
            if "i"==char:
                number=line[cont+6:cont+8:1].rstrip()
                lineList.append(int(number))
                cont=0
                break
            else:
                cont=cont+1
    return lineList

def process(numBlocks,processList,lineList):
    """
    This function reads the calend.txt file and creates a process for each line in the file
    
    :param numBlocks: The number of blocks in the memory
    :param processList: a list of all the processes
    :param lineList: This is a list of all the lines in the file
    :return: The number of blocks and the process list
    """
   
    with open('calend.txt') as f:
        datafile = f.readlines()
    numLine=1
    name=""
    for line in datafile:
        cont=0
        for char in line:
            if "c"==char:
                while numLine<=20:
                    if ("id:   "+str(numLine) in line)  :
                        name=switchName(numLine)
                        createProcess(numLine,int(line[cont+4:cont+6:1]),str(name),numBlocks,processList,lineList)
                        cont=0
                        numLine=0
                        break
                    else:
                        numLine=numLine+1

            else:
                cont=cont+1
    return numBlocks,processList


def createProcess(num,length,name,numBlocks,processList,lineList):
    """
    This function creates a process and adds it to the process list
    
    :param num: the number of the process
    :param length: the length of the capacity process
    :param name: the name of the process
    :param numBlocks: a list of strings that will be used to print the memory map
    :param processList: This is the list that will hold all the processes
    :param lineList: list of all the lines in the file
    """
    tempList=[]
    tempList.append(name)
    for i in range(len(lineList)):
        if i<=length-1:
            tempList.append(num)
        else:
            tempList.append(0)
    numBlocks.append(name+":"+ str(length))
    
    processList.append(tempList)




def duplicados(lst, i):
    """
    It takes a list and an index, and if the element at the index is repeated in the list, it deletes
    the first instance of the repeated element. 
    
    It then recursively calls itself with the same list and the next index. 
    
    If the element at the index is not repeated, it calls itself with the same list and the next index. 
    
    If the index is equal to the length of the list, it returns the list.
    
    :param lst: the list to be checked
    :param i: the index of the element we're currently looking at
    :return: The list without duplicates
    """
    
    if i==len(lst):
        return lst
    else:
    
        for j in range(len(lst)):
            
            if lst[i] == lst[j] and i!=j:
                del lst[j]
                return duplicados(lst,i)
        return duplicados(lst,i+1)