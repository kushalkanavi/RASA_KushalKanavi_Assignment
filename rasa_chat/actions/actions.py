# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
import requests

class ActionPincodeEntry(Action):

    def name(self) -> Text:
        return "action_pincode"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        user_entry = tracker.latest_message['text']
        pincode = [int(s) for s in user_entry.split() if s.isdigit()]
        print('User Entry : ', user_entry)
        print('Pincode : ', pincode[0])

        response = requests.get("https://api.postalpincode.in/pincode/"+str(pincode[0])).json()
        print('response : ', response[0]['PostOffice'])

        name = ''
        for i in response[0]['PostOffice']:
            name = name + '\n'+i['Name']
            state = i['Circle']
            district = i['District']
            message = 'State : '+state+'  District : '+district+'\n'+"Please Choose 'Area' from : "+name+'\n\n'+"Please Type Area Name as Eg: 'Area : Delhi'"


        dispatcher.utter_message(message)

        return []

class ActionAreaEntry(Action):

    def name(self) -> Text:
        return "action_area"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        user_entry = tracker.latest_message['text']
        area = user_entry.split(' : ')
        categories = requests.get("http://ec2-3-23-130-174.us-east-2.compute.amazonaws.com:8000/categories").json()

        category = ''
        for c in categories['data']:
            category = category + '\n'+c
        
        message = "For "+str(area[1])+", Choose from Category Below : "+"\n"+category

        dispatcher.utter_message(message)

        return []

class ActionCategoryEntry(Action):

    def name(self) -> Text:
        return "action_category"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        user_entry = tracker.latest_message['text']

        categories = requests.get("http://ec2-3-23-130-174.us-east-2.compute.amazonaws.com:8000/categories").json()
        
        if user_entry in categories['data']:
            message = 'You Chose : ' + user_entry + '\n' + 'This Help will be provided to you.'
        else:
            message = 'You have choosen the wrong option. Please choose the right option'+'\n'+ " - Or Type New Indian Pincode as Eg: 'pincode : 560040'"

        dispatcher.utter_message(message)

        return []

#
#
# class ActionHelloWorld(Action):
#
#     def name(self) -> Text:
#         return "action_hello_world"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#
#         dispatcher.utter_message(text="Hello World!")
#
#         return []
