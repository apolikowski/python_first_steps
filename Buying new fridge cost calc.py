def fridge(shop):
    if shop == "MediaMarkt":
     return 1200
    if shop == "MediaExpert":
     return 1250
    if shop == "Euro":
     return 1150

def delivery(kilometers):
    cost = 10 * kilometers
    if kilometers >= 10:
        cost += 50
    elif kilometers >= 5:
        cost == 0
    return cost

def purchase(shop, kilometers):
    return fridge(shop) + delivery(kilometers)

print (purchase("Euro", 15))
