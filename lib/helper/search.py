def make_lookup(gnames_dict):
    '''
    Return dicts that allow for quick lookup of gname or gid by gs, or gs by gname.

    gname, gs, gid = make_lookup(gnames_dict)

    '''

    gname = {}
    for row in gnames_dict:
        gname[row['gs']-1] = row['gname']

    gs = {}
    for row in gnames_dict:
        gs[row['gname']] = row['gs']-1

    gid = {}
    for row in gnames_dict:
        gid[row['gs']-1] = row['gid']

    return gname, gs, gid

def gname(gs_list):
    '''
    Return of list of gnames from list of gs.
    '''
    return [gname[gs] for gs in gs_list]