def vc_to_dict(column):
    """
    Converts the value_counts of a column of the dataframe to a dictionary 
    Args:
        column (series): the column for which you want the value counts 
    Returns:
        The value counts in dictionary format 
    """
    vc = column.value_counts()
    vc.index = vc.index.astype(str)
    return vc.to_dict()

def subdata(min_,dict_):
    """
    Removes values from a dictionary at a lower frequency than desired 
    Args:
        min_ (int): limit value used for filtering
        dict_ (dict): dictionary to be filtered 
    Returns:
        The dictionary filtered
    """
    list_ = []
    return [value for value,freq in dict_.items() if freq > min_]

def create(df,column,list_):
    """
    Creates a subdataframe with those values of the given column present in the given list 
    Args:
        df (dataframe): dataframe to work with 
        column (series): column of the dataframe to be filtered on
        list_ (list): list with the values that are used for filtering 
    Returns:
        The subdataframe
    """
    return df[df[column].isin(list_)]