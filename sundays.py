from datetime import date


def number_of_sundays_on_first_of_month():
    sundays = 0
    for year in range(1901, 2001):
        for month in range(1, 13):
            if date(year, month, 1).weekday() == 6:
                sundays += 1
    return sundays


print("There were %d Sundays on the first of the month in the 20th century." % number_of_sundays_on_first_of_month())
