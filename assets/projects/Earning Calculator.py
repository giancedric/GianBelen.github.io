earningsgoal = int(input("How much money do you want to save a year?"))
months = earningsgoal/12
weeks = earningsgoal/52 
days = earningsgoal/365
print("To save up " + str(earningsgoal) + " dollars per year, you will need to save " + str(int(round(months,2))) + ' per month')
print("To save up " + str(earningsgoal) + " dollars per year, you will need to save " + str(int(round(weeks,2))) + ' per week')
print("To save up " + str(earningsgoal) + " dollars per year, you will need to save " + str(int(round(days,2))) + ' per day') 
