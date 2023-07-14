exit=False
while not exit:
    o=input('enter order of matrix-1 in the form m*p >>>').split('*')
    m,p=int(o[0]),int(o[1])
    l1=[]
    for i in range(m):
        l1.append([])
        for j in range(p):
            l1[i].append(0)
    for i in range(m):
        for j in range(p):
            l1[i][j]=int(input(f'[{i+1}][{j+1}]:'))
    o1=input('enter order of matrix-2 in the form p*n >>>').split('*')
    n=int(o1[1])
    l2=[]
    for i in range(p):
        l2.append([])
        for j in range(n):
            l2[i].append(0)
    for i in range(p):
        for j in range(n):
            l2[i][j]=int(input(f'[{i+1}][{j+1}]:'))

    l3=[]
    for i in range(m):
        l3.append([])
        for j in range(n):
            l3[i].append(0)

    for i in range(len(l1)):
        for j in range(len(l2[0])):
            for k in range(len(l2)):
                l3[i][j]+=l1[i][k]*l2[k][j]

    print('matix-1 X matrix-2:')
    for i in range(m):
        print(l3[i])
    if input('type "exit" to leave matrix mul\nelse type any button to proceed further')=='exit':
        exit=True
# last line added