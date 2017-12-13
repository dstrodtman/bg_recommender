import numpy as np

def get_rated(sparse_mat):
    return sparse_mat.nonzero()

def overall_bias(sparse_mat, rated):
    rating_bias = np.mean(sparse_mat[rated])
    overall_bias_mat = np.zeros_like(sparse_mat)
    overall_bias_mat[rated] = -rating_bias
    res_mat = sparse_mat + overall_bias_mat
    return res_mat, rating_bias

def item_bias(sparse_mat, rated, lam=25):
    sum_ratings = np.sum(sparse_mat, axis=0)
    _, count = np.unique(rated[1], return_counts=True)
    lambda_count = np.add(count, lam)
    item_bias = np.divide(sum_ratings, lambda_count)
    item_bias_mat = np.zeros_like(sparse_mat)
    item_bias_mat[rated] = 1
    item_bias_mat = np.multiply(item_bias_mat, -item_bias)
    res_mat = np.add(sparse_mat, item_bias_mat)
    return res_mat, item_bias

def user_bias(sparse_mat, rated, lam=10):
    sum_ratings = np.sum(sparse_mat, axis=1)
    _, count = np.unique(rated[0], return_counts=True)
    lambda_count = np.add(count, lam)
    user_bias = np.divide(sum_ratings, lambda_count)
    user_bias_mat = np.zeros_like(sparse_mat)
    user_bias_mat[rated] = 1
    user_bias_mat = np.multiply(user_bias_mat.T, -user_bias).T
    res_mat = np.add(sparse_mat, user_bias_mat)
    return res_mat, user_bias






    

# def game_bias(sparse_mat, alpha=5):
#     rated = sparse_mat.nonzero()
#     theta_hat = np.sum(sparse_mat, axis=0)
#     _, count = np.unique(rated[1], return_counts=True)
#     theta = (count*theta_hat)/(count + alpha)
#     game_bias_mat = np.zeros_like(sparse_mat)
#     game_bias_mat[rated] = 1
#     game_bias_mat = (game_bias_mat * -theta)
#     res_mat = sparse_mat + game_bias_mat
#     return res_mat, game_bias_mat

# def user_bias(sparse_mat, alpha=5):
#     rated = sparse_mat.nonzero()
#     theta_hat = np.sum(sparse_mat, axis=1)
#     _, count = np.unique(rated[0], return_counts=True)
#     theta = (count*theta_hat)/(count + alpha)
#     user_bias_mat = np.zeros_like(sparse_mat)
#     user_bias_mat[rated] = 1
#     user_bias_mat = (user_bias_mat.T * -theta).T
#     res_mat = sparse_mat + user_bias_mat
#     return res_mat, user_bias_mat