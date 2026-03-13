def check_duplicates(arr):
    freq={}
    duplicates=[]
    for num in arr:
        if num in freq:
            freq[num]+=1
        else:
            freq[num]=1
    for num in freq:
        if freq[num]>1:
            duplicates.append(num)
    return duplicates
    
arr = list(map(int, input().split()))
print(check_duplicates(arr))
            
