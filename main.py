import re
import sys
import random

reading_from_file = 'readfile.txt' if len(sys.argv) < 3 else sys.argv[1]
write_to_file = 'writefile.txt' if len(sys.argv) < 3 else sys.argv[2]
## using the quick sort algorithm
def quicksort(arr,left,right):
   if left >= right:
      return
   k = random.randint(left,right-1)
   pivot = arr[k][1]
   arr[k],arr[left] = arr[left],arr[k]
   l = left+1
   r=right-1
   while(l <=r ):
        while(l <=r and arr[l][1] <= pivot):
            l+=1
        while(l <=r and arr[r][1] > pivot):
            r-=1
        if(l < r):
            arr[l],arr[r] = arr[r],arr[l]
   arr[left],arr[r] = arr[r], arr[left]
   quicksort(arr,left,r)
   quicksort(arr,r+1,right)
    

        

WORD_RE = re.compile(r'\w+')
index = {}
with open(reading_from_file, encoding='utf-8') as fp:
    for line_no, line in enumerate(fp,1):
        for match in WORD_RE.finditer(line):
            word=match.group()
            column_no = match.start()+1
            # print(word, column_no)
            location = (line_no,column_no)
            # print(location)
            index.setdefault(word,[]).append(location)

count = {word:len(items) for word, items in index.items()}
tupleArray = [(w,n) for w,n in count.items() ]





quicksort(tupleArray,0,len(tupleArray))

with open(write_to_file,'w') as f:
    for w in tupleArray:
        f.write(f'{w[0]} {w[1]}\n')
