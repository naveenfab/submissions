#Task 1
import pandas as pd
import numpy as np

def generate_car_matrix(dataset_path):
    # Load the dataset into a DataFrame
    df = pd.read_csv(dataset_path)

    # Create a pivot table using id_1 as index, id_2 as columns, and car as values
    car_matrix = df.pivot(index='id_1', columns='id_2', values='car').fillna(0)

    # Set diagonal values to 0
    np.fill_diagonal(car_matrix.values, 0)

    return car_matrix
    
    # Task 2
   import pandas as pd
import numpy as np

def get_type_count(df):
    # Add a new categorical column 'car_type' based on values of the 'car' column
    conditions = [
        (df['car'] <= 15),
        (df['car'] > 15) & (df['car'] <= 25),
        (df['car'] > 25)
    ]
    choices = ['low', 'medium', 'high']
    df['car_type'] = pd.Series(np.select(conditions, choices, default=np.nan), dtype="category")

    # Calculate the count of occurrences for each 'car_type' category
    type_counts = df['car_type'].value_counts().to_dict()

    # Sort the dictionary alphabetically based on keys
    type_counts = dict(sorted(type_counts.items()))

def generate_car_matrix(df)->pd.DataFrame:
   

    Args:
        df (pandas.DataFrame)
    
    # Task 3
    
import pandas as pd

def get_bus_indexes(df):
    # Calculate the mean value of the 'bus' column
    bus_mean = df['bus'].mean()

def get_type_count(df)->dict:
  

    Args:
        df (pandas.DataFrame)
    # Sort the indices in ascending order
    bus_indexes.sort()

    Returns:
        dict: A dictionary with car types as keys and their counts as values.
  
    # Task 4
      # Group by 'route' and filter based on average 'truck' values
    filtered_routes = df.groupby('route')['truck'].mean().loc[lambda x: x > 7].index.tolist()

    return filtered_routes

    return list()

 def multiply_matrix(matrix)->pd.DataFrame:
    Returns:
        pandas.DataFrame: Modified matrix with values multiplied based on custom conditions.
    
    # Task 5
     # Apply custom multiplication based on conditions
    modified_matrix = matrix.applymap(lambda x: x * 0.75 if x > 20 else x * 1.25).round(1)

    return matrix
    return modified_matrix


def time_check(df)->pd.Series:
def time_check(df: pd.DataFrame)->pd.Series:
    
   
 def time_check(df)->pd.Series:
    Returns:
        pd.Series: return a boolean series
   
    # Task 6
        
    df['start_datetime'] = pd.to_datetime(df['startDay'] + ' ' + df['startTime'])
    df['end_datetime'] = pd.to_datetime(df['endDay'] + ' ' + df['endTime'])

    # Calculate duration for each entry
    df['duration'] = df['end_datetime'] - df['start_datetime']

    # Group by ('id', 'id_2') and check time completeness
    time_completeness = df.groupby(['id', 'id_2']).apply(lambda group: group['duration'].sum() == pd.Timedelta(days=7)).droplevel(2)

    return time_completeness

    return pd.Series()
