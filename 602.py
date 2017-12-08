from enum import Enum

daysofweek = Enum('sunday','monday','tuesday','wednesday','thursday','friday','saturday')
for day,name in enumerate(daysofweek):
    print day,name
favday = int(input('enter your favourite day: '))
print 'your favourite day of the week is', daysofweek[favday]
