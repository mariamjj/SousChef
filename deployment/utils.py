import pandas as pd
import numpy as np


def intersect(df_in, list_ing):
    '''Function to return a dataframe containing recipes, ordered by the measure of intersections. e.g.,
    If 3 ingredients, then it respectively outputs recipes with 3-way intersection, 2-way, no intersection
    Input:
        df_in       : initial dataframe
        list_ingred : list of ingredients 
    '''
    from functools import reduce
    from itertools import combinations

    intersect_ids = []
    
    # Make a dictionary containing dataframes,w/ key:val => index: id's (in dataframe)
    
    dict_dfs = dict()
    for ind, ingred in enumerate(list_ing):
        
        # Build dataframe
        df_out = pd.DataFrame([],columns= df_in.columns)
        df_containing = df_in[df_in['ingred_string'].str.contains(ingred)]
        df_out = df_out.append(df_containing)
        
        # append ids of dataframe to the dictionary
        dict_dfs[ind] = df_out.id.values.tolist()
        
    print(f'1. Recipes with {list_ing[0]}: {len(dict_dfs[0])}, {list_ing[1]}: {len(dict_dfs[1])}, {list_ing[2]}: {len(dict_dfs[2])}')
    
    # First find id's with 3-way intersections
    ids_3way = list(set.intersection(*map(set, [dict_dfs[0],dict_dfs[1],dict_dfs[2]])))
    #print('2. Recipes using all 3 ingredients: ', len(ids_3way))
    df_dummy = pd.DataFrame([], columns=df_in.columns)
    df_3way = df_dummy.append(df_in[df_in.id.isin(ids_3way)])
    print('2. Recipes using all 3 ingredients: ', df_3way.shape[0])

    # Then find id's with 2-way intersections
    ids_2way = []
    for x,y in combinations([dict_dfs[0],dict_dfs[1],dict_dfs[2]], 2):
        ids_2way += list(set.intersection(*map(set, [x,y])))
        ids_2way = list(set(ids_2way))
    #print('3. Recipes using 2 of 3 ingredients: ', len(ids_2way))
    df_2way = df_dummy.append(df_in[df_in.id.isin(ids_2way)])
    print('3. Recipes using 2 of 3 ingredients: ', df_2way.shape[0])

    # Finally, add individual
    for ingred in list_ing:
        df_each = df_dummy.append(df_in[df_in['ingred_string'].str.contains(ingred)])
    df_each = df_each.drop_duplicates(subset='id')
    print('4. Recipes using 1 of 3 ingredients: ',df_each.shape[0])

    # concat all df's and
    df_intersect = df_3way.append(df_2way).append(df_each)
    df_intersect = df_intersect.drop_duplicates(subset='id')
    print('5. Total recipe collection: ', df_intersect.shape[0])

    return df_3way.reset_index(drop=True), df_2way.reset_index(drop=True), df_each.reset_index(drop=True), df_intersect.reset_index(drop=True)

# The final function
def outputRecipes(df_in):
    '''Function returns another dataframe of only relevant data
    Input:
        df_in   - dataframe of interest
    Output:
        df_out  - containing 'title','ingredient','instructions'
        links   - list of url's for each recipe
        images  - list of image_paths
    '''
    df_out = df_in[['title','ingredients','instructions', 'meal_type', 'cuisine']]

    return df_out