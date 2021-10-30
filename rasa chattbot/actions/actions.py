# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher


class ActionHelloWorld(Action):

    def name(self) -> Text:
        return "action_hello_world"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(text="Hello World!")

        return []

class PizzaOrderForm(Action):

    def name(self) -> Text:
        """Unique identifier of the form"""
        return "get_pizza_order"

    @staticmethod
    def required_slots(tracker: Tracker) -> List[Text]:
        """A list of required slots that the form has to fill"""
        return ["pizza_topping", "pizza_size"]

    def submit(self, dispatcher: CollectingDispatcher,
              tracker: Tracker,
              domain: Dict[Text, Any]) -> List[Dict]:
        """Define what the form has to do after all required slots are filled"""
        pizza_size = tracker.get_slot("pizza_size")
        pizza_topping = tracker.get_slot("pizza_topping")
        print('YOO pizza order form')
        
        dispatcher.utter_message(text=f'Okay Great. Your order is {pizza_size} pizza with {pizza_topping}. Can you confirm please')
        return []