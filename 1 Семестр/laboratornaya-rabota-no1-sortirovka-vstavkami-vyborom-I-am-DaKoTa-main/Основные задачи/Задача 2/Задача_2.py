def Sort(a):
    indx[0]=1
    for i in range(1, n):
        temp = a[i]
        if -10**9 <= a[i] <= 10**9: # проверка числа, чтобы оно не превосходило по модулю 10**9
            j = i - 1
            while j >= 0 and temp < a[j]:
                a[j + 1] = a[j]
                j -= 1
            a[j + 1] = temp
            indx[i] = (j + 2)
        else:
            return 'Error'
    # Переводим из массивов в строки с отступом в виде пробела
    indx_w = ' '.join(map(str, indx))
    aint_w = ' '.join(map(str, aint))
    return (indx_w + '\n' + aint_w)
with open('input.txt','r') as f:
    n=int(f.readline())
    a=f.readline().split()
    aint = list(map(int, a))
indx=[0]*n
if (1 <= n <= 10**3): # проверка первого числа (кол-во чисел), чтобы оно не превосходило 10**3
    with open('output.txt', 'w') as f:
        f.write(Sort(aint))