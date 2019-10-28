"""Case-study #3 Investment report
The program allows to receive information for several years with a monthly capitalization
Developers:
Zhuravleva A. (65%), Anufrieva A. (58%)

"""

# Determine the language of the program.
language = input("Русский, English, Francais ").lower()

if language == "русский":
    import localru as lc
elif language == "english":
    import localen as lc
else:
    import localfr as lc

# Take input from user.
years = int(input(lc.TXT_CAPITAL_PERIOD))
initial_capital = float(input(lc.TXT_INIT_CAPITAL))
percent = float(input(lc.TXT_PERCENT))
investment_infusion = float(input(lc.TXT_INVEST_INFUSION))

print(" ")

for year in range(1, years + 1):
    print(year, lc.TXT_YEAR)
    print("------------------------------------------------------------------------------")
    print("|       |",lc.TXT_INVEST_BASIS,"|", lc.TXT_SUM_MONTH,"    |   ", lc.TXT_CAPITAL,"         |")
    print("|",lc.TXT_M,"|                      |                      |                      |")
    print("------------------------------------------------------------------------------")

# Calculate the values for the entered interval.

    month = 1

    while month <= 12:

        sum_per_month = initial_capital * (percent / 100)
        capital = initial_capital * (1 + percent / 100)
        initial_capital = investment_infusion + capital
        print("|", "%3d" % month, "  |", "%19s" % "{0:.2f}".format(capital - sum_per_month), " |",
              "%19s" % "{0:.2f}".format(sum_per_month), " |", "%19s" % "{0:.2f}".format(capital), " |")
        month += 1
    print(" ")


