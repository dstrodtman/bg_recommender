import numpy as np
from lib import db
from time import time

with open('../../data/item_bias', 'rb') as f:
    bias = f.read()

class Recommender():
    
    def __init__(self):
        self.liked = set()
        self.bag = set()
        self.recs = None
        
    def update(self, c_liked):
        self.start = time()
        if self.liked.symmetric_difference(c_liked):
            self.liked = c_liked
            self.get_liked()
            self.get_bag()
            self.get_exp()
            self.clean_bag()
            self.get_rec_lu()
            self.get_sim()
            self.add_bias()
            self.get_recs()
            self.signal_complete()
        else:
            self.signal_complete()

    def get_liked(self):
        con, cur = db.con_cur.bgg_tuples()
        cur.execute('SELECT * FROM rec_lookup WHERE gs IN ({});'.format(self.liked))
        self.sql_tuples = cur.fetchall()
        con.close()

    def get_bag(self):
        self.bag = set()
        for row in range(len(self.sql_tuples)):
            item_bag.update(self.sql_tuples[row][1])

    def get_exp(self):
        self.exp = set(self.liked)
        for row in range(len(self.sql_tuples)):
            exp.update(self.sql_tuples[row][4])
        
    def clean_bag(self):
        self.bag.difference_update(self.exp)

    def get_rec_lu(self):    
        self.rec_lu = list(self.bag)

    def get_sim(self):
        self.sim = np.array(tuple(self.sql_tuples[row][3][self.rec_lu] for row 
                                    in range(len(self.sql_tuples))))
        self.sim = np.sum(self.sim, axis=0)

    def add_bias(self):
        self.sim = np.add(self.sim, bias[self.rec_lu])

    def get_recs(self):
        self.rec_order = np.argsort(self.sim)[::-1]
        self.recs = self.rec_lu[self.rec_order]

    def signal_complete(self):
        self.complete = time()