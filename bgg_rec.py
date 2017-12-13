import numpy as np
from lib import db
from lib.recommend import get_sim
from lib.helper import search

class Recommender():
    
    def __init__(self, n_games=10000):
        self.u_vec = np.zeros(n_games)
        self.feat_bag = set()
        self.added_to_bag = set()
        self.liked = set()
        self.rated = set()
        self.item_bag = set()
        self.last_get = 0
        
    def rate(self, game_name):
        curr_gs = gs[game_name]
        self.u_vec[curr_gs] = 1
        self.liked.add(curr_gs)
        self.rated.add(curr_gs)
        
    def get_bag(self, K=100):
        to_get = self.liked.difference(self.added_to_bag)
        while to_get:
            game = to_get.pop()
            top_feat_items, sim = get_sim.by_feats(game, K, feat_mat)
            self.feat_bag.update(top_feat_items)
            top_item_items, c_sim = get_sim.by_items(game, K, item_mat)
            self.item_bag.update(top_item_items)
            self.added_to_bag.add(game)
        
    def clean_bag(self):
        self.feat_bag.difference_update(self.rated)
        self.item_bag.difference_update(self.rated)
        exps = set(exp_mat[list(self.rated)].nonzero()[1])
        self.feat_bag.difference_update(exps)
        self.item_bag.difference_update(exps)
        
    def update_bag_vec(self):
        self.feat_bag_vec = np.zeros_like(self.u_vec)
        self.feat_bag_vec[list(self.feat_bag)] = 1
        self.item_bag_vec = np.zeros_like(self.u_vec)
        self.item_bag_vec[list(self.item_bag)] = 1
        
    def get_cum_vecs(self, item_weight=.7, feat_weight=.3):
        rated_sim_bag = np.multiply(corr_ect[list(self.rated)], self.feat_bag_vec)
        cum_corr_vec = np.sum(rated_sim_bag, axis=0)
        self.bias_corr = np.multiply(cum_corr_vec, item_bias)
        rated_corr_bag = np.multiply(cos_sim_mat[list(self.rated)], self.item_bag_vec)
        cum_sim_vec = np.sum(rated_corr_bag, axis=0)
        self.bias_sim = np.multiply(cum_sim_vec, item_bias)
        self.comb_vec = np.add(np.multiply(self.bias_corr, item_weight), np.multiply(self.bias_sim, feat_weight))
        
    def get(self, n):
        if len(self.rated) > self.last_get:
            self.get_bag()
            self.clean_bag()
            self.update_bag_vec()
            self.get_cum_vecs()
        comb_recs = np.argsort(self.comb_vec)[:-(n+1):-1]
        self.top_games = search.gname(comb_recs)
        _ = [print(game) for game in self.top_games]
        self.last_get = len(self.rated)