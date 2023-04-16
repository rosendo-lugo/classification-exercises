import acquire as acq
import pandas as pd 
import os

from sklearn.model_selection import train_test_split



#-------------------------

def split_function(df, target_varible):
    train, test = train_test_split(df,
                                   random_state=123,
                                   test_size=.20,
                                   stratify= df[target_varible])
    
    train, validate = train_test_split(train,
                                   random_state=123,
                                   test_size=.25,
                                   stratify= train[target_varible])
    return train, validate, test


#-------------------------

# This will clean the data. 
def prep_telco(df_telco):
    '''
    This function will clean the the telco dataset
    '''
    df_telco = df_telco.drop(columns =['contract_type_id', 'internet_service_type_id', 'payment_type_id'])
    
    dummy_telco = pd.get_dummies(df_telco[['gender',
                                             'partner',
                                             'dependents',
                                             'phone_service',
                                             'multiple_lines',
                                             'online_security',
                                             'online_backup',
                                             'device_protection',
                                             'tech_support',
                                             'streaming_tv',
                                             'streaming_movies',
                                             'paperless_billing',
                                             'churn',
                                             'contract_type',
                                             'internet_service_type',
                                             'payment_type']], dummy_na=False, drop_first=[True, True])
    df_telco = pd.concat([df_telco, dummy_telco], axis=1)
    df_telco.total_charges = df_telco.total_charges.str.replace(' ', '0').astype(float)
    return df_telco

#-------------------------


# This will clean the data. 
def prep_titanic(df_titanic):
    '''
    This function will clean the the titanic dataset
    '''
    df_titanic = df_titanic.drop(columns =['embark_town','class','age','deck'])
    dummy_titanic = pd.get_dummies(df_titanic[['sex','embarked']], drop_first=True)
    df_titanic = pd.concat([df_titanic, dummy_titanic], axis=1)
    return df_titanic

#-------------------------

def prep_iris(df_iris):
    '''
    This function prepares the iris data by dropping the species_id and measurement_id.
    It also renames the species_name column to species and creates a dummies for the
    column species and at the end concats the dummy species columns with the iris database
    '''
    df_iris = df_iris.drop(columns = ['species_id', 'measurement_id'])
    df_iris = df_iris.rename(columns={'species_name': 'species'})
    dummy_iris = pd.get_dummies(df_iris.species, drop_first=True)
    df_iris = pd.concat([df_iris, dummy_iris], axis=1)
    return df_iris














