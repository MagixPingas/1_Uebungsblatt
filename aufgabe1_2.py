'''Im Jahr 1999 hat Dagobert Duck 1000000 Dollar in ein Finanzprodukt mit festem Zinssatz
investiert. Die jährliche Verzinsung beträgt traumhafte 4,5%. Unter Berücksichtigung des
Zinseszins belief sich das Kapital im Jahre 2000 also auf 1000000·(1 + 0,045) Dollar, im
Jahre 2001 auf 1000000·(1+0,045)·(1+0,045) Dollar, etc. Berechnen Sie in der IDLE-Shell
den Wert des Kapital im Jahr 2024, also nach 25 Jahren Verzinsung.'''



amount = 1_000_000

years = 25




def zins(amount, years):
    zins = (1+0.045)
    return amount*(zins**years)


print(zins(amount, years))
