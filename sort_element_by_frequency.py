def sortbyfrq(a):
    frequency = {}
    for ele in a:
        if ele in frequency:
            frequency[ele]['count'] += 1
        else:
            frequency[ele] = {'count':1}
        l=list(frequency.keys())
    for i in range(len(l)):
        for j in range(i + 1, len(l)):
            num1=l[i] 
            num2=l[j] 
            if frequency[num1]['count'] > frequency[num2]['count']:
                l[i], l[j] = l[j], l[i]
    p=[]
    for ele in l:
        count = frequency[ele]['count'] 
        for x in range(count):
            p.append(ele)
    return p   
 
print(sortbyfrq([5,5,5,1,1,1,3,3,2,7,7,7,7])) 