class flightPlan:
#importing libraries 
  import math
  import numpy as np 

# variables for flightplan; the scale is what we're incrementing each waypoint by. The smaller the scale, the more precise the flightplan.
#gconstant = earth's grav field 
#hmin = takeoff height

scale=.1
gconstant = 9.807
hmin = 10
wayPoint = 10
randombool = True

#These columns represent each of the mission planner parameters for creating a flight profile 
c1 = 0
c2 = 0
c3 = 3
#c4
c5 = 0.00000000
c6 = velocity++
c7p1 = latitude++
c7 = 0.00000000
c8 = 0.00000000
c9 = latitude
c10 = longitude
c11 = wayPoint
c12 = 1

#this represents the 12 datapoints needed at each waypoint
num_rows = 1
num_col = 12
array = np.zeros((num_rows, num_col))

#x and y are parameters for the array that wiill store 12 datapoints for EACH waypoint 
x=0
y=0


#looping through heights 10-30 generating velocity and time for each point

while(wayPoint<=30): 
  scale=scale+.1
  wayPoint = 10+scale
  velocity = math.sqrt(2*gconstant*(wayPoint-hmin))
  c6 = velocity  
    array[0,0] = c1
    array[0,1] = c2
    array[0,2] = c3
    array[0,3] = c4
    array[0,4] = c5
    array[0,5] = c6
    array[0,6] = c7
    array[0,7] = c8
    array[0,8] = c9
    array[0,9] = c10
    array[0,10] = c11
    array[0,11] = c12

    if (c1==0):
      array[1,0] = 1
      array[2,0] = 0
      array[6,0] = c9

    array2[x,y] = array
    
    x=x+1
    y=y+1
    c=c+1
    c1=c1+1
    time = .5*(wayPoint-hmin)/velocity
    
    

  
  
  #print("The velocity at height " +str(wayPoint)+ "is "+str(velocity) +"m/s and the time is "+str(time)+"s")

  print(x)


#array1 = np.array([1,2,3])
  #allarrays = np.array([array1, array2, array3])

  
