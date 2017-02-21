years = [10900, 2000, 2100]
print filter(lambda year:(year % 4 == 0 and year % 100 != 0) or (year % 400 == 0), years)
print [year for year in years if (year % 4 == 0 and year %  100 != 0) or (year % 400 == 0)]



filter(lambda year:(year % 4 == 0 and year % 100 != 0) or (year % 400 == 0), years)
[year for year in years if (year % 4 == 0 and year % 100 != 0) or (year % 400) == 0]