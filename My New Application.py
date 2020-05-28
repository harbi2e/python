print ('Please insert your Salary: ')
Salary = int(input())
print ('Please insert your Dept: ')
Dept = int(input())
balance = Salary - Dept
print('Your new balance =')
print(balance)
print ('Saving amount is =')
Saving_amount = (balance * 0.11)
print(Saving_amount)
print('This is last balnce after cut saving amount')
New_balance = (balance - Saving_amount)
print(New_balance)
print('Please choise Y or N if you have new plan')
NewPlan = str(input())
if NewPlan == 'N':
    print('Thank you for use my applaiction')
if NewPlan == 'Y':
    print('Please insert pric for your new plan')
    Plan_pric = int(input())
    print('This is maximum amount to pay new plan')
    Maximum_amount = (New_balance * 0.16)
    print(Maximum_amount)
    if Maximum_amount >= Plan_pric :
        print('OK')
    else:
        print ('This is number of month for save amount to pay your new plan ')
        print(Plan_pric / Maximum_amount)
        print('Thank you for use my application')
