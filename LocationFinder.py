import geocoder as gc

BING_KEY = 'AodIk13OFjAZz5jakEWtDDj7C9-qhVbluX_DLTnAjRdVv1jZdgvolKJyP6hBSPx3'


class locateMe():
    
    def __init__(self):
        pass

    def getTown(self):
        # get coordinates by using ip address
        geo = gc.ip('me')
        # Set the latitude and longitude to be coordinate values
        coordinates = geo.latlng
        results = gc.bing([coordinates[0], coordinates[1]], method = 'reverse', key = BING_KEY)
        results = str(list(results)[0])
        while (("]" or "[") in results):
            results = results.replace("]", "")
            results = results.replace("[", "")

        results = results.split(",")
        # the second item is a town
        return results[1]


'''
g = geocoder.ip('me')
print(g.latlng)
results = geocoder.bing([g.latlng[0], g.latlng[1]], method = 'reverse', key = BING_API_Key)
results = str(list(results)[0])
results = results.replace("]", "")
newResults = results.replace("[", "")
newResults = newResults.split(",")
print(newResults)
'''
