from sodapy import Socrata

class dataHandle():

    def __init__(self):
        client = Socrata("data.ct.gov", None)
        self.results = client.get("28fr-iqnx", limit=2000)

    def getTownInfo(self, town):
        # sorts the results into an array
        results = self.results
        townData = []
        for i in range(len(results)):
            if str(results[i]['town']).lower() == town.lower():
                townData.append(results[i])
        return townData[0]

    def activateFilters(self, switches = None):
        # To on takes a list of keys(id's) to change to true
        filters = {
            'Total Confirmed': switches.confirmedcases.active,
            'Case Rate (Per 100,000)': switches.rate.active,
            'Deaths': switches.deaths.active,
            'Total Probable': switches.probcases.active,
            'People Tested': switches.peopletested.active,
            'Total Tests': switches.totaltests.active,
            'Total Positives': switches.numberpositives.active,
            'Total Negatives': switches.numbernegatives.active,
            'Total Unknowns': switches.numberunknowns.active
        }
        
        return filters
        
    def getData(self, filters = {}, town = ""):
        townData = self.getTownInfo(town)
        results = {}
        data = {
            'Total Confirmed': townData['townconfirmedcases'],
            'Case Rate (Per 100,000)': str(float(townData['towncaserate']) / 100000) + '%',
            'Deaths': townData['towntotaldeaths'],
            'Total Probable': townData['townprobablecases'],
            'People Tested': townData['peopletested'],
            'Total Tests': townData['numberoftests'],
            'Total Positives': townData['numberofpositives'],
            'Total Negatives': townData['numberofnegatives'],
            'Total Unknowns': townData['numberofindeterminates']
        }
        for key in filters.keys():
            if (filters[key] is True):
                results[key] = data[key]

        townName = townData["town"]
        updateDate = townData['lastupdatedate']
        updateDate = updateDate.split("T")
        updateDate = updateDate[0]
        
        # returns the update
        return updateDate, townName, results

        


handler = dataHandle()
results = handler.getTownInfo('Wethersfield')
print(results)



    

