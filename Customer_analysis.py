import pandas as pd
df = pd.read_csv('customer_shopping_dataset (1).csv')
df.head()
df.info()
# summary statistics using .describe()
df.describe(include='all')
# checking if missing data or null values are present in the dataset
df.isnull().sum()
#input missing values in review rating column with the median rating of the product category
df['Review Rating'] = df.groupby('Category')['Review Rating'].transform(lambda x: x.fillna(x.median()))
df.isnull().sum()
#Renaming columns according to snake casing for better readability and documentation
df.columns = df.columns.str.lower()
df.columns = df.columns.str.replace(' ','_')
df = df.rename(columns={'purchase_amount_(usd)':'purchase_amount'})
df.columns
# Create a new column age_group
labels = ['Young Adult', 'Adult', 'Middle-aged', 'Senior']
df['age_group'] = pd.qcut(df['age'], q=4, labels=labels)
df[['age','age_group']].head(10)
#create new column purchase_frequency_days
frequency_mapping = {
    'Fortnightly':14,
    'weekly':7,
    'monthly':30,
    'quarterly':90,
    'Bi-weekly':14,
    'annually':365,
    'every 3 months':90
}

df['purchase_frequency_days'] = df['frequency_of_purchases'].map(frequency_mapping)
df[['purchase_frequency_days','frequency_of_purchases']].head(10)
df[['discount_applied','promo_code_used']].head(10)
(df['discount_applied'] == df['promo_code_used']).all()
# dropping promo code used column
df = df.drop('promo_code_used', axis=1)
df.columns

import pymysql
import sqlalchemy

from sqlalchemy import create_engine
from sqlalchemy import create_engine

username = "root"
password = "root"
host = "localhost"
port = "3306"
database = "customer_behaviour"

engine = create_engine(
    f"mysql+pymysql://{username}:{password}@{host}:{port}/{database}"
)

print("MySQL connection created successfully")

df.to_sql("customer", engine, if_exists="replace", index=False)

pd.read_sql("SELECT * FROM customer LIMIT 5;", engine)
