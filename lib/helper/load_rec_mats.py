import pickle

with open('data/feat_mat', 'rb') as f:
    feat_mat = pickle.load(f)

with open('data/item_mat', 'rb') as f:
    item_mat = pickle.load(f)

with open('data/exp_mat', 'rb') as f:
    exp_mat = pickle.load(f)

with open('data/item_bias', 'rb') as f:
    item_bias = pickle.load(f)