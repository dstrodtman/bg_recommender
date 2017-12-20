import numpy as np
from lib import db
from lib.recommend import get_sim
from lib.helper import search

import pickle

with open('data/gname', 'rb') as f:
    gname = pickle.load(f)
    
with open('data/gs', 'rb') as f:
    gs = pickle.load(f)
    
with open('data/gid', 'rb') as f:
    gid = pickle.load(f)


def search_gname(gs_list):
    '''
    Return of list of gnames from list of gs.
    '''
    return [gname[gs] for gs in gs_list]



# try:
#     assert _session_id
# except:
#     _session_id = str(uuid.uuid4())