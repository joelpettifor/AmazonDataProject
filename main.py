import pandas as pd
import numpy as np

df = pd.read_csv('ViewingActivity.csv')

df = df.drop(['Attributes', 'Device Type', 'Bookmark', 'Latest Bookmark', 'Country'], axis=1)

df['Start Time'] = pd.to_datetime(df['Start Time'], utc=True)
df['Duration'] = pd.to_timedelta(df['Duration'])
df['Title'] = df['Title'].str.replace(r":.*", "")
df = df[(df['Supplemental Video Type'].isna())]

titles = df.sort_values(['Profile Name'], ascending=True) \
    .groupby(['Profile Name', 'Title']).sum() \
    .apply(lambda x: x.sort_values(['Duration'], ascending=True)) \
    .reset_index(drop=True)

print(titles[['Profile Name','Title','Duration']])

#print(df.head(4))
#print(titles.loc[:5,['Profile Name','Title','Duration']])


