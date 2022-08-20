inpt = '442444424442444-'
identified = [int(i) if i.isdigit() else i for i in inpt]
print(identified)


num = "5555-4567-8912-3456"

start = 0
end = start + 4
eval_collector = []
print(eval_collector)
while end < len(num):

	for i in num[start:end]:

		digit_counter = num[start:end].count(i)
		print(digit_counter)
		if digit_counter == 4:
			eval_collector.append(True)  # a digit occurred 4 times and thus negated a validation
		else:
			eval_collector.append(False)
		start +=1
		end +=1

print(eval_collector)
if not any(eval_collector):
	print(True)
else:
	print(False)




