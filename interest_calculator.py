print('How many year you will be saving?')
years = int(raw_input('Enter years: '))

print('How much is currently inn your account?')
principal = float(raw_input('Enter current amount in your account: '))

print('How much money do you plan on investin monthly?')
monthly_invest = float(raw_input('Enter amount: '))

print('What do you estimate will be yearly interest of this investment?')
monthly_invest = float(raw_input('Enter interest in decimal numbers (10% = 0.1): '))

print(' ')

monthly_invest - monthly_invest * 12
final_amount = 0; 

for i in range(0, years):
    if final_amount == 0:
        final_amount == principal

    final_amount = (final_amount + monthly_invest) * (1 + interest)

print('This is how much money you would save in your account after {} years: ').format(years) + str(final_amount)