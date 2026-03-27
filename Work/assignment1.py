import pandas as pd

dataImport = pd.read_csv("./ClinicData.csv")
clinic_data = pd.DataFrame(data=dataImport)
print(clinic_data)
