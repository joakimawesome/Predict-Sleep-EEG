"""Functions for LISC search notebook"""

import os
import copy
import pandas as pd
from lisc.utils.io import save_object

def format_terms(words:list[str], tool:str) -> str:
    if tool == 'urllib':
        return ' OR '.join([f'"{word}"' for word in words])
    elif tool == 'lisc':
        return [f'"{word}"' for word in words]
    else:
        raise Exception("Argument 'tool' missing. Must be 'urllib' or 'lisc'.")


def run_and_save(counts, filename:str, db):
    '''
    Executes run_collection() on Counts object and saves it to SCDB (database).

    Parameters
    ----------
    counts : Counts
        Object to save out.
    filename : str
        Name of .p file.
    db : SCDB
        Database object
    '''
    # Run co-occurrences of search terms.
    counts.run_collection()

    # Save the data to SCDB.
    main_dir = os.path.dirname(os.getcwd())
    db_dir = os.path.join(main_dir, 'data/', db.get_folder_path('counts'))
    save_object(counts, filename, directory=db_dir)


def load_counts(filename:str, db):
    '''
    Returns Counts object from SCDB (database).

    Parameters
    ----------
    filename : str 
        Name of .p file.
    db : SCDB
        Database object
        
    Returns
    -------
    Counts
    '''
    main_dir = os.path.dirname(os.getcwd())
    data_rpath = db.get_file_path('counts', filename)
    data_abspath = os.path.join(main_dir, 'data/', data_rpath)
    return pd.read_pickle(data_abspath)

    
def pick_top(counts, top_n:int=None, thresh:float=None) -> list[tuple]:
    '''
    Returns the top 'n' co-occurrence or top percentile co-occurrences terms

    Parameters
    ----------
    counts : Counts
        Counts object.
    top_n : int, optional
        The number of best co-occurrence results to return.
    thresh : float, optional
        Set the threshold that co-occurrence scores must meet.
    Returns
    -------
    top : list[tuple]
        List of tuples with each tuple containing two co-occurrence terms.
    '''
    counts = copy.deepcopy(counts)
    len_A = len(counts.terms['A'].terms)
    len_B = len(counts.terms['B'].terms)

    top = []
    if top_n:
        thresh = 0

    assert 0 < thresh < 1, "'thresh' must be float between 0 and 1."

    for i in range(len_A):
        for j in range(len_B):
            if counts.score[i][j] > counts.score.max() * thresh:
                top.append([counts.terms['A'].terms[i][0], counts.terms['B'].terms[j][0], counts.score[i][j]])

    top = sorted(top, key=lambda x: x[2], reverse=True)
    if top_n:
        top = top[:top_n]
    return top 
