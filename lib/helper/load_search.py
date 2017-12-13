import pickle

with open('data/gname', 'rb') as f:
    gname = pickle.load(f)
    
with open('data/gs', 'rb') as f:
    gs = pickle.load(f)
    
with open('data/gid', 'rb') as f:
    gid = pickle.load(f)