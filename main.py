import requests
import json
import math
import time
import datetime

URL = 'https://2bqueue.info/queue'

response = requests.get(URL)
jsonData = json.loads(response.text)

regular = jsonData['regular']
prio = jsonData['prio']
total = jsonData['total']

print('Regular: ' + str(regular))
print('Prio: ' + str(prio))
print('Total: ' + str(total))

# Print current date and time
print("Time: " + str(datetime.datetime.now()))

# Print UNIX time
print("UNIX: " + str(time.time()))

def calculateWaitTime():
    averageWaitFor1stSpot = 4.3271
    averagePeoplePerSecond = 1.8534
    # calculate wait time for nth spot
    waitTime = (averageWaitFor1stSpot + (averagePeoplePerSecond * total)) - (averagePeoplePerSecond * regular)
    return waitTime

def simplifyWaitTime(waitTime):
    # only keep 2 decimal places
    return math.floor(waitTime * 100) / 100

def splitHourDecimalIntoHoursAndMins(hour):
    # split hour into hours and minutes
    hours = math.floor(hour)
    minutes = math.floor((hour - hours) * 60)
    return hours, minutes
waittime = splitHourDecimalIntoHoursAndMins(simplifyWaitTime(calculateWaitTime()))
print("Wait time: {0} hours and {1} minutes".format(waittime[0], waittime[1]))
