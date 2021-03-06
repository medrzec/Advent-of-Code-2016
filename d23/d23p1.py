puzle = open('puzzle')
puzzle = []

for i in puzle:
	puzzle.append(i.split('\n')[0])

def is_int(x):
	ints = '1,2,3,4,5,6,7,8,9,0'.split(',')
	for j in ints:
		if j == x:
			return True
	return False
def change(x):
	ret = ''
	if len(x.split(' ')) < 3:
		if x.split(' ')[0] == 'inc':
			ret = 'dec ' + " ".join(x.split(' ')[1:])
		else:
			ret = 'inc ' + " ".join(x.split(' ')[1:])
	else:
		if x.split(' ')[0] == 'jnz':
			ret = 'cpy ' + " ".join(x.split(' ')[1:])
		else:
			ret = 'jnz ' + " ".join(x.split(' ')[1:])
	return ret
import time
a = 7
b = 0
c = 0
d = 0
count = 0
while count < len(puzzle):
	i = puzzle[count]
	if i.split(' ')[0] == 'cpy':
		if i.split(' ')[2] == 'a':
			if is_int(i.split(' ')[1][0]):
				a = int(i.split(' ')[1])
			else:
				if i.split(' ')[1] == 'b':
					a = b
				elif i.split(' ')[1] == 'c':
					a = c
				else:
					a = d

		elif i.split(' ')[2] == 'b':
			if is_int(i.split(' ')[1][0]):
				b = int(i.split(' ')[1])
			else:
				if i.split(' ')[1] == 'a':
					b = a
				elif i.split(' ')[1] == 'c':
					b = c
				else:
					b = d
		elif i.split(' ')[2] == 'c':
			if is_int(i.split(' ')[1][0]):
				c = int(i.split(' ')[1])
			else:
				if i.split(' ')[1] == 'b':
					c = b
				elif i.split(' ')[1] == 'a':
					c = a
				else:
					c = d
		elif i.split(' ')[2] == 'd':
			if is_int(i.split(' ')[1][0]):
				d = int(i.split(' ')[1])
			else:
				if i.split(' ')[2] == 'b':
					d = b
				elif i.split(' ')[2] == 'c':
					d = c
				else:
					d = a
	elif i.split(' ')[0] == 'inc':
		if i.split(' ')[1] == 'a':
			a += 1
		elif i.split(' ')[1] == 'b':
			b += 1
		elif i.split(' ')[1] == 'c':
			c += 1
		else:
			d += 1

	elif i.split(' ')[0] == 'dec':
		if i.split(' ')[1] == 'a':
			a -= 1
		elif i.split(' ')[1] == 'b':
			b -= 1
		elif i.split(' ')[1] == 'c':
			c -= 1
		else:
			d -= 1
	elif i.split(' ')[0] == 'jnz':
		if (is_int(i.split(' ')[1][0]) and not is_int(i.split(' ')[2])):
			if i.split(' ')[2] == 'a':
				count += a
			elif i.split(' ')[2] == 'b':
				count += b
			elif i.split(' ')[2] == 'c':
				count += c
			elif i.split(' ')[2] == 'd':
				count += d
		elif (is_int(i.split(' ')[1][0]) and i.split(' ')[1] != '0'):
			count += int(i.split(' ')[2]) - 1
		elif (i.split(' ')[1] == 'a' and a != 0):
			count += int(i.split(' ')[2]) - 1
		elif (i.split(' ')[1] == 'b' and b != 0):
			count += int(i.split(' ')[2]) - 1
		elif (i.split(' ')[1] == 'c' and c != 0):
			count += int(i.split(' ')[2]) - 1
		elif (i.split(' ')[1] == 'd' and d != 0):
			count += int(i.split(' ')[2]) - 1
	else:
		if count + c < len(puzzle):
			puzzle[count + c] = change(puzzle[count + c])
	count += 1
print a