pay_per_hour = float(input("Enter pay per hour "))
total_hours = int(input("Enter total hours "))
if total_hours <= 40:
    pay = total_hours * pay_per_hour
else:
    over_time = total_hours - 40
    ot_pay = over_time * 1.5 * pay_per_hour
    normal_pay = 40 * pay_per_hour
    pay = ot_pay + normal_pay
print(pay)
