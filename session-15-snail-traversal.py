def snail(matrix):
	out = []
	while len(matrix):
		out += matrix.pop(0)
		print(out)
		matrix = list(zip(*matrix))[::-1]
	return out


grid = [[1, 2, 3, 4],
		[5, 6, 7, 8],
		[9, 10,11,12],
		[13,14,15,16]]
print(snail(grid))