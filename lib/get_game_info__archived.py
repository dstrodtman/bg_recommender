import csv
import requests
import xml.etree.ElementTree as ET
import pymongo

def get_id_list(page_num):
    ids = []
    glinks = []

    with open('games/page_{}'.format(page_num, 'r')) as f:
        reader = csv.reader(f)
        for row in reader:
            ids.append(row[0])
            glinks.append(row[2])
            
    api_id_list = ','.join(ids)  
    return api_id_list, ids, glinks

def get_game_tree(api_id_list):
    api_q = 'http://www.boardgamegeek.com/xmlapi/boardgame/{}?stats=1'.format(api_id_list)
    r = requests.get(api_q)
    tree = ET.fromstring(r.text)

    return tree

class game_info():

    def __init__(self, gid, glink, tree):

        root = tree.find("boardgame[@objectid='{}']".format(gid))
        
        self.gid = gid

        try:
            self.gname = root.find("name[@primary='true']").text
        except:
            self.gname = ''

        sub_name = []
        sub_id = []
        for item in root.findall('boardgamesubdomain'):
            sub_name.append(item.text)
            sub_id.append(item.attrib['objectid'])
        self.subdomain = list(zip(sub_id, sub_name))

        fam_name = []
        fam_id = []
        for item in root.findall('boardgamefamily'):
            fam_name.append(item.text)
            fam_id.append(item.attrib['objectid'])
        self.bgfamily = list(zip(fam_id, fam_name))

        mec_name = []
        mec_id = []
        for item in root.findall('boardgamemechanic'):
            mec_name.append(item.text)
            mec_id.append(item.attrib['objectid'])
        self.mechanic = list(zip(mec_id, mec_name))

        cat_name = []
        cat_id = []
        for item in root.findall('boardgamecategory'):
            cat_name.append(item.text)
            cat_id.append(item.attrib['objectid'])
        self.category = list(zip(cat_id, cat_name))

        try:
            self.yearpublished = int(root.find('yearpublished').text)
        except:
            self.yearpublished = ''

        try:
            self.minplaytime = int(root.find('minplaytime').text)
        except:
            self.minplaytime = ''

        try:
            self.maxplaytime = int(root.find('maxplaytime').text)
        except:
            self.maxplaytime = ''

        try:
            self.age = int(root.find('age').text)
        except:
            self.age = ''

        try:
            self.minplayers = int(root.find('minplayers').text)
        except:
            self.minplayers = '' 
        
        try:
            self.maxplayers = int(root.find('maxplayers').text)
        except:
            self.maxplayers = '' 
        
        # self.numplayers = {}
        # if (self.minplayers != '') and (self.maxplayers != ''):
        #     for num in range(self.minplayers, self.maxplayers+1):
        #         num = str(num)
        #         self.numplayers[num] = {}
        #         for vote in ['Best', 'Recommended', 'Not Recommended']:
        #             result = root.find("poll[@name='suggested_numplayers']/results[@numplayers='{}']/result[@value='{}']".format(num, vote))
        #             self.numplayers[num][vote] = result.attrib['numvotes']

        try:
            self.avgrating = float(root.find("statistics/ratings/average").text)
        except:
            self.avgrating = ''

        try:
            self.bayesrating = float(root.find("statistics/ratings/bayesaverage").text)
        except:
            self.bayesrating = ''

        try:
            self.complexity = float(root.find("statistics/ratings/averageweight").text)
        except:
            self.complexity = ''

        try:
            self.numratings = int(root.find("statistics/ratings/usersrated").text)
        except:
            self.numratings = ''

        try:
            self.ratingstd = float(root.find("statistics/ratings/stddev").text)
        except:
            self.ratingstd = ''

        # try:
        #     self.description = root.find('description').text
        # except:
        #     self.description = ''

        # self.implementations = [item.attrib['objectid'] for item in root.findall('boardgameimplementation')]

        # self.expansions = [item.attrib['objectid'] for item in root.findall('boardgameexpansion')]

# def mongo_write_game_info(game_info):
#     cli = pymongo.MongoClient('52.36.190.91', 27016)
#     db_ref = cli.capstone
#     co_ref = db_ref['game_info']
    
#     co_ref.insert_one({'gname': game_info.gname, 
#                        'gid': game_info.gid,
#                        'subdomain': game_info.subdomain,
#                        'bgfamily': game_info.bgfamily,
#                        'mechanic': game_info.mechanic,
#                        'category': game_info.category,
#                        'yearpublished': game_info.yearpublished,
#                        'minplaytime': game_info.minplaytime,
#                        'maxplaytime': game_info.maxplaytime,
#                        'age': game_info.age,
#                        'minplayers': game_info.minplayers,
#                        'maxplayers': game_info.maxplayers,
#                        'numplayers': game_info.numplayers,
#                        'avgrating': game_info.avgrating,
#                        'bayesrating': game_info.bayesrating,
#                        'complexity': game_info.complexity,
#                        'numratings': game_info.numratings,
#                        'ratingstd': game_info.ratingstd,
#                        'description': game_info.description,
#                        'implementations': game_info.implementations,
#                        'expansions': game_info.expansions})

# def save_game_info_csv(game_info):
#     wide_gi = ','.join([game_info.gid,
#                     game_info.gname, 
#                     '[{}]'.format(','.join(game_info.subdomain)),
#                     '[{}]'.format(','.join(game_info.bgfamily)),
#                     '[{}]'.format(','.join(game_info.mechanic)),
#                     '[{}]'.format(','.join(game_info.category)),
#                     str(game_info.yearpublished),
#                     str(game_info.minplaytime),
#                     str(game_info.maxplaytime),
#                     str(game_info.age),
#                     str(game_info.minplayers),
#                     str(game_info.maxplayers),
#                     str(list(game_info.numplayers.items())),
#                     str(game_info.rating),
#                     str(game_info.bayesrating),
#                     str(game_info.complexity),
#                     str(game_info.numratings),
#                     str(game_info.ratingstd),
#                     '"{}"'.format(game_info.description),
#                     '[{}]'.format(','.join(game_info.implementations)),
#                     '[{}]'.format(','.join(game_info.expansions))
#                          ])
    
#     with open('game_info/{}'.format(game_info.gid), 'w') as f:
#         f.write(wide_gi)


for page in range(1, 101):
    api_id_list, ids = get_id_list(page)
    tree = get_game_tree(api_id_list)
    for gid in ids:
        gi = game_info(gid, tree)
        # mongo_write_game_info(gi)
        # save_game_info_csv(gi)


def write_bg_csv(game_info):
    bg_line = ','.join([game_info.gid,
                    game_info.gname,
                    game_info.glink, 
                    str(game_info.yearpublished),
                    str(game_info.minplaytime),
                    str(game_info.maxplaytime),
                    str(game_info.age),
                    str(game_info.minplayers),
                    str(game_info.maxplayers),
                    str(game_info.avgrating),
                    str(game_info.bayesrating),
                    str(game_info.complexity),
                    str(game_info.numratings),
                    str(game_info.ratingstd),
                         ])
    with open('csv/bg_info', 'a') as f:
        f.write(bg_line + '\n')

    # gid, 
    # gname,
    # glink,
    # yearpublished,
    # minplaytime,
    # maxplaytime,
    # age,
    # minplayers,
    # maxplayers,
    # avgrating,
    # bayesrating,
    # complexity,
    # numratings,
    # ratingstd

def write_feat_csv(game_info):
    with open('csv/feats', 'a') as f:
        for sub in self.subdomain:
            f.write(sub + '\n')

    fid,
    fname,
    fclass,
    gid
