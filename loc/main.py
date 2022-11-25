latitude1 = 47.20168089915109
longitude1 = 38.93606726189317

latitude2 = 47.203218079988375
longitude2 = 38.9337863042296

user_latitude = float(input("latitude :"))
user_longitude = float(input ("longitude :"))

if latitude2 > user_latitude > latitude1 and longitude2 < user_longitude < longitude1:
    print("все ништяк")
else:
    print("ты где мужик")