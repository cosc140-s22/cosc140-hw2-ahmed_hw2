#######################################################
#
# COSC 140 Homework 2, "bus trip planner" problem
#
#######################################################


def getTimeString(H, M, S):
    '''
        Return a well formatted time string from the hours, minutes, and seconds
    '''
    timeStr = []

    if(H > 0):
        timeStr.append(F"{H:02d}h")
    if(M > 0):
        timeStr.append(F"{M:02d}m")
    if(S > 0):
        timeStr.append(F"{S}s")

    return ":".join(timeStr)


def getTime():
    '''
        Get a valid departure time from user
    '''
    while(True):
        time = input("What is the departure time of your bus? [HH:MM]: ").split(":")
        if(len(time) == 2 and all(t.isdigit() for t in time)):
            timeH, timeM = int(time[0]), int(time[1])
            if((0 <= timeH < 24) and (0 <= timeM < 60)):
                return (timeH, timeM)
            else:
                print("Time must be in proper 24hr format")
        else:
            print("Time must be provided in HH:MM format")


def getDist():
    '''
        Get a valid distance from user
    '''
    while(True):
        dist = input("How far do you need to travel (in km)? ")
        try:
            dist = float(dist)
            return dist
        except ValueError:
            print("Distance must be a valid number of kilometers")


def getstops():
    '''
        Get a valid number of stops from user
    '''
    while(True):
        stops = input("How many stops there are before getting to the destination? ")
        if(stops.isdigit()):
            return int(stops)
        else:
            print("stops must be a valid number:")


# Departure time
depH, depM = getTime()
dist, stops = getDist(), getstops()

# Travel time calculations
busSpeed = 40/3600  # Bus travels at 40 km/hr which is 0.01111111 km/s
stopTime = 30  # Each stop takes 30 seconds
timeTaken = (dist/busSpeed) + (stopTime * stops)  # The total time the ride takes in seconds

# Travel time breakdown
travelSec = timeTaken
travelH, travelSec = divmod(travelSec, 60*60)
travelM, travelSec = divmod(travelSec, 60)

# Arrival time
arrivalSec = (depH*3600) + (depM*60) + timeTaken
arrivalH, arrivalSec = divmod(arrivalSec, 60*60)
arrivalM, arrivalSec = divmod(arrivalSec, 60)

# Convert all hours and minutes to integers, and seconds to int if not fractional or float otherwise
travelH, travelM, travelSec, arrivalH, arrivalM, arrivalSec = [(int(x) if (round(x, 2) == int(x)) else float(x)) for x in [
    travelH, travelM, travelSec, arrivalH, arrivalM, arrivalSec]]


print(F"\nIf you leave at {getTimeString(depH,depM,0)} and travel {dist} km with {stops} stops, after traveling for {getTimeString(travelH,travelM,travelSec)}, you should arrive at {getTimeString(arrivalH,arrivalM,arrivalSec)}")
