def is_leap(year):
    leap = False
    
    # Write your logic here
    if year % 400==0 or year % 100 != 0 and year %4 ==0:
        leap=True
    return leap

year = int(input())