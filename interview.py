def num_coins(cents):
	if cents == 0:
		return 0
	coin_val = [25, 10, 5, 1]
	for val in coin_val:
		quot = cents // val
		if quot > 0:
			return quot + num_coins(cents % val)
print(num_coins(31))
