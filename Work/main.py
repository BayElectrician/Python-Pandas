import pandas as pd
import os
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

def startFunc():
    os.system('cls')
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
        userInput = input("Which Question Would you like Answered?: ")
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
    numOfRecords = clinicData.shape[0]
    print(f"The number of rows is {numOfRecords}")
    numOfVar = clinicData.shape[0] * clinicData.shape[1]
    print(f"The number of variables within the dataset is {numOfVar}")
    print(' ')


# Question 3
def lastThreeRows():
    print("The Final Three Rows")
    print(' ')
    print(clinicData.tail(3))


# Question 4
def handleData():
    global clinicData

    print("Critical Values:")
    #Critical Values
    # Age
    print("Checking Age Values")
    clinicData.loc[clinicData["age"] > 120, "age"] = 120
    clinicData.loc[clinicData["age"] < 0, "age"] = 0
    clinicData.dropna(subset=["age"], inplace=True)
    
    # Gender
    print("\nChecking Gender Values")
    clinicData.dropna(subset=["gender"], inplace=True)

    #Cholesterol
    print("\nChecking Cholesterol Values")
    clinicData.loc[clinicData["cholesterol"] > 300, "cholesterol"] = 300
    clinicData.loc[clinicData["cholesterol"] < 0, "cholesterol"] = 0
    clinicData.dropna(subset=["cholesterol"], inplace=True)

    # Risk Status
    print("\nChecking Risk Status")
    clinicData = clinicData[clinicData["risk_status"].isin([0.0, 1.0])]

    print("\n\nNon-critical Values")
    #None Critical Values
    #BMI
    print("\nChecking BMI")
    clinicData.loc[clinicData["bmi"] < 0, "bmi"] = clinicData["bmi"].abs()

    #Exercise
    print("\nChecking exercise")
    clinicData.loc[clinicData["exercise_level"] < 0, "exercise_level"] = clinicData["exercise_level"].abs()


# Question 5
def dataInsights():
    minAge = clinicData["age"].min()
    maxAge = clinicData["age"].max()
    meanAge = round(clinicData["age"].mean(), 2)
    medAge = clinicData["age"].median()

    minBMI = clinicData["bmi"].min()
    maxBMI = clinicData["bmi"].max()
    meanBMI = round(clinicData["bmi"].mean(), 2)
    medBMI = clinicData["bmi"].median()

    minExer = clinicData["exercise_level"].min()
    maxExer = clinicData["exercise_level"].max()
    meanExer = round(clinicData["exercise_level"].mean(), 2)
    medExer = clinicData["exercise_level"].median()

    minSys = clinicData["systolic_bp"].min()
    maxSys = clinicData["systolic_bp"].max()
    meanSys = round(clinicData["systolic_bp"].mean(), 2)
    medSys = clinicData["systolic_bp"].median()

    minDias = clinicData["diastolic_bp"].min()
    maxDias = clinicData["diastolic_bp"].max()
    meanDias = round(clinicData["diastolic_bp"].mean(), 2)
    medDias = clinicData["diastolic_bp"].median()

    minChol = clinicData["cholesterol"].min()
    maxChol = clinicData["cholesterol"].max()
    meanChol = round(clinicData["cholesterol"].mean(), 2)
    medChol = clinicData["cholesterol"].median()

    minHealth = clinicData["health_score"].min()
    maxHealth = clinicData["health_score"].max()
    meanHealth = round(clinicData["health_score"].mean(), 2)
    medHealth = clinicData["health_score"].median()


    insightsTable = pd.DataFrame(
             {
                 "Minimum": [minAge, minBMI, minExer, minSys, minDias, minChol, minHealth],
                 "Maximum": [maxAge, maxBMI, maxExer, maxSys, maxDias, maxChol, maxHealth],
                 "Mean": [meanAge, meanBMI, meanExer, meanSys, meanDias, meanChol, meanHealth],
                 "Medium": [medAge, medBMI, medExer, medSys, medDias, medChol, medHealth]
            },
            index=["Age", "BMI", "Exercise", "Systolic", "Diastolic", "Cholesterol", "Health Score"]
    )
    print(insightsTable)


# Question 6
def cholesterolHistogram():
    print("The graph will shwo up on another screen")

    '''
    Matplotlib Histogram is amazing
    The pandas DataFrame can be chosen through changing cholesterol to whatever
    column name is desired.
    The number of histogram bars can be controlled through changing the bins to 
    number requested.
    '''
    plt.hist(clinicData["cholesterol"], bins=20, color='skyblue', edgecolor='black')
    plt.xlabel("Cholesterol")
    plt.ylabel("Frequency")
    plt.title("Frequency of Cholesterol points in the Clinic Data")
    plt.show()


# Question 7
def barAgeDistrobution():
    countYoung = 0
    countMid = 0
    countOld = 0
    countElse = 0
    for x in clinicData["age"]:
        if x <= 18:
            countYoung += 1
        elif 18 < x < 60:
            countMid += 1
        elif x >= 60:
            countOld += 1
        else:
            print(x)
            countElse += 1
    
    yIncrement = [countYoung, countMid, countOld, countElse]
    print("The bar chart will display on a new window")

    grouping = ["Child(<=18)", "Adult(19-59)", "Senior(60+)", "No Age Entered"]
    data = [countYoung, countMid, countOld, countElse]

    plt.bar(grouping, data)
    plt.xlabel("Age Groups")
    plt.ylabel("Frequency")
    plt.yticks(np.arange(0, max(yIncrement)+20, 10))
    plt.title("Frequency of Age Grouping in Data")

    plt.show()


# Question 8
def riskGenderChart():
    femaleRiskZero = 0
    femaleRiskOne = 0

    maleRiskZero = 0
    maleRiskOne = 0

    errorRiskZero = 0
    errorRiskOne = 0
    
    genders = ["Male", "Female", "Error"]
    for index, row in clinicData.iterrows():
        if row["gender"] == 0:
            if row["risk_status"] == 0:
                femaleRiskZero += 1
            else:
                femaleRiskOne += 1
        elif row["gender"] == 1:
            if row["risk_status"] == 0:
                maleRiskZero += 1
            else:
                maleRiskOne += 1
        else:
            if row["risk_status"] == 0:
                errorRiskZero += 1
            else:
                errorRiskZero += 1

    labels = ["Low", "High"]
    data1 = [femaleRiskZero, femaleRiskOne]
    data2 = [maleRiskZero, maleRiskOne]
    data3 = [errorRiskZero, errorRiskOne]

    # Width and Position of axes
    w, x = 0.25, np.arange(len(labels))
    plt.bar(x - w, data1, width=w, label=genders[0])
    plt.bar(x, data2, width=w, label=genders[1])
    plt.bar(x + w, data3, width=w, label=genders[2])

    plt.xticks([0, 1], labels)
    plt.xlabel("Cardiovascular Risk Status")
    plt.ylabel("Frequency")
    plt.title("Frequency of Risk Status of Each Gender")
    plt.legend()
    plt.show()


# Question 9
def scatterPlot():
    xData = clinicData["systolic_bp"]
    yData = clinicData["cholesterol"]

    plt.scatter(xData, yData)
    plt.xlabel("Systolic BP (mm/Hg)")
    plt.ylabel("Cholesterol")
    plt.title("Connection between Systolic BP and Cholesterol")
    plt.show()


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
        replaceCSV = pd.read_csv("./Clean-ClinicData.csv")
        replaceCSV.to_csv("./ClinicData.csv", index=False)
        exit()

    print(' ')
    os.system("pause")
    startFunc()

startFunc()
