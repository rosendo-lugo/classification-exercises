import pandas as pd 
from env import get_db_url
import os

def check_file_exists(fn, query, url):
    """
    check if file exists in my local directory, if not, pull from sql db
    return dataframe
    """
    if os.path.isfile(fn):
        print('csv file found and loaded')
        return pd.read_csv(fn, index_col=0)
    else: 
        print('creating df and exporting csv')
        df = pd.read_sql(query, url)
        df.to_csv(fn)
        return df 



def get_titanic_data():
    url = get_db_url('titanic_db')
    filename = 'titanic.csv'
    query = 'select * from passengers'
    
    df = check_file_exists(filename, query, url)
    return df 



def get_iris_data():
    url = get_db_url('iris_db')
    query = '''
            select * from measurements
                join species
                    using (species_id)
            '''
    filename = 'iris.csv'
    df = check_file_exists(filename, query, url)
    return df




def get_telco_data():
    url = get_db_url('telco_churn')
    query = ''' select * from customers
    join contract_types
        using (contract_type_id)
    join internet_service_types
        using (internet_service_type_id)
    join payment_types
        using (payment_type_id)
        '''
    filename = 'telco.csv'
    df = check_file_exists(filename, query, url)

    return df
