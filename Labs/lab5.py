import statistics

data = "100,30,53,67,85,87,50,45,51,72,64,69,59,17,22,23,44,25,16,67,85,87,50,45,51,72,59,14,50,55,32,23,24,25,37,28,39,30,33,35,40,34,41,43,94,95,59,98,99,44,45,47,48,49,53,61,63,69,75,77,60,83"

# Split the data string into a list of strings
grades = data.split(",")

# Cast the elements of grades into integers
grades = list(map(int, grades))

# Display the minimum value
minimum = min(grades)
print("Minimum value:", minimum)

# Display the maximum value
maximum = max(grades)
print("Maximum value:", maximum)

# Calculate and display the average to 2 decimal places
average = round(sum(grades) / len(grades), 2)
print("Average value:", average)

# Calculate and display the median value
median = statistics.median(grades)
print("Median value:", median)

# Display the statistics using string.format()
print("Statistics:")
print("Minimum: {}".format(minimum))
print("Maximum: {}".format(maximum))
print("Average: {:.2f}".format(average))
print("Median: {}".format(median))


#for loop instead of map
import statistics

data = "100,30,53,67,85,87,50,45,51,72,64,69,59,17,22,23,44,25,16,67,85,87,50,45,51,72,59,14,50,55,32,23,24,25,37,28,39,30,33,35,40,34,41,43,94,95,59,98,99,44,45,47,48,49,53,61,63,69,75,77,60,83"

# Split the data string into a list of strings
grades_str = data.split(",")

# Cast the elements of grades into integers
grades = []
for grade in grades_str:
    grades.append(int(grade))

# Display the minimum value
minimum = min(grades)
print("Minimum value:", minimum)

# Display the maximum value
maximum = max(grades)
print("Maximum value:", maximum)

# Calculate and display the average to 2 decimal places
average = round(sum(grades) / len(grades), 2)
print("Average value:", average)

# Calculate and display the median value
median = statistics.median(grades)
print("Median value:", median)

# Display the statistics using string.format()
print("Statistics:")
print("Minimum: {}".format(minimum))
print("Maximum: {}".format(maximum))
print("Average: {:.2f}".format(average))
print("Median: {}".format(median))

#list comprehension instead of map

import statistics

data = "100,30,53,67,85,87,50,45,51,72,64,69,59,17,22,23,44,25,16,67,85,87,50,45,51,72,59,14,50,55,32,23,24,25,37,28,39,30,33,35,40,34,41,43,94,95,59,98,99,44,45,47,48,49,53,61,63,69,75,77,60,83"

# Split the data string into a list of strings
grades = data.split(",")

# Cast the elements of grades into integers using list comprehension
grades = [int(grade) for grade in grades]

# Display the minimum value
minimum = min(grades)
print("Minimum value:", minimum)

# Display the maximum value
maximum = max(grades)
print("Maximum value:", maximum)

# Calculate and display the average to 2 decimal places
average = round(sum(grades) / len(grades), 2)
print("Average value:", average)

# Calculate and display the median value
median = statistics.median(grades)
print("Median value:", median)

# Display the statistics using string.format()
print("Statistics:")
print("Minimum: {}".format(minimum))
print("Maximum: {}".format(maximum))
print("Average: {:.2f}".format(average))
print("Median: {}".format(median))
