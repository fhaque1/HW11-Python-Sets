def union(a,b):
	return sorted([x for x in b if x not in a] + a)

def intersection(a,b):
	return sorted([x for x in b if x in a])
	
def set_difference(u,a):
	return sorted([x for x in u if x not in a])

def simmer_differ(a,b):
        return sorted([x for x in a if x not in b] + [x for x in b if x not in a])

def cartesian_product(a,b):
        return sorted([[x,y] for x in a for y in b])

print union([1,2,3],[2,3,4])
print intersection([1,2,3],[2,3,4])
print set_difference([1,2,3],[2,3,4])
print simmer_differ([1,2,3],[2,3,4])

print cartesian_product([1,2],["red","white"])
