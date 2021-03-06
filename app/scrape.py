from .parser import HTMLParser
import re
import json

ROOT_URL = 'http://www.sainsburys.co.uk/webapp/wcs/stores/servlet/CategoryDisplay?listView=true&orderBy=FAVOURITES_FIRST&parent_category_rn=12518&top_category=12518&langId=44&beginIndex=0&pageSize=20&catalogId=10137&searchTerm=&categoryId=185749&listId=&storeId=10151&promotionId=#langId=44&storeId=10151&catalogId=10137&categoryId=185749&parent_category_rn=12518&top_category=12518&pageSize=20&orderBy=FAVOURITES_FIRST&searchTerm=&beginIndex=0&hideFilters=true'

ALL_FRUITS = {
    'selector': 'div#content h3 a',
    'spec': {
        'title': None,
        'url': 'href'
    }
}

DETAIL1 = {
    'selector': 'div#content p.pricePerUnit',
    'spec': {
        'unit_price': None
    },
}
DETAIL2 = {
    'selector': 'div.productText p',
    'spec': {
        'description': None
    },
}


items = HTMLParser(ROOT_URL)
item_list = items.get_data(ALL_FRUITS['selector'], ALL_FRUITS['spec'])

total_cost = 0

for item in item_list:
    item_detail = HTMLParser(item['url'])
    price = item_detail.get_data(DETAIL1['selector'], DETAIL1['spec'])[0]
    # convert to a pure number
    price['unit_price'] = float(re.sub('[^0-9|.]', '', price['unit_price']))
    item.update(price)
    description = item_detail.get_data(DETAIL2['selector'], DETAIL2['spec'])
    item.update(description[0])
    item['size'] = "%sKb" % round(float(item_detail.get_response_size())/1000, 2)
    total_cost += float(item['unit_price'])
    item.pop('url')

print json.dumps({
    "items": item_list,
    "total": total_cost
})
