latitude1 = 47.201680
longitude1 = 38.936067

latitude2 = 47.203218
longitude2 = 38.933786

user_latitude = float(input("latitude :"))
user_longitude = float(input ("longitude :"))

if latitude2 > user_latitude > latitude1 and longitude2 < user_longitude < longitude1:
    print("все ништяк")
else:
    print("ты где мужик")