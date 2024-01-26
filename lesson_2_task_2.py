def is_year_leap(year):
    if year % 4 != 0:
        return False
    else:
        return True
    
year = 1967
result = is_year_leap(year)
print (f"год {year}: {result}")