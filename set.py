def union(a,b):
	return sorted([x for x in b if x not in a] + a)

def intersection(a,b):
	return sorted([x for x in b if x in a])
	
def set_difference(u,a):
	return sorted([x for x in u if x not in a])
	
print union([1,2,3],[2,3,4])
print intersection([1,2,3],[2,3,4])
print set_difference([1,2,3],[2,3,4])
