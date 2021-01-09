print("Welcome to the tip calculator.")
bill = float(input("What was the total bill? $"))
prec = float(input("What precent tip? 10, 12, 15? %"))/ 100 + 1
ppl = int(input("For how much people to split? "))
each_pay = "{:.2f}".format((bill / ppl) * prec)
print(f"Each one pay ${each_pay}")
