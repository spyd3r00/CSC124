from timeit import default_timer as timer
ranNum = []
exeTime = []


start= timer()

f=open("time.txt", "a+")


file = open('10000.txt')
textfile= file.read()
values = textfile.split(",")

for i in values:
	ranNum.append(int(i))

def insertionSort(arr): 
  
    for i in range(1, len(arr)): 
  
        key = arr[i] 

        j = i-1
        while j >=0 and key < arr[j] : 
                arr[j+1] = arr[j] 
                j -= 1
        arr[j+1] = key
  

arr =ranNum

insertionSort(arr) 
print ("Sorted array is:") 
for i in range(len(arr)): 
    print (arr[i]) 

end = timer()
print("Time taken:", end-start)
timeResult = end-start

f.write(str(timeResult))
f.write(str(','))
   