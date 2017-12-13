from pandas.algos import nancorr
import numpy as np

def cardinality_set(sparse_mat):
    rated = sparse_mat.nonzero()
    rated_mat = np.empty_like(sparse_mat)
    rated_mat[rated] = 1
    card_mat = rated_mat.T.dot(rated_mat)

    return card_mat

def corr(sparse_mat):
    nan_mat = sparse_mat.copy()
    nan_mat[nan_mat == 0] = np.nan
    corr_mat = nancorr(nan_mat)
    corr_mat = np.nan_to_num(corr_mat)

    return corr_mat

def correct_corr(corr_mat, card_mat, alpha=5):
    denom = np.add(card_mat, alpha)
    scaling = np.divide(card_mat, denom)
    corr_ect = np.multiply(corr_mat, scaling)

    return corr_ect