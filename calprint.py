import calendar


def print_month_calendar():
    year = int(input("Enter a year: "))
    month = int(input("Enter a month: "))
    print(calendar.month(year, month))


print_month_calendar()