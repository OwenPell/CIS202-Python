distance = float(input('What is the distance you are traveling in miles: '))
speedLimit = float(input('What is speed limit in mph: '))
speed = float(input('What is your average speed in mph: '))
time = distance/speedLimit
speedTime = distance/speed
minInHour = 60
timeInMin = time * minInHour
speedTimeInMin = speedTime * minInHour



if speed > speedLimit:
    timeSaved = timeInMin - speedTimeInMin
    if speed <= speedLimit + 5:
        print(f'You saved {timeSaved:.0f} minutes')
    else:
        print(f'You should\'t speed, but you saved {timeSaved:.0f} minutes')
elif speed < speedLimit:
    timeLost = speedTimeInMin - timeInMin
    print(f'You are overly cautious, so you took {timeLost:.0f} extra minutes')
else:
    print('You are a safe driver, but you have not saved any time')