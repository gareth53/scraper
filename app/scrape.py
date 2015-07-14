
MENU_SPEC = {
	"title": {
		"selector": "h3 a",
	},
	"url": {
		'selector': 'h3 a.href',
		'attr': 'href'
	}
}

ITEM_SPEC = {
	"unit_price": {
		'selector': 'div.pricing p.pricePerUnit'
	},
 	"description": {
		'selector': 'productText p:first-child'
	} 
}


items = HTMLSeriesParser(url, 'div#productLister div.productInfo', MENU_SPEC)
item_list = items.get_data()

total_cost = 0

for item in item_list:
	item_detail = HTMLSeriesParser(url, selector='', spec=ITEM_SPEC)
	item.update(item_detail.get_data())
	item['size'] = item.detail.get_response_size()
	total_cost += int(item['cost'])

	print json.dumps({
		"items": item_list,
		"total": total_cost  # TODO - decimalize
	})
