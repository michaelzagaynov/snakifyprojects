from math import floor
print("what number is the day?")
day = input()

answer = (((int(day)%7)-4)%7)
print(answer)
print("thursday is 4, friday is 5, saturday 6, sunday is 7, monday is 1, tueday is 2, ans wednesday is 3")