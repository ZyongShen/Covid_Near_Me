from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.scrollview import ScrollView
from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.properties import ObjectProperty
from DataHandling import dataHandle
from sodapy import Socrata
from DataHandling import dataHandle
from LocationFinder import locateMe


class ContentNavigationDrawer(BoxLayout):
    pass

class CovidApp(MDApp):

    def build(self):
        return Builder.load_file("widgets.kv")


    def trackMethod(self, method):
        if (method == "typeInput"):
            return "Typing"
        if (method == "findMe"):
            return "LocFinder"

    
    def prepData(self, town = ""):
        handler = dataHandle()
        myFilters = handler.activateFilters(self.root.ids)
        # Apply the filters and the town to get town data
        date, name, data = handler.getData(myFilters, town)
        return date, name, data

    def displayData(self):

        inputTown = str(self.root.ids.input.text)

        # Check if getting data will return a value or not
        try:
            date, name, data = self.prepData(inputTown)
        except:
            self.root.ids.covidInfo.text = "No Town Selected"
            return None
        # Set the value for the output text
        output = ""
        for key in data.keys():
            output += str(key + ": " + data[key] + "\n\n")
        # This will set the town name as the title
        self.root.ids.townTitle.text = name
        # Sets the returned information as the body text
        self.root.ids.covidInfo.text = ("\n" + "Update Date: " + date + "\n\n" + output)
        # Changes the current screen to the results screen
        self.root.ids.screen_manager.current = "results"


    def fromLocFinder(self):
        locFinder = locateMe()
        town = locFinder.getTown()
        town = town.replace(" ", "")
        self.root.ids.input.text = town
        self.displayData()

    def refresh(self):
        self.displayData()

    

    


        
if __name__=="__main__":
    CovidApp().run()