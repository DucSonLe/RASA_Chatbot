# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet

class ActionSaveCustInfo(Action):
    def name(self) -> Text:
        return "action_save_cust_info"

    async def run(
        self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]
    ) -> List[Dict[Text, Any]]:

        user_id = (tracker.current_state())["sender_id"]
        print(user_id)
        customer_gender = next(tracker.get_latest_entity_values("customer_gender"), None)
        customer_name = next(tracker.get_latest_entity_values("customer_name"), None)
        return [SlotSet("customer_gender", customer_gender), SlotSet("customer_name", customer_name)]
