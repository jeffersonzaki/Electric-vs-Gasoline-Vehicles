import pandas as pd

# First electric vehicle dataframe
ev_df = pd.read_csv("Data/ev_pop.csv")[["Model Year", "Make", "Model", "Electric Range", "Base MSRP"]]
ev_df = ev_df.rename(columns={"Model Year": "Year", "Electric Range": "Range", "Base MSRP": "MSRP"})  # Renaming columns

# Second electric vehicle dataframe
ev_df2 = pd.read_csv("Data/vehicles.csv")[["Model Year", "Manufacturer", "Model", "Category"]]
ev_df2 = ev_df2.rename(columns={"Model Year": "Year", "Manufacturer": "Make"})  # Renaming columns

# Functions return top 4 luxury car makers
def audi(df):
    audi_ev = df.loc[df.Make == "Audi"]
    return audi_ev
    
def tesla(df):
    tesla_ev = df.loc[df.Make == "Tesla"]
    return tesla_ev
    
def mercedes(df):
    mercedes_ev = df.loc[df.Make == "Mercedes-Benz"]
    return mercedes_ev
    
def bmw(df):
    bmw_ev = df.loc[df.Make == "BMW"]
    return bmw_ev