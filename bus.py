#######################################################
#
# COSC 140 Homework 2, "bus trip planner" problem
#
#######################################################

def get_time():
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


def get_dist():
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


def get_stops():
    '''
        Get a valid number of stops from user
    '''
    while(True):
        stops = input("How many stops there are before getting to the destination? ")
        if(stops.isdigit()):
            return int(stops)
        else:
            print("stops must be a valid number:")


def get_time_breakdown(totalSec):
    '''
        Breakdown seconds into hours, minutes and seconds
    '''
    S = totalSec
    D, S = divmod(S, 3600*24)
    H, S = divmod(S, 60*60)
    M, S = divmod(S, 60)

    # Return all units as int if whole number or rounded float otherwise
    return [(int(t) if (round(t, 2) == int(t)) else round(float(t), 2)) for t in [D, H, M, S]]


def get_time_str(time):
    '''
        Return a properly formatted time string from the hours, minutes, and seconds
    '''
    D, H, M, S = time
    timeStr = []
    Day = F"Day {D+1} "
    if(H > 0):
        timeStr.append(F"{H:02d}h")
    if(M > 0):
        timeStr.append(F"{M:02d}m")
    if(S > 0):
        timeStr.append(F"{S}s")
    timeStr = ":".join(timeStr)
    return F"{Day if D>0 else ''}{timeStr}"


# Departure time
depH, depM = get_time()
dist, stops = get_dist(), get_stops()
departure_time = (0, depH, depM, 0)  # Day, Hour, Minute, Seconds

# Travel time calculations
busSpeed = 40/3600  # Bus travels at 40 km/hr which is 0.01111111 km/s
stopTime = 30  # Each stop takes 30 seconds
timeTaken = (dist/busSpeed) + (stopTime * stops)  # The total time the ride takes in seconds
travel_time = get_time_breakdown(timeTaken)

# Arrival time
arrival_time = get_time_breakdown((depH*3600) + (depM*60) + timeTaken)

print(F"\nIf you leave at {get_time_str(departure_time)} and travel {dist} km with {stops} stops, after traveling for {get_time_str(travel_time)}, you should arrive at {get_time_str(arrival_time)}")
