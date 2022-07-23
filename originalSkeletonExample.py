#importing libraries
import math
import csv

# variables for flightplan; the scale is what we're incrementing each waypoint by. The smaller the scale, the more precise the flightplan.
#gconstant = earth's grav field
#hmin = takeoff height
#take off & land command; verify that exact values match

#header for flightplan document
print("QGC WPL 110")
latitude = 39.91098980
longitude = -74.92385000

scale = .1
gconstant = 9.807
hmin = 10
wayPoint = 10
randombool = True
velocity = 0.00

#These columns represent each of the mission planner parameters for creating a flight profile
c1 = 0
c2 = 0
c3 = 3
c4 = 0
c5 = 0.00000000
c6 = velocity
c7 = 0.00000000
c8 = 0.00000000
c9 = latitude
c10 = longitude
c12 = 1

#this represents the 12 datapoints needed at each waypoint
num_rows = 1
num_col = 12

#x and y are parameters for the array that wiill store 12 datapoints for EACH waypoint
x = 0
y = 0

array = [[0 for x in range(num_col)] for y in range(num_rows)]

#looping through heights 10-30 generating velocity and time for each point; time not included in .txt file but can be used to generate flight profile
#we're putting loop into .txt extension
#delimiter is what separates the values; space instead of comma
#in zero gravity only for downwards freefall, does not need to accelerate upwards @ 0g
with open("./testfile.txt", "w+") as file:
    csv_writer = csv.writer(file, delimiter=' ')
    csv_writer.writerow(["QGC", "WPL", "110"])
    while (wayPoint <= 30):
        scale = scale + .1
        wayPoint = 10 + scale
        c11 = wayPoint
        velocity = math.sqrt(2 * gconstant * ((wayPoint - hmin)))
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

        x = x + 1

        y = y + 1
        c1 = c1 + 1
        time = .5 * (wayPoint - hmin) / velocity

        #print("The velocity at height " +str(wayPoint)+ "is "+str(velocity) +"m/s and the time is "+str(time)+"s")

        print(values_array)
        csv_writer.writerow(values_array)
"""

  For reference: TO READ CSV

  https://docs.python.org/3/library/csv.html

  with open('filename', 'r') as in_file:

    csv_reader = csv.reader(in_file, delimiter=' ')

    for row in csv_reader:  # row is an array containing elements in a row

      print(', '.join(row))

"""
