data = input("Enter the data:")
m = len(data)
p = 0
'''
to find no of parity bits
2^p - p >= m+1
where p = no of parity bits
      m = length of the data
'''
for i in range(m):
    temp = 2**i - i
    if (temp >= m+1):
        p = i
        break
print("The length of the data",m,"and it has",p,"parity bits")
'''
positioning the parity bit and data bit
Example:
Data = 1010, then
Hamming code= PP1P010
place parity bit on 2^n position
'''
for i in range(p):
    pos = 2**i - 1
    data=data[:pos]+'P'+data[pos:]

print("The parity position of data is",data)

#Even parity generator
for i in range(p):
    count = 2**i
    start = count
    parity = 0
    while(start <= m+p):
        for j in range(start,start+count):
            if j-1< m+p and data[j-1] != 'P':
                parity ^= int(data[j-1])
        start += count+1
    data = data[:count-1]+str(parity)+data[count:]
print("The data is",data,"and data length is",(m+p))

