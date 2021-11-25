import pandas as pd
import numpy as np

df = pd.read_csv('ViewingActivity.csv')

df = df.drop(['Attributes', 'Device Type', 'Bookmark', 'Latest Bookmark', 'Country'], axis=1)

df['Start Time'] = pd.to_datetime(df['Start Time'], utc=True)
df['Duration'] = pd.to_timedelta(df['Duration'])
df['Title'] = df['Title'].str.replace(r":.*", "")
df['Supplemental Video Type'] = df[(df['Supplemental Video Type'].isna())]
titles = df.groupby(['Profile Name', 'Title'])

print(df.dtypes)
print(df.head(5))
titles_total = titles['Duration'].sum()
print titles_total
