per_cent = {
    'ТКБ': 5.6,
    'СКБ': 5.9,
    'ВТБ': 4.28,
    'СБЕР': 4.0
}
money = int(input("Введите сумму: "))
month = int(input("На какое количество месяцев Вы собираетесь открыть вклад? "))
tkb, skb, vtb, sber = per_cent['ТКБ'], per_cent['СКБ'], per_cent['ВТБ'], per_cent['СБЕР']
tkb_dep = round((money * (1 + tkb / 1200) ** month), 2)
skb_dep = round((money * (1 + skb / 1200) ** month), 2)
vtb_dep = round((money * (1 + vtb / 1200) ** month), 2)
sber_dep = round((money * (1 + sber / 1200) ** month), 2)
deposit = [tkb_dep, skb_dep, vtb_dep, sber_dep]
d = {
    'ТКБ': tkb_dep,
    'СКБ': skb_dep,
    'ВТБ': vtb_dep,
    'СБЕР': sber_dep
    }
print("Deposit = " + str(deposit))
max_val = max(d.values())
max_key = max(d, key=d.get)
print("Максимальная сумма, которую вы можете заработать — " + str(max_key) + " " + str(max_val))