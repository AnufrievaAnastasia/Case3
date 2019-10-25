#Developers:



years = int(input("Срок размещения капитала (лет): "))
initial_capital = float(input("Начальный капитал ($): "))
percent = float(input("Процентная ставка (%/мес.): "))
investment_infusion = float(input("Инвестиционные вливания ($/мес.): "))

for year in range(1, years + 1):
    print(year, "год")
    print("-------------------------------------------")
    print("|       |   основа   | сумма %  |         |")
    print("| месяц | инвестиций | за месяц | капитал |")
    print("-------------------------------------------")


    month = 1

    while month <= 12:

        sum_per_month = initial_capital * (percent / 100)
        capital = initial_capital * (1 + percent / 100)
        initial_capital = investment_infusion + capital
        print(month, capital - sum_per_month,  sum_per_month, capital)

        month += 1


