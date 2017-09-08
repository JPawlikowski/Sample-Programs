class minutesToHours():
    minutes = input("Enter number of minutes: ")

    hours = minutes // 60
    hoursRemain = minutes % 60
    hoursRemainDecimal = (hoursRemain * 100) // 60

    print minutes, "minutes is", hours,".",hoursRemainDecimal,"hours"


minutesToHours()
