import numpy as np

def by_feats(gs, K, cos_sim_mat):
    '''
    Returns array of gs for top K games with greatest similarity to gs, along with 
    their similarity rating, based on precomputed cosine similarity of feature vectors.

    top_games_feat, top_games_feat_sim = get_sim.by_feats(gs, K, cos_sim_mat)

    '''
    top_games_feat = np.argsort(cos_sim_mat[gs])[-2:-(K+2):-1]
    top_games_feat_sim = np.sort(cos_sim_mat[gs])[-2:-(K+2):-1]

    return top_games_feat, top_games_feat_sim

def by_items(gs, K, corr_mat):
    '''
    Returns array of gs for top K games with greatest similarity to gs, along with 
    their similarity rating, based on precomputed Pearson correlation of item-item pairs.

    top_games_item, top_games_item_sim = get_sim.by_items(gs, K, corr_mat)

    '''
    top_games_item = np.argsort(corr_mat[gs])[-2:-(K+2):-1]
    top_games_item_sim = np.sort(corr_mat[gs])[-2:-(K+2):-1]

    return top_games_item, top_games_item_sim


