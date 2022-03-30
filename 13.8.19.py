need_tickets = int(input('Введите количество билетов: '))
ticket_price  = 0

for ticket in range(need_tickets):
    age = int(input('Введите возраст участника конференции: '))
    if age < 18:
        ticket_price = ticket_price
    elif 18 <= age <= 25:
        ticket_price += 990
    else:
        ticket_price += 1390

if need_tickets >= 3:
    print('Стоимость Ваших билетов = ', ticket_price * 0.9)
else:
    print('Стоимость Ваших билетов = ',ticket_price, )