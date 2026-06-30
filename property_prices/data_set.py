import pandas as pd
import numpy as np

df = pd.read_csv("C:\\Users\\keely\\OneDrive\\Documents\\Coding Projects\\property_prices\\melb_data.csv")

df = df.drop(columns={'Method', 'SellerG', 'Bedroom2', 'BuildingArea', 'YearBuilt', 'CouncilArea', 'Lattitude', 'Longtitude', 'Regionname', 'Propertycount'})

df['Date'] = pd.to_datetime(df['Date'], dayfirst=True)

print(df.head())