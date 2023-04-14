import pandas as pd
import os
import env

from sklearn.model_selection import train_test_split



def clean_titanic(df):
    '''
    This function will clean the the titanic dataset
    '''
    df = df.drop(columns =['embark_town','class','age','deck'])

    df.embarked = df.embarked.fillna(value='S')

    dummy_df = pd.get_dummies(df[['sex','embarked']], drop_first=True)
    df = pd.concat([df, dummy_df], axis=1)
    return df


# This will only work on survived
def split_titanic(df): 
    '''
    Takes in the titanic dataframe and return train, validate, test subset dataframes
    '''
    train, test = train_test_split(df, #first split
                                   test_size=.2, 
                                   random_state=123, 
                                   stratify=df.survived) 
    train, validate = train_test_split(train, # second split
                                       test_size=.25, 
                                       random_state=123, 
                                       stratify=train.survived)
    return train, validate, test


# Another function? YES PLZ!
def prep_titanic_data(df):
    '''
    The ultimate dishwasher - clean data and split my titanic
    '''
    df = clean_titanic(df)
    train, validate, test = split_titanic(df)
    
    return train, validate, test