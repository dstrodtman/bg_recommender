def gen_a_bar(sparse_mat, card_mat, epsilon=1e-9):
    sim = sparse_mat.T.dot(sparse_mat)
    a_bar = sim / (card_mat + 1e-9)
    return a_bar


def cardinality_mat(sparse_mat):
    rated = sparse_mat.nonzero()
    rated_mat = np.empty_like(sparse_mat)
    rated_mat[rated] = 1
    card_mat = rated_mat.T.dot(rated_mat)

    return card_mat

def calc_avg(a_bar):
    diag = a_bar.diagonal()
    d_avg = np.sum(diag)/diag.shape[0]
    a_triu = np.triu(a_bar)
    np.fill_diagonal(a_triu, 0)
    sum_a = np.sum(a_triu)
    count = a_triu.nonzero()[0].shape[0]
    avg = sum_a/count

    return avg, d_avg

def gen_a_hat(a_bar, card_mat, avg, d_avg, beta=500):
    diag = a_bar.diagonal()
    card_diag = card_mat.diagonal()
    a_hat_diag = (diag * card_diag + (beta*d_avg)) / (card_diag + beta)
    np.fill_diagonal(a_bar, 0)
    a_hat = (a_bar * card_mat + (beta*avg)) / (card_mat + beta)
    a_hat[range(a_hat.shape[0]), range(a_hat.shape[0])] = a_hat_diag
    return a_hat


















# def a_bar(sparse_mat, upper_right, epsilon=1e-9):
#     sim = sparse_mat.T.dot(sparse_mat)
#     sim_ur = np.triu(sim)
#     np.fill_diagonal(sim_ur, 0)
#     sim_ur / (upper_right + 1e-9)



def gen_a_bar(sparse_mat, card_mat, epsilon=1e-9):
    sim = sparse_mat.T.dot(sparse_mat)
    a_bar = sim / (card_mat + 1e-9)
    return a_bar


def cardinality_mat(sparse_mat):
    rated = sparse_mat.nonzero()
    rated_mat = np.empty_like(sparse_mat)
    rated_mat[rated] = 1
    card_mat = rated_mat.T.dot(rated_mat)

    return card_mat

def calc_avg(a_bar):
    diag = a_bar.diagonal()
    d_avg = np.sum(diag)/diag.shape[0]
    a_triu = np.triu(a_bar)
    np.fill_diagonal(a_triu, 0)
    sum_a = np.sum(a_triu)
    count = a_triu.nonzero()[0].shape[0]
    avg = sum_a/count

    return avg, d_avg

def gen_a_hat(a_bar, card_mat, avg, d_avg, beta=500):
    diag = a_bar.diagonal()
    card_diag = card_mat.diagonal()
    a_hat_diag = (diag * card_diag + (beta*d_avg)) / (card_diag + beta)
    np.fill_diagonal(a_bar, 0)
    a_hat = (a_bar * card_mat + (beta*avg)) / (card_mat + beta)
    a_hat[range(a_hat.shape[0]), range(a_hat.shape[0])] = a_hat_diag
    return a_hat







