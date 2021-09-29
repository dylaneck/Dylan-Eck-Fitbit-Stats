###########################
#Dylan Eck
#CPSC 222, Fall 2021
#Data Assignment #2
#I did not attempt the bonus
#This program reads in, cleans, and then calculates stats for fitbit data
#############################

import math
from utils import  display_table, get_column, read_data


lines, headers = read_data("Fitbit.csv")
#calls function that reads in data

data, new_headers = display_table(lines, headers)
#Calls function that prints out more organized data table

print("Enter the name of a column: ")
col_name =  input()
#Prompts user for header to use for next function

col_index = get_column(headers, col_name, data)
#Calls function that creates 1d list based off of selected column

for i in range(len(col_index)):
        col_index[i] = float(col_index[i])
#Turns all values in list into float


list_sorting = col_index.copy()
#Copies list so it can be sorted for median
print("Number of values in the list: " + str(len(col_index)))
#Prints number of values in the list

mean_list = (sum(col_index))/int(len(col_index))
#Calculates the mean
mean = round(mean_list, 2)
#round smean to 2 decimals
print("Mean of the list: ", str(mean))
#Prints mean


total_variation = 0
i = 0
while i < len(col_index):
   variation = col_index[i] - mean
   variation = pow(variation, 2)
   total_variation += variation
   i += 1
#Runs a loop to find the sum of all of the variances
length = len(col_index)  
#Finds length of list
mean_variation = total_variation / length
#Finds mean variation
standard_deviation = pow(mean_variation, 1/2)
#Finds standard deviation
standard_deviation = round(standard_deviation, 2)
#Rounds to 2 decimal places
print("Standard Deviation: " + str(standard_deviation))
#Prints SD


mid_num = (len(list_sorting)) / 2
#Finds middle number
list_sorting.sort()
#Sorts list
print("The median of the list is: " + str(list_sorting[int(mid_num)]))
#prints result


min = min(col_index)
print("Minimum number: " + str(min))
#finds and prints min


max = max(col_index)
print("Maximum number: " + str(max))
#finds and prints max