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
