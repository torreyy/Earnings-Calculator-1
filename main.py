print("Your Earnings Calculator")

hourly = float(input("How much do you make per hour? "))

daily = float(input("How many hours do you work per day? "))

daily_earnings = hourly * daily

print("This is your daily earnings:", str(daily_earnings))

weekly_earnings = daily_earnings * 5

print("This is your weekly earnings: ", + daily_earnings * 5)

monthly_earnings = daily_earnings *5 /12

print("This is your monthly earnings: ", + weekly_earnings * 52 //12 )
yearly_earnings = monthly_earnings * 12

print("This is your yearly earnings: ", + weekly_earnings * 52)

print("Congratulations!")

