import acquire
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
def prep_telco(telco_df):
    '''
    This function will clean the the telco dataset
    '''
    telco_df = telco_df.drop(columns =['contract_type_id', 'internet_service_type_id', 'payment_type_id'])
    
    dummy_telco = pd.get_dummies(telco_df[['gender',
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
    telco_df = pd.concat([telco_df, dummy_telco], axis=1)
    telco_df.total_charges = telco_df.total_charges.str.replace(' ', '0').astype(float)
    return telco_df

#-------------------------


# This will clean the data. 
def prep_titanic(titanic_df):
    '''
    This function will clean the the titanic dataset
    '''
    # Drop any duplicates values
    titanic_df = titanic_df.drop_duplicates()
    
    # Fills the small number of null values for embark_town with the mode
    titanic_df['embark_town'] = titanic_df.embark_town.fillna(value='Southampton')
    
    # Uses one-hot encoding to create dummies of string columns for future modeling 
    dummy_titanic = pd.get_dummies(titanic_df[['sex','embarked']],dummy_na=False, drop_first=True)
    titanic_df = pd.concat([titanic_df, dummy_titanic], axis=1)
    
    # Drops columns that are already represented by other columns
    titanic_df = titanic_df.drop(columns =['passenger_id','embark_town','class','age','deck','sex','embarked'])

    return titanic_df

#-------------------------

def prep_iris(iris_df):
    '''
    This function prepares the iris data by dropping the species_id and measurement_id.
    It also renames the species_name column to species and creates a dummies for the
    column species and at the end concats the dummy species columns with the iris database
    '''
    iris_df = iris_df.drop(columns = ['species_id', 'measurement_id'])
    iris_df = iris_df.rename(columns={'species_name': 'species'})
    dummy_iris = pd.get_dummies(iris_df.species, drop_first=True)
    iris_df = pd.concat([iris_df, dummy_iris], axis=1)
    return iris_df

# ---------------------
# Create a model that includes only age, fare, and pclass. Does this model perform better than your baseline?
# remove the following futures: sibsp	parch	alone	sex_male	embarked_Q	embarked_S
# This will clean the data. 
def prep_titanic2(titanic_df):
    '''
    This function will clean the the titanic dataset
    '''
    
    titanic2_df = titanic_df['age'].fillna(0, inplace=True)
    
    # Drop any duplicates values
    titanic2_df = titanic_df.drop_duplicates()
    
#     # Fills the small number of null values for embark_town with the mode
#     titanic_df['embark_town'] = titanic_df.embark_town.fillna(value='Southampton')
    
#     # Uses one-hot encoding to create dummies of string columns for future modeling 
#     dummy_titanic = pd.get_dummies(titanic_df[['sex','embarked']],dummy_na=False, drop_first=True)
#     titanic_df = pd.concat([titanic_df, dummy_titanic], axis=1)
    
    # Drops columns that are already represented by other columns
    titanic2_df = titanic2_df.drop(columns = ['passenger_id','embark_town',
                                       'class','deck','sex','embarked','sibsp','parch','alone'])
    

    return titanic2_df 


# ---------------------
# Create a model that includes only age, fare, and pclass. Does this model perform better than your baseline?
# remove the following futures: sibsp	parch	alone	sex_male	embarked_Q	embarked_S
# This will clean the data. 
def prep_titanic3(titanic_df):
    '''
    This function will clean the the titanic dataset
    '''
    
    titanic3_df = titanic_df['age'].fillna(0, inplace=True)
    
    # Drop any duplicates values
    titanic3_df = titanic_df.drop_duplicates()
    
#     # Fills the small number of null values for embark_town with the mode
#     titanic_df['embark_town'] = titanic_df.embark_town.fillna(value='Southampton')
    
    # Uses one-hot encoding to create dummies of string columns for future modeling 
    dummy_titanic3 = pd.get_dummies(titanic_df[['sex']],dummy_na=False, drop_first=True)
    titanic3_df = pd.concat([titanic_df, dummy_titanic3], axis=1)
    
    # Drops columns that are already represented by other columns
    titanic3_df = titanic3_df.drop(columns = ['passenger_id','embark_town',
                                       'class','sex','deck','embarked','sibsp','parch','alone'])
    

    return titanic3_df 

# ---------------------
# Create a model that includes only age, fare, and pclass. Does this model perform better than your baseline?
# remove the following futures: sibsp	parch	alone	sex_male	embarked_Q	embarked_S
# This will clean the data. 
def prep_titanic4(titanic_df):
    '''
    This function will clean the the titanic dataset
    '''
    
    titanic4_df = titanic_df['age'].fillna(0, inplace=True)
    
    # Drop any duplicates values
    titanic4_df = titanic_df.drop_duplicates()
    
    # Fills the small number of null values for embark_town with the mode
    titanic4_df['embark_town'] = titanic_df.embark_town.fillna(value='Southampton')
    
    # Uses one-hot encoding to create dummies of string columns for future modeling 
    dummy_titanic4 = pd.get_dummies(titanic4_df[['sex','embarked']],dummy_na=False, drop_first=True)
    titanic4_df = pd.concat([titanic4_df, dummy_titanic4], axis=1)
    
    # Drops columns that are already represented by other columns
    titanic4_df = titanic4_df.drop(columns = ['passenger_id','embark_town',
                                       'class','sex','deck','embarked','sibsp','parch','alone'])
    

    return titanic4_df 









