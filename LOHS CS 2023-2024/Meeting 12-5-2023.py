# EXAMPLE 1
n = int(input())
m = int(input())
adj = []
noun = []
for i in range(n):
	s = input()
	adj.append(s)
for i in range(m):
	s = input()
	noun.append(s)

for i in range(n):
	for j in range(m):
		print(f"{adj[i]} as {noun[j]}")

# EXAMPLE 2
n = int(input())
pepper = {
	"Poblano":1500,
	"Mirasol":6000,
	"Serrano":15500,
	"Cayenne":40000,
	"Thai":75000,
	"Habanero":125000

}
ans = 0
for i in range(n):
	name = input()
	ans = ans + pepper[name]

print(ans)

# EXAMPLE 3

n = int(input())
pairing = dict() # empty dict
s = input().split() # turns line 2 into list of strings
a = input().split() # turns line 3 into list of strings
good = 1 # assume at the start that string is good
for i in range(n):
	if s[i] in pairing:
		if pairing[s[i]] != a[i]: # doesnt satisfy condition 1
			good = 0
	elif s[i] == a[i]: # doesnt satisfy condition 2
		good = 0
	else: # create new key values so they are pairs
		pairing[s[i]] = a[i]
		pairing[a[i]] = s[i]

if good == 1:
	print("good")
else:
	print("bad")
