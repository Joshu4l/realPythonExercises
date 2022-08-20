

num = "5123 - 3567 - 8912 - 3456"
for i in num:
	if not i.isdigit():
		num = num.replace(i,"")

print(num)
