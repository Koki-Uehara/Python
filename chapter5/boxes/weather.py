from sources import daily, weekly

print("daily forecast : ", daily.forecat())
print("weekly forecast :")
for number, outlook in enumerate(weekly.forecat(), 1):
    print(number, outlook)