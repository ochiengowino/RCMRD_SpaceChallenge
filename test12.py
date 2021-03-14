import pandas as pd

#READS THE ORIGINAL CSV FILE AS A DATAFRAME
df = pd.read_csv("Likoni.csv", sep=",")

df1 = df.loc[:, ["site", "name", "dateTimeUTC",	"humidity",	"precipitation", "pressure","radiation","temperature", "winddirection", "windspeed"]]

#CONVERTS THE "dateTimeUTC" COLUMN INTO DATE TIME FORM
df1["dateTimeUTC"] = pd.to_datetime(df1.dateTimeUTC)


#CREATES A BUFFER FILE TO HOLD THE DATA FOR PROCESSING
df1.to_csv("Likoni2.csv", sep=",", header=True)

#GROUPS THE DATA BY DATE AS THE REFERENCE
df2 = df1.groupby(pd.Grouper(key="dateTimeUTC", freq="D")).mean()

#SENDS THE DATA TO THE FINAL FILE CONTAINING THE AVERAGES
df2.to_csv("Likoni AVG.csv")


