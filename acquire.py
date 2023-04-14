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



def three_eleven_data(SQL_query):
    '''
    This function will:
    - take in a SQL_query
    - create a connect_url to mySQL
    - return a df of the given query from the 311_data
    '''
    url = get_connection_url("311_data")
    return pd.read_sql(SQL_query, url)

def get_three_eleven_data(SQL_query, directory, filename="three_eleven_.sv"):
    '''
    This function will
    - Check local directory for csv file
        - return id exists
    - If csv doesn't exists:
        - create a df of the SQL_query
        - write df to csv
    - Output three_eleven df
    '''
    if os.path.exists(directory + filename):
        df = pd.read_csv(directory + filename)
        return df
    else:
        df = three_eleven_data(SQL_query)
        
        # want to save to csv 
        # if you want to change where to save your file change your directory
        df.to_csv(directory + filename) 
        return df
    



def albums_data(SQL_query):
    '''
    This function will:
    - take in a SQL_query
    - create a connect_url to mySQL
    - return a df of the given query from the albums_db
    '''
    url = get_connection_url('albums_db')
    return pd.read_sql(SQL_query, url)

def get_albums_data(SQL_query, directory, filename="albums.csv"):
    '''
    This function will
    - Check local directory for csv file
        - return id exists
    - If csv doesn't exists:
        - create a df of the SQL_query
        - write df to csv
    - Output albums df
    '''
    if os.path.exists(directory + filename):
        df = pd.read_csv(directory + filename)
        return df
    else:
        df = albums_data(SQL_query)
        
        # want to save to csv 
        # if you want to change where to save your file change your directory
        df.to_csv(directory + filename) 
        return df
    



def chipotle_data(SQL_query):
    '''
    This function will:
    - take in a SQL_query
    - create a connect_url to mySQL
    - return a df of the given query from the chipotle
    '''
    url = get_connection_url('chipotle')
    return pd.read_sql(SQL_query, url)

def get_chipotle_data(SQL_query, directory, filename="chipotle.csv"):
    '''
    This function will
    - Check local directory for csv file
        - return id exists
    - If csv doesn't exists:
        - create a df of the SQL_query
        - write df to csv
    - Output chipotle df
    '''
    if os.path.exists(directory + filename):
        df = pd.read_csv(directory + filename)
        return df
    else:
        df = chipotle_data(SQL_query)
        
        # want to save to csv 
        # if you want to change where to save your file change your directory
        df.to_csv(directory + filename) 
        return df
    



def elo_data(SQL_query):
    '''
    This function will:
    - take in a SQL_query
    - create a connect_url to mySQL
    - return a df of the given query from the elo_db
    '''
    url = get_connection_url('elo_db')
    return pd.read_sql(SQL_query, url)

def get_elo_data(SQL_query, directory, filename="elo.csv"):
    '''
    This function will
    - Check local directory for csv file
        - return id exists
    - If csv doesn't exists:
        - create a df of the SQL_query
        - write df to csv
    - Output elo df
    '''
    if os.path.exists(directory + filename):
        df = pd.read_csv(directory + filename)
        return df
    else:
        df = elo_data(SQL_query)
        
        # want to save to csv 
        # if you want to change where to save your file change your directory
        df.to_csv(directory + filename) 
        return df
    


def employees_data(SQL_query):
    '''
    This function will:
    - take in a SQL_query
    - create a connect_url to mySQL
    - return a df of the given query from the employees
    '''
    url = get_connection_url('employees')
    return pd.read_sql(SQL_query, url)

def get_employees_data(SQL_query, directory, filename="employees.csv"):
    '''
    This function will
    - Check local directory for csv file
        - return id exists
    - If csv doesn't exists:
        - create a df of the SQL_query
        - write df to csv
    - Output employees df
    '''
    if os.path.exists(directory + filename):
        df = pd.read_csv(directory + filename)
        return df
    else:
        df = employees_data(SQL_query)
        
        # want to save to csv 
        # if you want to change where to save your file change your directory
        df.to_csv(directory + filename) 
        return df
    



def farmers_market_data(SQL_query):
    '''
    This function will:
    - take in a SQL_query
    - create a connect_url to mySQL
    - return a df of the given query from the farmers_market
    '''
    url = get_connection_url('farmers_market')
    return pd.read_sql(SQL_query, url)

def get_farmers_market_data(SQL_query, directory, filename="farmers_market.csv"):
    '''
    This function will
    - Check local directory for csv file
        - return id exists
    - If csv doesn't exists:
        - create a df of the SQL_query
        - write df to csv
    - Output farmers_market df
    '''
    if os.path.exists(directory + filename):
        df = pd.read_csv(directory + filename)
        return df
    else:
        df = farmers_market_data(SQL_query)
        
        # want to save to csv 
        # if you want to change where to save your file change your directory
        df.to_csv(directory + filename) 
        return df
    



def fruits_data(SQL_query):
    '''
    This function will:
    - take in a SQL_query
    - create a connect_url to mySQL
    - return a df of the given query from the fruits_db
    '''
    url = get_connection_url('fruits_db')
    return pd.read_sql(SQL_query, url)

def get_fruits_data(SQL_query, directory, filename="fruits.csv"):
    '''
    This function will
    - Check local directory for csv file
        - return id exists
    - If csv doesn't exists:
        - create a df of the SQL_query
        - write df to csv
    - Output fruits df
    '''
    if os.path.exists(directory + filename):
        df = pd.read_csv(directory + filename)
        return df
    else:
        df = fruits_data(SQL_query)
        
        # want to save to csv 
        # if you want to change where to save your file change your directory
        df.to_csv(directory + filename) 
        return df





def grocery_data(SQL_query):
    '''
    This function will:
    - take in a SQL_query
    - create a connect_url to mySQL
    - return a df of the given query from the grocery_db
    '''
    url = get_connection_url('grocery_db')
    return pd.read_sql(SQL_query, url)

def get_grocery_data(SQL_query, directory, filename="grocery.csv"):
    '''
    This function will
    - Check local directory for csv file
        - return id exists
    - If csv doesn't exists:
        - create a df of the SQL_query
        - write df to csv
    - Output grocery df
    '''
    if os.path.exists(directory + filename):
        df = pd.read_csv(directory + filename)
        return df
    else:
        df = grocery_data(SQL_query)
        
        # want to save to csv 
        # if you want to change where to save your file change your directory
        df.to_csv(directory + filename) 
        return df





def home_credit_data(SQL_query):
    '''
    This function will:
    - take in a SQL_query
    - create a connect_url to mySQL
    - return a df of the given query from the home_credit
    '''
    url = get_connection_url('home_credit')
    return pd.read_sql(SQL_query, url)

def get_home_credit_data(SQL_query, directory, filename="home_credit.csv"):
    '''
    This function will
    - Check local directory for csv file
        - return id exists
    - If csv doesn't exists:
        - create a df of the SQL_query
        - write df to csv
    - Output home_credit df
    '''
    if os.path.exists(directory + filename):
        df = pd.read_csv(directory + filename)
        return df
    else:
        df = home_credit_data(SQL_query)
        
        # want to save to csv 
        # if you want to change where to save your file change your directory
        df.to_csv(directory + filename) 
        return df



def join_example_data(SQL_query):
    '''
    This function will:
    - take in a SQL_query
    - create a connect_url to mySQL
    - return a df of the given query from the join_example
    '''
    url = get_connection_url('join_example_db')
    return pd.read_sql(SQL_query, url)

def get_join_example_data(SQL_query, directory, filename="join_example.csv"):
    '''
    This function will
    - Check local directory for csv file
        - return id exists
    - If csv doesn't exists:
        - create a df of the SQL_query
        - write df to csv
    - Output join_example df
    '''
    if os.path.exists(directory + filename):
        df = pd.read_csv(directory + filename)
        return df
    else:
        df = join_example_data(SQL_query)
        
        # want to save to csv 
        # if you want to change where to save your file change your directory
        df.to_csv(directory + filename) 
        return df




def logs_data(SQL_query):
    '''
    This function will:
    - take in a SQL_query
    - create a connect_url to mySQL
    - return a df of the given query from the logs
    '''
    url = get_connection_url('logs')
    return pd.read_sql(SQL_query, url)

def get_logs_data(SQL_query, directory, filename="logs.csv"):
    '''
    This function will
    - Check local directory for csv file
        - return id exists
    - If csv doesn't exists:
        - create a df of the SQL_query
        - write df to csv
    - Output logs df
    '''
    if os.path.exists(directory + filename):
        df = pd.read_csv(directory + filename)
        return df
    else:
        df = logs_data(SQL_query)
        
        # want to save to csv 
        # if you want to change where to save your file change your directory
        df.to_csv(directory + filename) 
        return df




def mail_customers_data(SQL_query):
    '''
    This function will:
    - take in a SQL_query
    - create a connect_url to mySQL
    - return a df of the given query from the mail_customers
    '''
    url = get_connection_url('mail_customers')
    return pd.read_sql(SQL_query, url)

def get_mail_customers_data(SQL_query, directory, filename="mail_customers.csv"):
    '''
    This function will
    - Check local directory for csv file
        - return id exists
    - If csv doesn't exists:
        - create a df of the SQL_query
        - write df to csv
    - Output mail_customers df
    '''
    if os.path.exists(directory + filename):
        df = pd.read_csv(directory + filename)
        return df
    else:
        df = mail_customers_data(SQL_query)
        
        # want to save to csv 
        # if you want to change where to save your file change your directory
        df.to_csv(directory + filename) 
        return df




def numbers_data(SQL_query):
    '''
    This function will:
    - take in a SQL_query
    - create a connect_url to mySQL
    - return a df of the given query from the numbers
    '''
    url = get_connection_url('numbers')
    return pd.read_sql(SQL_query, url)

def get_numbers_data(SQL_query, directory, filename="numbers.csv"):
    '''
    This function will
    - Check local directory for csv file
        - return id exists
    - If csv doesn't exists:
        - create a df of the SQL_query
        - write df to csv
    - Output numbers df
    '''
    if os.path.exists(directory + filename):
        df = pd.read_csv(directory + filename)
        return df
    else:
        df = numbers_data(SQL_query)
        
        # want to save to csv 
        # if you want to change where to save your file change your directory
        df.to_csv(directory + filename) 
        return df





def pizza_data(SQL_query):
    '''
    This function will:
    - take in a SQL_query
    - create a connect_url to mySQL
    - return a df of the given query from the pizza
    '''
    url = get_connection_url('pizza')
    return pd.read_sql(SQL_query, url)

def get_pizza_data(SQL_query, directory, filename="pizza.csv"):
    '''
    This function will
    - Check local directory for csv file
        - return id exists
    - If csv doesn't exists:
        - create a df of the SQL_query
        - write df to csv
    - Output pizza df
    '''
    if os.path.exists(directory + filename):
        df = pd.read_csv(directory + filename)
        return df
    else:
        df = pizza_data(SQL_query)
        
        # want to save to csv 
        # if you want to change where to save your file change your directory
        df.to_csv(directory + filename) 
        return df




def quotes_data(SQL_query):
    '''
    This function will:
    - take in a SQL_query
    - create a connect_url to mySQL
    - return a df of the given query from the quotes_db
    '''
    url = get_connection_url('quotes_db')
    return pd.read_sql(SQL_query, url)

def get_quotes_data(SQL_query, directory, filename="quotes.csv"):
    '''
    This function will
    - Check local directory for csv file
        - return id exists
    - If csv doesn't exists:
        - create a df of the SQL_query
        - write df to csv
    - Output quotes df
    '''
    if os.path.exists(directory + filename):
        df = pd.read_csv(directory + filename)
        return df
    else:
        df = quotes_data(SQL_query)
        
        # want to save to csv 
        # if you want to change where to save your file change your directory
        df.to_csv(directory + filename) 
        return df





def saas_llc_data(SQL_query):
    '''
    This function will:
    - take in a SQL_query
    - create a connect_url to mySQL
    - return a df of the given query from the saas_llc
    '''
    url = get_connection_url('saas_llc')
    return pd.read_sql(SQL_query, url)

def get_saas_llc_data(SQL_query, directory, filename="saas_llc.csv"):
    '''
    This function will
    - Check local directory for csv file
        - return id exists
    - If csv doesn't exists:
        - create a df of the SQL_query
        - write df to csv
    - Output saas_llc df
    '''
    if os.path.exists(directory + filename):
        df = pd.read_csv(directory + filename)
        return df
    else:
        df = saas_llc_data(SQL_query)
        
        # want to save to csv 
        # if you want to change where to save your file change your directory
        df.to_csv(directory + filename) 
        return df




def sakila_data(SQL_query):
    '''
    This function will:
    - take in a SQL_query
    - create a connect_url to mySQL
    - return a df of the given query from the sakila
    '''
    url = get_connection_url('sakila')
    return pd.read_sql(SQL_query, url)

def get_sakila_data(SQL_query, directory, filename="sakila.csv"):
    '''
    This function will
    - Check local directory for csv file
        - return id exists
    - If csv doesn't exists:
        - create a df of the SQL_query
        - write df to csv
    - Output sakila df
    '''
    if os.path.exists(directory + filename):
        df = pd.read_csv(directory + filename)
        return df
    else:
        df = sakila_data(SQL_query)
        
        # want to save to csv 
        # if you want to change where to save your file change your directory
        df.to_csv(directory + filename) 
        return df





def spam_data(SQL_query):
    '''
    This function will:
    - take in a SQL_query
    - create a connect_url to mySQL
    - return a df of the given query from the spam_db
    '''
    url = get_connection_url('spam_db')
    return pd.read_sql(SQL_query, url)

def get_spam_data(SQL_query, directory, filename="spam.csv"):
    '''
    This function will
    - Check local directory for csv file
        - return id exists
    - If csv doesn't exists:
        - create a df of the SQL_query
        - write df to csv
    - Output spam df
    '''
    if os.path.exists(directory + filename):
        df = pd.read_csv(directory + filename)
        return df
    else:
        df = spam_data(SQL_query)
        
        # want to save to csv 
        # if you want to change where to save your file change your directory
        df.to_csv(directory + filename) 
        return df




def superstore_data(SQL_query):
    '''
    This function will:
    - take in a SQL_query
    - create a connect_url to mySQL
    - return a df of the given query from the superstore_db
    '''
    url = get_connection_url('superstore_db')
    return pd.read_sql(SQL_query, url)

def get_superstore_data(SQL_query, directory, filename="superstore.csv"):
    '''
    This function will
    - Check local directory for csv file
        - return id exists
    - If csv doesn't exists:
        - create a df of the SQL_query
        - write df to csv
    - Output superstore df
    '''
    if os.path.exists(directory + filename):
        df = pd.read_csv(directory + filename)
        return df
    else:
        df = superstore_data(SQL_query)
        
        # want to save to csv 
        # if you want to change where to save your file change your directory
        df.to_csv(directory + filename) 
        return df




def tsa_item_demand_data(SQL_query):
    '''
    This function will:
    - take in a SQL_query
    - create a connect_url to mySQL
    - return a df of the given query from the tsa_item_demand
    '''
    url = get_connection_url('tsa_item_demand')
    return pd.read_sql(SQL_query, url)

def get_tsa_item_demand_data(SQL_query, directory, filename="tsa_item_demand.csv"):
    '''
    This function will
    - Check local directory for csv file
        - return id exists
    - If csv doesn't exists:
        - create a df of the SQL_query
        - write df to csv
    - Output tsa_item_demand df
    '''
    if os.path.exists(directory + filename):
        df = pd.read_csv(directory + filename)
        return df
    else:
        df = tsa_item_demand_data(SQL_query)
        
        # want to save to csv 
        # if you want to change where to save your file change your directory
        df.to_csv(directory + filename) 
        return df





def world_data(SQL_query):
    '''
    This function will:
    - take in a SQL_query
    - create a connect_url to mySQL
    - return a df of the given query from the world
    '''
    url = get_connection_url('world')
    return pd.read_sql(SQL_query, url)

def get_world_data(SQL_query, directory, filename="world.csv"):
    '''
    This function will
    - Check local directory for csv file
        - return id exists
    - If csv doesn't exists:
        - create a df of the SQL_query
        - write df to csv
    - Output world df
    '''
    if os.path.exists(directory + filename):
        df = pd.read_csv(directory + filename)
        return df
    else:
        df = world_data(SQL_query)
        
        # want to save to csv 
        # if you want to change where to save your file change your directory
        df.to_csv(directory + filename) 
        return df





def zillow_data(SQL_query):
    '''
    This function will:
    - take in a SQL_query
    - create a connect_url to mySQL
    - return a df of the given query from the zillow
    '''
    url = get_connection_url('zillow')
    return pd.read_sql(SQL_query, url)

def get_zillow_data(SQL_query, directory, filename="zillow.csv"):
    '''
    This function will
    - Check local directory for csv file
        - return id exists
    - If csv doesn't exists:
        - create a df of the SQL_query
        - write df to csv
    - Output zillow df
    '''
    if os.path.exists(directory + filename):
        df = pd.read_csv(directory + filename)
        return df
    else:
        df = zillow_data(SQL_query)
        
        # want to save to csv 
        # if you want to change where to save your file change your directory
        df.to_csv(directory + filename) 
        return df