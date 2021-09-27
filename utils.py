import math

def load_lines_from_file(filename):

    
    infile = open(filename, "r") 

    
    lines = infile.readlines() 
    headers = [lines.pop(0)]
    #headers = lines.pop()
    infile.close()
    return lines, headers


def clean_lines(headers):
    for i in range(len(headers)):
        headers[i] = headers[i].strip()

def display_table(lines, headers):
    new_headers = []
    data = [] #going to be a 2d list
    for variable in headers:
        values = variable.split(",")
        new_headers.append(values)
    for variable in lines:
        values = variable.split(",")
        data.append(values)
    
    for row in new_headers:
        print(row, end=" \t")
    print()
    for row in data:
        for value in row:
            print(value, end="\t \t")
        print()
    return data, headers
