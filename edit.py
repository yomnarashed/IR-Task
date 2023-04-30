i= 0
j = 0
word1= "abcdef"
word2 = "azced"
h= len(word1)
w=len(word2)
m = [[0 for x in range(w+1)] for y in range(h+1)] 
operations = []
for i in range(h+1):
    m[i][0] = i
for j in range(w+1):
    m[0][j]= j
i =0 
j = 0
for i in range(1,h+1):
    for j in range(1,w+1):
        if word1[i-1] == word2[j-1]:
            m[i][j] =m[i-1][j-1]
        else:    
            m[i][j] = min(m[i-1][j-1] +1 , 
            m[i-1][j] +1 ,  m[i][j-1]+1)
print (m[h][w])
#find the operations starting from the end of matrix
i, j = h, w
while i > 0 or j > 0:
    #minus m value from 1 and compare it to check whether it's insert or delete
    if i > 0 and m[i][j] -1 == m[i - 1][j] :
        operations.append(("delete", word1[i - 1]))
        i -= 1
    elif j > 0 and m[i][j] -1== m[i][j - 1] :
        operations.append(("insert", word2[j - 1]))
        j -= 1
    else:
        #To not count similar letters as substitute operation
        if word1[i - 1] != word2[j - 1]:
            operations.append(("substitute", (word1[i - 1], word2[j - 1])))
        i -= 1
        j -= 1
operations.reverse()
print (operations)