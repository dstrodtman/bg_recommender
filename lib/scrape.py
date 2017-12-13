import requests
from scrapy.selector import Selector
from scrapy.http import HtmlResponse

def scrape_game_names(page_num):
    url = 'https://boardgamegeek.com/browse/boardgame/page/{}?sort=numvoters&sortdir=desc'.format(page_num)
    r = requests.get(url)
    html = r.text
    xpath_names = "//tr/td[3]/div/a/text()"
    xpath_links = "//tr/td[3]/div/a/@href"
    
    names = Selector(text=html).xpath(xpath_names).extract()
    links = Selector(text=html).xpath(xpath_links).extract()
    
    return names, links

def get_game_ids(links):
    search = re.compile('\/(\d+)\/').search
    ids = [m.group(1) for m in map(search, links) if m]
    return ids

def mongo_write_games(names, links, ids):
    cli = pymongo.MongoClient('52.36.190.91', 27016)
    db_ref = cli.capstone
    co_ref = db_ref['games']
    
    requests = [InsertOne({'gname': names[i], 'glink': links[i], 'gid': ids[i]}) for i in range(len(ids))]
    
    co_ref.bulk_write(requests)

def save_game_csv(page_num, names, links, ids):
    rows = zip(ids, names, links)
    
    with open('games/page_{}'.format(page_num), 'w') as f:
        writer = csv.writer(f)
        for row in rows:
            writer.writerow(row)





# def scrape_user_names()
#     url = 'https://boardgamegeek.com/boardgame/13/catan/ratings?rated=1&pageid={}'.format(page_num)
#     r = requests.get(url)
#     xpath_names = "//ratings-module//div[@class='comment-header']/div/div/a/text()"
#     user_links = "//ratings-module//div[@class='comment-header']/div/div/a/@href"
#     ratings = "//ratings-module//li/div[@class='summary-item-callout']/div/text()"