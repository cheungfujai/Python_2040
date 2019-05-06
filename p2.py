def recursive_pow(x, n):
    value = 1
    if n == 0:
    	return value
    elif n > 1:
    	value = value * (x * x) * recursive_pow(x, n - 2)
    	n -= 2
    elif n == 1:
    	value = value * x
    return value

record = int(raw_input('Input value: '))
Index = int(raw_input('Input Index: '))
print(recursive_pow(record, Index))