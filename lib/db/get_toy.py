import psycopg2 as pg2

def game_ratings_count():
    con, cur = con_cur.bgg_dict()
    cur.execute('SELECT gid, COUNT(*) FROM ratings WHERE gid IN\
                (SELECT gid FROM boardgames) GROUP BY gid;')
    rating_count = cur.fetchall()
    con.close()
    return rating_count

def gids():
    con, cur = con_cur.bgg_dict()
    cur.execute('SELECT gid FROM boardgames;')
    gids = cur.fetchall()
    con.close()
    return gids

def toy_set():
    con, cur = con_cur.bgg_tuples()
    cur.execute('SELECT u.us, g.gs, rating FROM lt t\
                 INNER JOIN lt_users u\
                 ON t.uid=u.uid\
                 INNER JOIN lt_bg g\
                 ON t.gid=g.gid;')
    rating_tuples = cur.fetchall()
    con.close()
    return rating_tuples

def gnames():
    con, cur = con_cur.bgg_dict()
    cur.execute('SELECT b.gid, t.gs, gname FROM boardgames b INNER JOIN lt_bg t ON b.gid=t.gid;')
    gnames = cur.fetchall()
    con.close()
    return gnames

def features():
    con, cur = con_cur.bgg_dict()
    cur.execute('SELECT * FROM feature_lookup;')
    flist = cur.fetchall()
    con.close()
    return flist

def get_toy_game_features():
    con, cur = con_cur.bgg_dict()
    cur.execute('SELECT fid, f.gid, t.gs FROM features f INNER JOIN lt_bg t ON f.gid=t.gid;')
    gflist = cur.fetchall()
    con.close()
    return gflist