#!/usr/bin/env python
# coding: utf-8

# In[3]:


"""Function file"""


# In[4]:


# Function to analyse the four data files and see how to merge them before clean up

def first_analysis(dataf):
    """Analyses briefly a DataFrame, displays, head, columns, shape, dtypes and checks on the null values"""
    display(dataf.head())
    display(dataf.columns)
    display(f'shape: {dataf.shape}')
    display(dataf.dtypes)
    print(f'Looking for null values: \n{dataf.isnull().sum().sort_values(ascending=False)}')


# In[5]:


def num_stats(df, column):
    """Function to generate the statistical data for numerical columns à la describe with mode in addition"""
    import seaborn as sns
    
    print(f'****** Brief Analysis of {column} *****')
          
    mean_col = df[column].mean().round()
    median_col = df[column].median()
    mode_col = df[column].mode()[0]
    variance_col = round(df[column].var(),2)
    std_dev_col = round(df[column].std(),2)
    min_col = df[column].min()
    max_col = df[column].max()
    range_col = max_col - min_col
    quantiles_col = df[column].quantile([0.25, 0.5, 0.75])

    print(f'mean= {mean_col}, median= {median_col}, mode= {mode_col}')
    print(f'var = {variance_col}, std_dev = {std_dev_col}, min = {min_col}, max = {max_col}, range = {range_col}')
    print(f'quantiles : \n{quantiles_col}')
    
    # Plotting a histogram for the column of the 'data' dataframe
    # 'bins=30' divides the data into 30 bins for more detailed granularity
    sns.histplot(df[column], kde=True, bins=30, color="blue")
    plt.show()  # to show the plot as it goes!
    sns.boxplot(data = df[column], color="lightgreen")
    plt.show()  # to show the plot as it goes!
          


# In[7]:


def cat_stats(df, column):
    """Function to generate the statistical data for categorical columns"""
    import seaborn as sns
    
    print(f'****** Brief analysis of {column} *****')
    frequency_table = df[column].value_counts()
    # Calculating the proportion of each unique value 
    proportion_table = df[column].value_counts(normalize=True)
    display(frequency_table, proportion_table)
      
    mode_col = df[column].mode()
    display(f'mode = {mode_col}')
          
    # Plotting a count plot for the 'MSZoning' column from the dataframe 'df', using the "Set3" palette for coloring
    sns.countplot(data=df, x= column, palette="Set1")
    plt.show() 


# In[ ]:




