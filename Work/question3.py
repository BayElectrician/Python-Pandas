import pandas as pd

# Used to change the file be parsed
# Added for future security reasons (Should be in a different file)
fileName = "ClinicData" #str(input("What is the name of the file to be parsed?:"))
fileType = "csv" #str(input("What is the type of file being parsed?:")).lower()

# Import and convert to Dataframe
dataImport = pd.read_csv(f"./{fileName}.{fileType}")
global clinic_data
clinicData = pd.DataFrame(data=dataImport)

print(' ')
print("The Final Three Rows")
print(' ')
print(clinicData.tail(3))

