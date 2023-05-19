# Функция слияния массивов
def merge(A, l, m, r):
	global inversion
	# Длины левого и правого массивов
	n1 = m - l + 1
	n2 = r - m

	L = [0] * n1
	R = [0] * n2

	# Перенос значений в левый и правый массивы
	for i in range(0, n1):
		L[i] = A[l + i]
	for j in range(0, n2):
		R[j] = A[m + 1 + j]


	# Подсчёт числа инверсий
	i=0 # Индекс числа в L[]
	j=0 # Индекс числа в R[]
	while i<len(L) and j<len(R):
		if L[i]>R[j]:
			j+=1
			inversion+=len(L)-i
		else:
			i+=1


	# Слияние двух массивов
	while len(L) != 0 or len(R) != 0:
		#Все элементы L[] скопированы в A[]
		if len(L) == 0:
			for l in range(l, len(R) + l):
				A[l] = R[0]
				R.pop(0)
			break
		# Все элементы R[] скопированы в A[]
		elif len(R) == 0:
			for l in range(l, len(L)+l):
				A[l] = L[0]
				L.pop(0)
			break

		# Если L[] и R[] непустые массивы
		if L[0] <= R[0]:
			A[l] = L[0]
			L.pop(0)
		elif L[0] > R[0]:
			A[l] = R[0]
			R.pop(0)
		l += 1

# Функция деления массива и нахождения
def mergeSort(A, l, r):
	if l < r:
		# Нахождение медианы массива
		m = (l+r)//2

		# Деление массива на левую и правую части
		mergeSort(A, l, m)
		mergeSort(A, m+1, r)

		# Вызов функции слияния после конца деления массива
		merge(A, l, m, r)

with open('input.txt','r') as f:
	n = int(f.readline())
	A = [int(x) for x in f.readline().split(' ')]
inversion=0
if 1 <= n <= (10**5) and not(any([abs(x)>10**9 for x in A])):
	mergeSort(A, 0, n - 1)
	with open('output.txt','w') as f:
		f.write(str(inversion))
