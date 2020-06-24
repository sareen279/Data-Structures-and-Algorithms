#Convert the Roman numeral to Decimal format.

t = 'V'
dt = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
ans = 0
i = 0
while i < (len(t) - 1):
	if dt[t[i]] < dt[t[i + 1]]:
		ans += (dt[t[i + 1]] - dt[t[i]])
		i += 1
	else:
		ans += dt[t[i]]
	print(ans, i)
	i += 1
while i < len(t):
	ans += dt[t[i]]
	i += 1
print(ans)
