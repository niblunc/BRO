import ipywidgets as widgets
from ipywidgets import interact, interact_manual
import os, glob
import pandas as pd
from IPython.display import display

# variables
csvs=[x.split("/")[-1] for x in glob.glob(os.path.join('/content/gdrive/My Drive/Projects/bromo/data/reports', '*.csv'))]
ALL = 'ALL'
data_path='/content/gdrive/My Drive/Projects/bromo/data/reports'
df_base= pd.read_csv('/content/gdrive/My Drive/Projects/bromo/data/reports/volume_report.csv')



def unique_sorted_values_plus_ALL(array):
    unique = array.unique().tolist()
    unique.sort()
    unique.insert(0, ALL)
    return unique;

def make_df(csv):
    file_path = os.path.join(data_path, csv)
    df = pd.read_csv(file_path)
    return df

@interact
def show_subject(file = csvs, subject= unique_sorted_values_plus_ALL(df_base['participantID'].dropna())):
    # get file dataframe
    df = make_df(file)

    if subject == "ALL":
        return df
    else:
        return df.loc[df['participantID'] == subject]
    #return taste_data