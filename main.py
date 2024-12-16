##Imports
# regex for advanced string matching
import re

## Global variables
# Unique values in the start of the string
uncounters = {}
# Unique values, end of the string
nocounters = {}
# Total items
totalcount = 0

## Main program
def Main(file):
    global totalcount
    # Skip first entry (header column)
    next(file)
    for line in file:
        # Get all letters at the start of the string
        un = re.search(r"^\D+", line).group()
        # Get the first number in the string
        no = re.search(r"\d{1}", line).group()
        # DEBUG: Print variables to verify
        print(f"un:{un}, no:{no}")
        # Process un
        AddToList(un, uncounters)
        # Process no
        AddToList(no, nocounters)
        # Raise counter
        totalcount += 1
    #Print results
    print("===")
    print(f'The are a total of {totalcount} applicants.')
    print("===")
    PrintList("Applicants per department", uncounters)
    PrintList("Applicants per seniority level", nocounters)

## Helper functions
def AddToList(value, list):
    if value is not None:
        if value not in list:
            list[value] = 1
        else:
            list[value] += 1

def PrintList(title, list):
    print(f"{title}:")
    for key, value in list.items():
        print(f"{key}:\t{value}")
    print("===")


## Intializer
if __name__ == "__main__":
    file = open('applicants.csv')
    Main(file)