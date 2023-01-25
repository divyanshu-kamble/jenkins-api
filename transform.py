import pandas as pd

df = pd.read_csv("/Users/dkamble.intern/Documents/jenkins-data/csv_file/weather.csv")


df['Date'] = pd.to_datetime(df['timestamp']).dt.date
df['Time'] = pd.to_datetime(df['timestamp']).dt.time
df.drop(['timestamp'], axis=1, inplace=True)
df['temperature'] = df['temperature'].apply(lambda x: x*10)

print(df.head(10))

df.to_csv("/Users/dkamble.intern/Documents/jenkins-data/final_csv/transformed.csv", index=False)

