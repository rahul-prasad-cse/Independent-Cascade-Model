import sys
import random
import time

def mergeSort(alist,otherid):
    #print("Splitting ",alist)
    if len(alist)>1:
        mid = len(alist)//2
        lefthalf = alist[:mid]
        righthalf = alist[mid:]
        leftotherid=otherid[:mid]
        rightotherid=otherid[mid:]

        mergeSort(lefthalf,leftotherid)
        mergeSort(righthalf,rightotherid)

        i=0
        j=0
        k=0
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:
                alist[k]=lefthalf[i]
                otherid[k]=leftotherid[i]
                i=i+1
            else:
                alist[k]=righthalf[j]
                otherid[k]=rightotherid[j]
                j=j+1
            k=k+1

        while i < len(lefthalf):
            alist[k]=lefthalf[i]
            otherid[k]=leftotherid[i]
            i=i+1
            k=k+1

        while j < len(righthalf):
            alist[k]=righthalf[j]
            otherid[k]=rightotherid[j]
            j=j+1
            k=k+1
    #print("Merging ",alist)

def binarySearch(toSearch,inputArray,low,high):
    #while low<high:
    #    mid=(low+high)//2
    #    midval=inputArray[mid]
    #    if midval< toSearch:
    #        low=
    mid=(low+high)//2
    if low>high:
         return -1
    if inputArray[mid]==toSearch:
        return mid
    #print(inputArray[mid])
    if inputArray[mid]<toSearch:
        return binarySearch(toSearch,inputArray,mid+1,high)
    if inputArray[mid]>toSearch:
        return binarySearch(toSearch,inputArray,low,mid-1)

f=open("Cit-HepPh.txt",'r')
fromnode=[]
tonode=[[]]
active=[]
firsttime=1
i=0
for line in f:
	if line[0]=='#':
		continue
	line=line.split()
	#print(line)
	if firsttime==1:
		firsttime=0
		fromnode.append(int(line[0]))
		tonode[i].append(int(line[1]))
		active.append(0)
		continue
	if fromnode[len(fromnode)-1]==int(line[0]):
		tonode[i].append(int(line[1]))
	else:
		i+=1
		fromnode.append(int(line[0]))
		tonode.append([int(line[1])])
		active.append(0)
f.close()
#print(str(fromnode[0])+" "+str(tonode[0]))
#print(len(fromnode))
#print(len(tonode))
print("Graph created")
mergeSort(fromnode,tonode)
print("Sorted")
print("Enter the number of most influencing citations needed:")
k=int(input().strip())
maxInfluencedNodes=0
maxInfluencingnodes=[]
iters=100
for m in range(iters):
	currentNodes=[]
	currentNodesIndex=[]
	nextNodes=[]
	active=[]
	active=[0 for i in range(len(fromnode))]
	for i in range(k):
		index=random.randrange(0,len(fromnode))
		if index in currentNodesIndex:
			i-=1
			continue
		currentNodes.append(fromnode[index])
		currentNodesIndex.append(index)
		active[index]=1
	intialNodes=currentNodes
	#print(intialNodes)
	influecednodes=k
	#declared variable for number of nodes that have been influenced
	while len(currentNodes)!=0:
		for i in range(len(currentNodes)):
			for j in range(len(tonode[currentNodesIndex[i]])):
				for k in range(len(tonode[j])):
					nextNodes.append(tonode[j][k])
	#added trusted nodes from current nodes to the nextNodes
		currentNodesIndex=[]
		currentNodes=[]
		#print(nextNodes)
		#time.sleep(5)
		for i in range(len(nextNodes)):
			#print(nextNodes[i])
			index=binarySearch(nextNodes[i],fromnode,0,len(fromnode)-1)
			if index==-1:
				continue
			if active[index]==1:
				continue
			currentNodes.append(fromnode[index])
			currentNodesIndex.append(index)
			active[index]=1
		influecednodes+=len(currentNodes)
		#print("length of currentNodes: "+str(len(currentNodes)))
		#print("influencedNodes: "+str(influecednodes))
		nextNodes=[]
	if influecednodes>maxInfluencedNodes:
		maxInfluencedNodes=influecednodes
		maxInfluencingnodes=intialNodes
	print(m)
print("Number of nodes influenced: "+str(maxInfluencedNodes))
print("The influencing nodes are:")
for i in range(len(maxInfluencingnodes)):
	print(maxInfluencingnodes[i])