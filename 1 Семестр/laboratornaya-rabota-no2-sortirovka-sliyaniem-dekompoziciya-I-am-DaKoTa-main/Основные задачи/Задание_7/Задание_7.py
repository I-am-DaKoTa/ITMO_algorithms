# Функция нахождения максимального подмассива
def maxSubarray(A):
    start, end, sum = 0, 0, 0
    tempstart, tempend, tempsum = 0, 0, 0
    minus=[-10**10]
    for i in range(n):
        # переменная minus необходима, если все числа в массиве отрицательные.
        # Если это так, то функция выдаст наибольшее отрицательное значение, то есть максимальный подмассив
        minus[0]=max(A[i],minus[0])

        if tempsum==0:
            tempstart=i
        tempsum += A[i]
        # Условие необходимое для нахождения максимальной суммы
        if sum < tempsum:
            sum=tempsum
            tempend=i

        # При отрицательной сумме мы заканчиваем с этим подмассивом и переходим к следующему
        if tempsum<0:
            tempsum=0
            if start<tempstart and end<tempend:
                start=tempstart
                end=tempend

    # sum==0 означает, что массив состоит из отрицательных чисел
    if sum==0:
        return minus
    else:
        return A[start:end+1]
with open('input.txt','r') as f:
	n = int(f.readline())
	A = [int(x) for x in f.readline().split(' ')]

if 1 <= n <= (2*10**4) and not(any([abs(x)>10**9 for x in A])):
	with open('output.txt','w') as f:
		f.write(' '.join(map(str,maxSubarray(A))))