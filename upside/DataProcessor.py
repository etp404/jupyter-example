from datetime import datetime
import math
from numpy import genfromtxt

from upside.DFFRService import DFFRService

frequency_variations = genfromtxt('2015_2mo.csv', delimiter=',')

service = DFFRService()
isBetweenMidnightAndEight = False
continuouslyWorking = False

for record in frequency_variations:
    if (math.isnan(record[0])):
        continue

    datetime = datetime.utcfromtimestamp(record[0])

    if (datetime.hour == 0):
        isBetweenMidnightAndEight=True
        continuouslyWorking=True

    elif(isBetweenMidnightAndEight):
        continuouslyWorking &= service.regulate_load(record[1], 1)

    if (isBetweenMidnightAndEight & (datetime.hour == 9)):
        print("%s/%s: %r" % (datetime.day, datetime.month, continuouslyWorking))
        isBetweenMidnightAndEight=False


