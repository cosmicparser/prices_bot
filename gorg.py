Ticket_prices = {
    "standard ticket": 10.20,
    "child ticket": 7.70,
    "Student Ticket": 8.20,
    "Senior Ticket": 6.80
}
St_ticket = float(input("How many standard ticket do you need?(please enter floateger)"))
St1_price = (St_ticket * Ticket_prices["standard ticket"])
Ch_ticket = float(input("How many child ticket do you need?(please enter floateger)"))
Ch1_price = (Ch_ticket * Ticket_prices["child ticket"])
Stu_ticket = float(input("How many student ticket do you need?(please enter floateger)"))
Stu1_price = (Stu_ticket * Ticket_prices["Student Ticket"])
Se_ticket = float(input("How many senior ticket do you need?(please enter floateger)"))
Se1_price = (Se_ticket * Ticket_prices["Senior Ticket"])
total_price = float((St1_price + Ch1_price + Stu1_price + Se1_price))
total_ticket =float((St_ticket + Ch_ticket +Stu_ticket + Se_ticket))
if total_ticket >= 2:
    print("your total is: £",total_price*0.8)
else:
    print("your total is: £",total_price)