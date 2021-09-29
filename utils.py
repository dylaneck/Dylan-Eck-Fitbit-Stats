import math

def read_data(filename):

    
    infile = open(filename, "r") 
#Opens file for reading
    
    lines = infile.readlines() 
#Assigns lines to the data and headers
    headers = [lines.pop(0)]
#Removes headers from lines and gives headers it's own variable
    infile.close()
#Closes file
    return lines, headers

def display_table(lines, headers):
    new_headers = []
    data = [] 
#Assigns new lists for the cleaned data and headers, couldn't figure out why headers stayed in the list
    for variable in headers:
        values = variable.split(",")
        new_headers.append(values)
#Seperates each value of headers and put them in a new list    
    for variable in lines:
        values = variable.split(",")
        data.append(values)
#Does the same with the data    
    for value in new_headers:
        print(value, end="\t")
    print()
#Prints out new list of headers
    for row in data:
        for value in row:
            print(value, end="\t\t")
        print()
#Prints out new list of data
    return data, new_headers

def get_column(new_headers, col_name, data):
    col_index = []
#creates col_index
    for i in range(len(data)):
#runs loop to fill in col_index
        if col_name == "Date":
            col_index.append(data[i][0])
        elif col_name == "Calories Burned":
           col_index.append(data[i][1])
        elif col_name == "Steps":
            col_index.append(data[i][2])
        elif col_name == "Distance":
            col_index.append(data[i][3])
        elif col_name == "Floors":
            col_index.append(data[i][4])
        elif col_name == "Minutes Sedentary":
            col_index.append(data[i][5])
        elif col_name == "Minutes Lightly Active":
            col_index.append(data[i][6])
        elif col_name == "Minutes Fairly Active":
            col_index.append(data[i][7])
        elif col_name == "Minutes Very Active":
            col_index.append(data[i][8])
        elif col_name == "Activity Calories":
            col_index.append(data[i][9])
#if statements fill in values based off of input from user
    print("Here is the list of values:", col_index)
    #Prints new 1D list
    return col_index
