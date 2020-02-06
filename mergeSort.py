from timeit import default_timer as timer
ranNum = []
start= timer()

f=open("time.txt", "a+")

file = open('100000.txt')
textfile= file.read()
values = textfile.split(",")

for i in values:
	ranNum.append(int(i))

def mergeSort(nlist):

    if len(nlist)>1:
        mid = len(nlist)//2
        lefthalf = nlist[:mid]
        righthalf = nlist[mid:]

        mergeSort(lefthalf)
        mergeSort(righthalf)
        i=j=k=0       
        while i < len(lefthalf) and j < len(righthalf):

            if lefthalf[i] < righthalf[j]:
                nlist[k]=lefthalf[i]
                i=i+1
            else:
                nlist[k]=righthalf[j]
                j=j+1
            k=k+1

        while i < len(lefthalf):
            nlist[k]=lefthalf[i]
            i=i+1
            k=k+1

        while j < len(righthalf):
            nlist[k]=righthalf[j]
            j=j+1
            k=k+1


nlist =ranNum


mergeSort(nlist)
print(nlist)
end = timer()
print("Time taken:", end-start)



timeResult = end-start
f.write(str(timeResult))
f.write(str(','))