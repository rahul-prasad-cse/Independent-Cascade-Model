import sys
import random

def mergeSort(alist,otherid,creation):
    #print("Splitting ",alist)
    if len(alist)>1:
        mid = len(alist)//2
        lefthalf = alist[:mid]
        righthalf = alist[mid:]
        leftotherid=otherid[:mid]
        rightotherid=otherid[mid:]
        leftcreation=creation[:mid]
        rightcreation=creation[mid:]

        mergeSort(lefthalf,leftotherid,leftcreation)
        mergeSort(righthalf,rightotherid,rightcreation)

        i=0
        j=0
        k=0
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:
                alist[k]=lefthalf[i]
                otherid[k]=leftotherid[i]
                creation[k]=leftcreation[i]
                i=i+1
            else:
                alist[k]=righthalf[j]
                otherid[k]=rightotherid[j]
                creation[k]=rightcreation[j]
                j=j+1
            k=k+1

        while i < len(lefthalf):
            alist[k]=lefthalf[i]
            alist[k]=lefthalf[i]
            otherid[k]=leftotherid[i]
            creation[k]=leftcreation[i]
            i=i+1
            k=k+1

        while j < len(righthalf):
            alist[k]=righthalf[j]
            otherid[k]=rightotherid[j]
            creation[k]=rightcreation[j]
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
    if inputArray[mid]<toSearch:
        return binarySearch(toSearch,inputArray,mid+1,high)
    if inputArray[mid]>toSearch:
        return binarySearch(toSearch,inputArray,low,mid-1)
f=open("user_rating.txt",'r')
my_id=[]
other_id=[[]]
creation=[]
count=0
active=[]
used=[]
#used is to keep track of which nodes have tried influencing others and wouldn't try again
#values represent same as active's values
#active 0 denotes inactive, 1 denotes active
for line in f:
    inputs=['','','','']
    i=0
    while line[i]!='\t':
        inputs[0]+=line[i]
        i+=1
    i+=1
    while line[i]!='\t':
        inputs[1]+=line[i]
        i+=1
    i+=1
    while line[i]!='\t':
        inputs[2]+=line[i]
        i+=1
    i+=1
    while line[i]!='\n':
        inputs[3]+=line[i]
        i+=1
    inputs[0]=int(inputs[0])
    inputs[1]=int(inputs[1])
    inputs[2]=int(inputs[2])
    if count==0:
        my_id.append(inputs[0])
        other_id.append([[inputs[1],inputs[2]]])
        creation.append(inputs[3])
        active.append(0)
        used.append(0)
        count+=1
        #j+=1
        continue
    if inputs[0] == my_id[count-1]:
        other_id[count].append([inputs[1],inputs[2]])
    else:
        my_id.append(inputs[0])
        other_id.append([[inputs[1],inputs[2]]])
        creation.append(inputs[3])
        active.append(0)
        used.append(0)
        count+=1
    #j+=1
del other_id[0]
f.close()
#graph created using adjacency list
print("Graph created")
mergeSort(my_id,other_id,creation)
print("Sorted")
print(len(my_id))
#print(len(other_id))
#print(len(creation))
x=binarySearch(my_id[0],my_id,0,len(my_id)-1)
print("Binary Search worst case handled")
print("Enter number of most influencing nodes required: ")
#k=int(input().strip())
k=10
maxInfluencedNodes=0
maxInfluencingnodes=[]
iters=1

for m in range(iters):
    used=[]
    active=[]
    used=[0 for l in range(len(my_id))]
    active=[0 for l in range(len(my_id))]
    currentNodes=[]
    currentNodesIndex=[]
    nextNodes=[]
    for i in range(k):
        index=random.randrange(0,len(my_id))
        if index in currentNodesIndex:
            i-=1
            continue
        currentNodes.append(my_id[index])
        currentNodesIndex.append(index)
        used[index]=1
        active[index]=1
    #print(currentNodesIndex)
    # selected k random nodes and stored their values and index in the named arrays
    intialNodes=currentNodes
    influecednodes=k
    #declared variable for number of nodes that have been influenced
    while len(currentNodes)!=0:
        for i in range(len(currentNodes)):
            for j in range(len(other_id[currentNodesIndex[i]])):
                if other_id[currentNodesIndex[i]][j][1]==1:
                    nextNodes.append(other_id[currentNodesIndex[i]][j][0])
        #added trusted nodes from current nodes to the nextNodes
        currentNodesIndex=[]
        currentNodes=[]
        for i in range(len(nextNodes)):
            #print(nextNodes[i])
            index=binarySearch(nextNodes[i],my_id,0,len(my_id)-1)
            if index==-1:
                continue
            if used[index]==1:
                continue
            currentNodes.append(my_id[index])
            currentNodesIndex.append(index)
            used[index]=1
            active[index]=1
        influecednodes+=len(currentNodes)
        #print("length of currentNodes: "+str(len(currentNodes)))
        #print("influencedNodes: "+str(influecednodes))
        nextNodes=[]
    print(m)
    if influecednodes>maxInfluencedNodes:
        maxInfluencedNodes=influecednodes
        maxInfluencingnodes=intialNodes
print("Number of nodes influenced: "+str(maxInfluencedNodes))
print("The influencing nodes are:")
for i in range(len(maxInfluencingnodes)):
    print(maxInfluencingnodes[i])