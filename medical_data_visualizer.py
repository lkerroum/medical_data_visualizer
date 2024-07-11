import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# 1 Import the data from medical_examination.csv and assign it to the df variable
df = pd.read_csv("medical_examination.csv")

# 2 Create the overweight column in the df variable

bmi = df["weight"].div((df["height"].div(100))**2)
    
df['overweight'] = bmi > 25
df['overweight'] = df['overweight'].replace({True: 1, False: 0})

# 3 Normalize data by making 0 always good and 1 always bad. If the value of cholesterol or gluc is 1, set the value to 0. If the value is more than 1, set the value to 1.
df['cholesterol'] = df['cholesterol'] > 1
df['cholesterol'] = df['cholesterol'].replace({True: 1, False: 0})

df['gluc'] = df['gluc'] > 1
df['gluc'] = df['gluc'].replace({True: 1, False: 0})

# 4 Draw the Categorical Plot in the draw_cat_plot function
def draw_cat_plot():
    # 5 Create a DataFrame for the cat plot using pd.melt with values from cholesterol, gluc, smoke, alco, active, and overweight in the df_cat variable.
    df_cat = pd.melt(df, id_vars=['cardio'], value_vars=['cholesterol', 'gluc', 'smoke', 'alco', 'active', 'overweight'])

    
    # 6 Group and reformat the data in df_cat to split it by cardio. Show the counts of each feature. You will have to rename one of the columns for the catplot to work correctly.
    grouped = df_cat.groupby(['cardio', 'variable', 'value']).size().reset_index(name="count")
    

    # 7 Convert the data into long format and create a chart that shows the value counts of the categorical features using the following method provided by the seaborn library import : sns.catplot()

    fig = sns.catplot(grouped, x="variable", y="count", col="cardio", hue = "value", kind="bar")

    # 8 and 9 Save the figure
    fig.savefig('catplot.png')
    return fig


# 10 Draw the Heat Map in the draw_heat_map function
def draw_heat_map():
    # 11 Clean the data in the df_heat variable by filtering out the patient segments that represent incorrect data
    low_height = df['height'] >= df['height'].quantile(0.025)
    high_height = df['height'] <= df['height'].quantile(0.975)
    low_weight = df['weight'] >= df['weight'].quantile(0.025)
    high_weight = df['weight'] <= df['weight'].quantile(0.975)
    df_heat = df[low_height & high_height & low_weight & high_weight]

    # 12 Calculate the correlation matrix and store it in the corr variable
    corr = df_heat.corr()

    # 13 Generate a mask for the upper triangle and store it in the mask variable
    mask = np.triu(np.ones_like(corr, dtype=bool))

    # 14 Set up the matplotlib figure
    fig, ax = plt.subplots(figsize=(16, 9))

    # 15 Plot the correlation matrix using the method provided by the seaborn 
    sns.heatmap(corr, mask=mask, annot=True)


    # 16 Save the figure
    fig.savefig('heatmap.png')
    return fig

