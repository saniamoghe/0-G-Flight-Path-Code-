import csv



values_array = []


with open('testfile.txt', 'r') as in_file:

  csv_reader = csv.reader(in_file, delimiter=' ')

  for row in csv_reader:  # row is an array containing elements in a row
    
    if row[0] == 'QGC':
      continue
    values_array.append(row)



print(values_array[30])


"""
  to cast a str to float, float(string)
"""
