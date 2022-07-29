#importing libraries
import math
import csv

#header for flightplan document; DO NOT ALTER
print("QGC WPL 110")

'''
changeable variables for flightplan: these can be changed by the user
- increment: how far apart each waypoint is (smaller = more precise)
- lat/ long points
- oscillations: how man up & down motions drone makes
'''
increment = .1
latitude = 40.5184505
longitude = -74.4319010
oscillations = 1
'''
NON-changeable variables for flightplan: these can NOT be changed by the user
- scale:  a factor of the increment that is added to the array
- gconstant: earth's grav field
- hmin: takeoff height
- waypoint = altitude points
- totalHeightCompletion = shows how many times drone goes up and down (has a counter for parsing through array- totalHeightCompletioncounter)
- descendingWayPoint = used to calculate waypoint when drone is in descent (has a counter for parsing through array- adcounter)
- accelerationBreakPhase = acceleration during breaking phase to slow drone down from Og (has counter- breakPhaseCounter)
- accelerationRisingPhase = acceleration during rising phase to generate enough thrust for 0g 
- mean = mean value between min/ max height
- lowLevelRise = used to calculate P1 of rising phase 
- highLevelRise = used to calculate P2 of rising phase
'''
scale = 0
gconstant = 9.807
hmin = 10
hmax = 30
wayPoint = hmin
totalHeightCompletion = 2*oscillations
totalHeightCompletioncounter = 1
descendingWayPoint = hmax
adcounter = 1
accelerationBreakPhase = 8.966399132
breakPhaseCounter = hmin
startOfBreakPhase = 20.5
accelerationRisingPhase = 9.414719
mean = ((hmax+hmin)/2)
lowLevelRise = hmin+increment
highLevelRise = mean
totalNumPoints = (hmax-hmin)*increment*totalHeightCompletion

#These columns represent a few of the mission planner parameters for creating a flight profile
c1 = 0
c2 = 0
c3 = 3
c4 = 0
c5 = 0.00000000
c7 = 0.00000000
c8 = 0.00000000
c9 = latitude
c10 = longitude
c12 = 1

#this represents the 12 datapoints needed at each single waypoint
num_rows = 1
num_col = 12

#x and y are parameters for the array that wiill store 12 datapoints for EACH waypoint
#x = 0
#y = 0

#creation of array
array = [[0 for x in range(num_col)] for y in range(num_rows)]
#velocityGraphArray = [0 for x in range(totalNumPoints)] 

#looping through heights 10-30 generating velocity, time, and other needed quantities for each point; time not included in .txt file but can be used to generate flight profile
#we're putting loop into .txt extension
#delimiter is what separates the values; space instead of comma
#this is the CSV writer; used for converting into .txt
with open("./testfile.txt", "w+") as file:
    csv_writer = csv.writer(file, delimiter=' ')
    csv_writer.writerow(["QGC", "WPL", "110"])
    while(totalHeightCompletioncounter<=totalHeightCompletion):
      while (wayPoint <= hmax):
            scale = scale + increment
            wayPoint = hmin + scale 
            c11 = wayPoint
            #velocity of each waypoint in 0g phase
            velocity = -1*math.sqrt(2 * gconstant * ((wayPoint - hmin)))

            #this if-else statement and counter are used to tell if the drone is ascending or descending
            if adcounter%2 != 0:
              #basically: if drone is ascending, it is in the rising phase. First, it must speed up and generate thrust at mean height. Then, it must start slowing down to zero by the time it gets to max height.  
              if(wayPoint <= mean):
                velocity = math.sqrt(2 * accelerationRisingPhase * ((lowLevelRise-hmin)))
                lowLevelRise+=increment
                time = .5 * (wayPoint - hmin) / abs(velocity)
              else:
                velocity = 1*math.sqrt(2 * accelerationRisingPhase * ((highLevelRise - hmin)))
                highLevelRise-=increment  
            else:
              #the drone is now descending and is in the 0g phase
              c11 = descendingWayPoint
              descendingWayPoint = hmax - scale
              velocity = -1*math.sqrt(2 * gconstant * ((hmax-descendingWayPoint)))
              time = .5 * (hmax-descendingWayPoint) / abs(velocity)
              #if the descending wayPoint is in the breaking zone, the drone will start to deccelerate and slow down to a stop
              if descendingWayPoint<=startOfBreakPhase:
                velocity = -1*math.sqrt(2 * accelerationBreakPhase * ((startOfBreakPhase -breakPhaseCounter)))
                breakPhaseCounter+=increment
                time = .5 * (startOfBreakPhase-descendingWayPoint) / abs(velocity)
            
            c6 = velocity
            #establishing an array for each waypoint with all datavalues needed
            values_array = [c1, c2, c3, c4, c5, c6, c7, c8, c9, c10, c11, c12]
            #hardcoding value exceptions for takeoff; constant regardless of flightplan
            if (c1 == 0):
    
                values_array[1] = 1
                values_array[2] = 0
                values_array[6] = c9
    
            #if statement for each waypoint number for c4
            if (c1 == 1):
                values_array[3] = 22
    
            elif (c1 == 0 or c1 % 2 != 0):
                values_array[3] = 16
            else:
                values_array[3] = 178
    
            #updating overarching counter value
            c1 = c1 + 1    
            #printing array values in terminal and CSV file; importantly, not all array values are shown in console due to limit
            print(values_array)
            csv_writer.writerow(values_array)
            '''plt.plot(1, 2)
            plt.xlabel("Time")
            plt.ylabel("Velocity")
            plt.show
            '''
      #updating inner loop inputs so loop can start over
      scale = 0
      descendingWayPoint = hmax
      wayPoint = hmin
      adcounter+=1
      totalHeightCompletioncounter+=1
      breakPhaseCounter = hmin
      lowLevelRise = hmin+increment
      highLevelRise = mean
    """
    
      For reference: TO READ CSV
    
      https://docs.python.org/3/library/csv.html
    
      with open('filename', 'r') as in_file:
    
        csv_reader = csv.reader(in_file, delimiter=' ')
    
        for row in csv_reader:  # row is an array containing elements in a row
    
          print(', '.join(row))
    
    """
