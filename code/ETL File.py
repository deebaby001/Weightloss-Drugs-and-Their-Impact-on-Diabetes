#ETL File

import pandas a pd

df = pd.read_csv(Define path for diabetes comorbid csv file from AWS)

print (df.head(5))

print (df.info())

#TRANSFORM

#Delete the following columns: Cholestol Check
#GenHlth
#NoDocbcCost

#LOAD
#Load data to database using (to_sql) command