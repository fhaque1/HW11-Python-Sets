def union(a,b):
	return sorted([x for x in b if x not in a] + a)

def intersection(a,b):
	pass
	
def set_difference(a,b):
	pass

print union([1,2,4,6],[1,2,3,4,5])