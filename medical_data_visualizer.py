import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# 1
df = pd.read_csv("medical_examination.csv")

# 2

bmi = df["weight"].div((df["height"].div(100))**2)
    
df['overweight'] = bmi > 25
df['overweight'] = df['overweight'].replace({True: 1, False: 0})

# 3
df['cholesterol'] = df['cholesterol'] > 1
df['cholesterol'] = df['cholesterol'].replace({True: 1, False: 0})

df['gluc'] = df['gluc'] > 1
df['gluc'] = df['gluc'].replace({True: 1, False: 0})

# 4
def draw_cat_plot():
    # 5
    df_cat = pd.melt(df, id_vars=['cardio'], value_vars=['cholesterol', 'gluc', 'smoke', 'alco', 'active', 'overweight'])

    print(df_cat)
    # 6
    grouped = df_cat.groupby(['cardio', 'variable', 'value']).size().reset_index(name="count")
    
    print(grouped)

    # 7

    fig = sns.catplot(grouped, x="variable", y="count", col="cardio", hue = "value", kind="bar")


    # 8


    # 9
    fig.savefig('catplot.png')
    return fig

print(draw_cat_plot())

# 10
def draw_heat_map():
    # 11
    df_heat = None

    # 12
    corr = None

    # 13
    mask = None



    # 14
    fig, ax = None

    # 15



    # 16
    fig.savefig('heatmap.png')
    return fig
