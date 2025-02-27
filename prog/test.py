def cost(freq, i, j):
	if j < i:	
		return 0
	if j == i:	 
		return freq[i]  
	fsum = Sum(freq, i, j) 
	Min = 111111111111111111000000
	for r in range(i, j + 1):
		cost1 = (cost(freq, i, r - 1) +
				cost(freq, r + 1, j)) 
		if cost1 < Min: 
			Min = cost1
	return Min + fsum
def Search(keys, freq, n): 
	return cost(freq, 0, n - 1)
def Sum(freq, i, j):
	s = 0
	for k in range(i, j + 1):
		s += freq[k] 
	return s
keys = [10, 20, 30] 
freq = [1, 1, 1] 
n = len(keys) 
print(Search(keys, freq, n))

