import pandas as pd

def startFunc():
    print("The follow options can be done with the Dataset")
    print(' ' * 4, "1. Import file into DataFrame")
    print(' ' * 4, "2. Display the number of records and variables in the dataset")
    print(' ' * 4, "3. Display the last 3 rows")
    print(' ' * 4, "4. Identify and handle any missing or inconsistent data")
    print(' ' * 4, "5. Produce a numerical summary of all numbered attributes")
    print(' ' * 4, "6. Create a histogram of cholesterol")
    print(' ' * 4, "7. Create a bar chart showing age groups")
    print(' ' * 4, "8. Plot the distribution of \"risk_status\" by \"gender\" using a bar chart")
    print(' ' * 4, "9. Create a scatter plot to examine the relationship between \"systolic_bp\" and \"cholesterol\"")

    print(' ')
    num = 110
    while num not in range(0,10):
        print("To Exit Type 0")
        userInput = input("Which Question Would you like Answered?:")
        try:
            num = int(userInput)
        except ValueError:
            print("Please enter an interger number between 0 and 9")

    print(' ')
    whichQuestion(num)

# Question 1
def importFile():
    # Used to change the file be parsed
    # Added for future security reasons (Should be in a different file)
    fileName = "ClinicData" #str(input("What is the name of the file to be parsed?:"))
    fileType = "csv" #str(input("What is the type of file being parsed?:")).lower()

    # Import and convert to Dataframe
    dataImport = pd.read_csv(f"./{fileName}.{fileType}")
    global clinicData
    clinicData = pd.DataFrame(data=dataImport)

    print(' ')
    print("The Dataset placed in a Pandas.DataFrame")
    print(' ')
    print(clinicData)


# Question 2
def numberOfValues():
    #Clarify what they mean by variables in the Dataset
    numOfRecords = clinicData.shape[0]
    print(f"The number of rows is {numOfRecords}")
    print(' ')


# Question 3
def lastThreeRows():
    print("The Final Three Rows")
    print(' ')
    print(clinicData.tail(3))


def whichQuestion(num):
    if num == 1:
        importFile()
    elif num == 2:
        numberOfValues()
    elif num == 3:
        lastThreeRows()
    elif num == 4:
        handleData()
    elif num == 5:
        dataInsights()
    elif num == 6:
        cholesterolHistogram()
    elif num == 7:
        barAgeDistrobution()
    elif num == 8:
        riskGenderChart()
    elif num == 9:
        scatterPlot()
    else:
        exit()
    startFunc()

startFunc()
