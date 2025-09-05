import random 
daysOfWeek = ["Sun","Mon","Tue","Wed","Thur","Fri","Sat"]
seasons = ["spring","summer","autumn","winter"]

watered_days = []


def regWaterUsage():
    # 30 minutes to water a lawn
    time = 20
    # 12 gallons per minute usualy 
    gallons = 12

    water = time * gallons
    return water

def rainChance(season):
    winter = 0.24
    spring = 0.30
    summer = 0.05
    fall = 0.23
    season = season.lower()
    if season == "winter":
        return winter
    elif season == "spring":
        return spring
    elif season == "summer":
        return summer
    elif season == "fall":
        return fall
    else :
        return none

def randomSeason(seasons):
    return(random.choice(seasons))

def weekWaterUse():
    dayUse = regWaterUsage()

    weekWater = dayUse * 3 

    return weekWater


def dayIntro(day):
    print("--------------------------------------------")
    print("--Welcome To Your Irrigation System--")

    if len(watered_days) == 3:
        print("--------------------------------------------")
        print("Your water has been irrigated for this week!")

    if watered_days != []:
        print("--------------------------------------------")
        print("Days the lawn was watered: ")
        print(watered_days)
    print("--------------------------------------------")

    print(f"Today is {day}.")
    print(f"We are currently in the season of {season.upper()}")
    print("--------------------------------------------")
    if len(watered_days) < 3 :
        print(f"Projected water usage for the day: ")
        print(str(regWaterUsage()) + " galloons ")
        print("--------------------------------------------")

def waterCounter(watered):
    boo = watered
    maxWater = 0

    if boo < 3:
        waterS = input("Do you want to turn sprinklers on today: (Yes/No)").lower()
        if maxWater >= 720:
            return boo
        if waterS == "yes":
            watered_days.append(day)
            maxWater += regWaterUsage()
            boo += 1
    return boo

def seasonProgress(season,seasonDayCount,seasons):
    seasonNumber = 5
    if season == "spring":
        seasonNumber = 0
    elif season == "summer":
        seasonNumber = 1
    elif season == "autumn":
        seasonNumber = 2
    elif season == "winter":
        seasonNumber = 3
    else:
        seasonNumber = 0
    
    if seasonDayCount >= 10:
        season = seasons[(seasonNumber + 1) % len(seasons)]
        seasonDayCount = 0
    return season,seasonDayCount




if __name__ == "__main__":
    seasonDayCount = 0
    dayCount = 0
    day = daysOfWeek[0]
    season = randomSeason(seasons)
    watered = 0

    ###create a loop to run the app 
    while True:
        season, seasonDayCount = seasonProgress(season,seasonDayCount,seasons)
        dayIntro(day)
        watered = waterCounter(watered)
        dayCount += 1 
        if dayCount % 6 == 0 :
            day = daysOfWeek[0]
            dayCount = 0
        day = daysOfWeek[0+dayCount]

        
        stop = input("Do u wanna stop?(Yes/No)").lower()
        if stop == "yes":
            break
        else:
            seasonDayCount += 5

