import acquire as acq
import pandas as pd 
import os

from sklearn.model_selection import train_test_split



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

-------------------------


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

--------------------------
train_df_iris, validate_df_iris, test_df_iris = split_function(df_iris, 'species')

print(f'Prepared df: {df_iris.shape}')
print()
print(f'Train: {train_df_iris.shape}')
print(f'Validate: {validate_df_iris.shape}')
print(f'Test: {test_df_iris.shape}')

--------------------------
train_df_titanic, validate_df_titanic, test_df_titanic = split_function(df_titanic, 'survived')

print(f'Prepared df: {df_titanic.shape}')
print()
print(f'Train: {train_df_titanic.shape}')
print(f'Validate: {validate_df_titanic.shape}')
print(f'Test: {test_df_titanic.shape}')

-------------------------
train_df_telco, validate_df_telco, test_df_telco = split_function(df_telco, 'churn')

print(f'Prepared df: {df_telco.shape}')
print()
print(f'Train: {train_df_telco.shape}')
print(f'Validate: {validate_df_telco.shape}')
print(f'Test: {test_df_telco.shape}')














