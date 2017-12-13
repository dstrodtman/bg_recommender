import numpy as np

def to_sparse(tuples, n_users=50000, n_items=10000):
    sparse_mat = np.zeros((n_users, n_items))
    for row in tuples:
        sparse_mat[row[0]-1, row[1]-1] = row[2]
    return sparse_mat

def calc_sparsity(sparse_mat):
    sparsity = float(len(sparse_mat.nonzero()[0]))
    sparsity /= (sparse_mat.shape[0] * sparse_mat.shape[1])
    sparsity *= 100
    print('Sparsity: {:4.2f}%'.format(sparsity))

# def cosine_similarity(sparse_mat, kind='user', epsilon=1e-9):
#     # epsilon -> small number for handling dived-by-zero errors
#     if kind == 'user':
#         sim = sparse_mat.dot(sparse_mat.T) + epsilon
#     elif kind == 'item':
#         sim = sparse_mat.T.dot(sparse_mat) + epsilon
#     norms = np.array([np.sqrt(np.diagonal(sim))])
#     return (sim / norms / norms.T)

# def predict_simple(sparse_mat, similarity, kind='user'):
#     if kind == 'user':
#         return similarity.dot(sparse_mat) / np.array([np.abs(similarity).sum(axis=1)]).T
#     elif kind == 'item':
#         return sparse_mat.dot(similarity) / np.array([np.abs(similarity).sum(axis=1)])



# def predict_topk(sparse_mat, similarity, kind='user', k=40):
#     pred = np.zeros(sparse_mat.shape)
#     if kind == 'user':
#         for i in xrange(sparse_mat.shape[0]):
#             top_k_users = [np.argsort(similarity[:,i])[:-k-1:-1]]
#             for j in xrange(sparse_mat.shape[1]):
#                 pred[i, j] = similarity[i, :][top_k_users].dot(sparse_mat[:, j][top_k_users]) 
#                 pred[i, j] /= np.sum(np.abs(similarity[i, :][top_k_users]))
#     if kind == 'item':
#         for j in xrange(sparse_mat.shape[1]):
#             top_k_items = [np.argsort(similarity[:,j])[:-k-1:-1]]
#             for i in xrange(sparse_mat.shape[0]):
#                 pred[i, j] = similarity[j, :][top_k_items].dot(sparse_mat[i, :][top_k_items].T) 
#                 pred[i, j] /= np.sum(np.abs(similarity[j, :][top_k_items]))        
    
#     return pred

