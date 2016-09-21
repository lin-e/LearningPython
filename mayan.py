import math

day = float(input("What day is it? "))
month = float(input("What month is it? "))
year = float(input("What year is it? ")) + 3113
remaining_days = (year * 365.25) + ((month - 1) * 30) + day + 144
#float((round((year * 365.25) + ((month - 1) * 30) + day)))
print(str(remaining_days))
baktuns = int(math.floor(remaining_days / 144000))
remaining_days = float(remaining_days - (baktuns * 144000))
katuns = int(math.floor(remaining_days / 7200))
remaining_days = float(remaining_days - (katuns * 7200))
tuns = int(math.floor(remaining_days / 360))
remaining_days = float(remaining_days - (tuns * 360))
unials = int(math.floor(remaining_days / 20))
remaining_days = int(remaining_days - (unials * 20))
print(str(baktuns) + "-" + str(katuns) + "-" + str(tuns) + "-" + str(unials) + "-" + str(remaining_days))

#days in a kin = 1
#days in a unial = 20 = 20
#days in a tun = 20 * 18 = 360
#days in a katun = 20 * 18 * 20 = 7200
#days in a baktun = 20 * 18 * 20 * 20 = 144000
