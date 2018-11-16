# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import typing
from typing import Dict, Text, Any, List, Union

from rasa_core_sdk import ActionExecutionRejection
from rasa_core_sdk.forms import FormAction, REQUESTED_SLOT
from rasa_core_sdk.events import SlotSet

from botactions.send_email import send_email 

if typing.TYPE_CHECKING:
    from rasa_core_sdk import Tracker
    from rasa_core_sdk.executor import CollectingDispatcher


class ContactForm(FormAction):
    """Example of a custom form action"""

    def name(self):
        # type: () -> Text
        """Unique identifier of the form"""

        return "contact_form"

    @staticmethod
    def required_slots(tracker):
        # type: (Tracker) -> List[Text]
        """A list of required slots that the form has to fill"""

        return ["message","email"]

    def slot_mappings(self):
        # type: () -> Dict[Text: Union[Dict, List[Dict]]]
        """A dictionary to map required slots to
            - an extracted entity
            - intent: value pairs
            - a whole message
            or a list of them, where a first match will be picked"""

        return {
                "email": [self.from_entity(entity='email'),
                                self.from_text()],
                "message": [self.from_text()]}


    def validate(self, dispatcher, tracker, domain):
        # type: (CollectingDispatcher, Tracker, Dict[Text, Any]) -> List[Dict]
        """Validate extracted requested slot
            else reject the execution of the form action
        """
        # extract other slots that were not requested
        # but set by corresponding entity
        slot_values = self.extract_other_slots(dispatcher, tracker, domain)

        # extract requested slot
        slot_to_fill = tracker.get_slot(REQUESTED_SLOT)
        if slot_to_fill:
            slot_values.update(self.extract_requested_slot(dispatcher,
                                                           tracker, domain))
            if not slot_values:
                # reject form action execution
                # if some slot was requested but nothing was extracted
                # it will allow other policies to predict another action
                raise ActionExecutionRejection(self.name(),
                                               "Failed to validate slot {0} "
                                               "with action {1}"
                                               "".format(slot_to_fill,
                                                         self.name()))

        # we'll check when validation failed in order
        # to add appropriate utterances
        # for slot, value in slot_values.items():
        #     if slot == 'cuisine':
        #         if value.lower() not in self.cuisine_db():
        #             dispatcher.utter_template('utter_wrong_cuisine', tracker)
        #             # validation failed, set slot to None
        #             slot_values[slot] = None

        #     elif slot == 'num_people':
        #         if not self.is_int(value) or int(value) <= 0:
        #             dispatcher.utter_template('utter_wrong_num_people',
        #                                       tracker)
        #             # validation failed, set slot to None
        #             slot_values[slot] = None

        #     elif slot == 'outdoor_seating':
        #         if isinstance(value, str):
        #             if 'out' in value:
        #                 # convert "out..." to True
        #                 slot_values[slot] = True
        #             elif 'in' in value:
        #                 # convert "in..." to False
        #                 slot_values[slot] = False
        #             else:
        #                 dispatcher.utter_template('utter_wrong_outdoor_seating',
        #                                           tracker)
        #                 # validation failed, set slot to None
        #                 slot_values[slot] = None

        # validation succeed, set the slots values to the extracted values
        return [SlotSet(slot, value) for slot, value in slot_values.items()]

    def submit(self, dispatcher, tracker, domain):
        # type: (CollectingDispatcher, Tracker, Dict[Text, Any]) -> List[Dict]
        """Define what the form has to do
            after all required slots are filled"""

        # utter submit template
        send_email(tracker.get_slot('email'),tracker.get_slot('message'))
        
        dispatcher.utter_template('utter_message_sent', tracker, email=tracker.get_slot('email'))
        return []


class QuestionAnswerer(FormAction):
    def name(self):
        return "question_answerer_form"
    
    @staticmethod
    def required_slots(tracker):
        return ["question"]
    
    def slot_mappings(self):
        return {
            "question": [self.from_entity(entity='mon_job',intent="question"),
            self.from_entity(entity='mon_entreprise',intent="question")]


        }

    def validate(self, dispatcher, tracker, domain):
        
        slot_values = self.extract_other_slots(dispatcher, tracker, domain)

        # extract requested slot
        slot_to_fill = tracker.get_slot(REQUESTED_SLOT)
        if slot_to_fill:
            slot_values.update(self.extract_requested_slot(dispatcher,
                                                           tracker, domain))
            if not slot_values:
                # reject form action execution
                # if some slot was requested but nothing was extracted
                # it will allow other policies to predict another action
                raise ActionExecutionRejection(self.name(),
                                               "Failed to validate slot {0} "
                                               "with action {1}"
                                               "".format(slot_to_fill,
                                                         self.name()))
        for slot, value in slot_values.items():
            if slot == 'question':
                if 'market' in value.lower():
                    # validation failed, set slot to None
                    slot_values[slot] = "mon_job"

            
                elif "Maestro" in value:
                    slot_values[slot] = "mon_entreprise"

        # validation succeed, set the slots values to the extracted values
        return [SlotSet(slot, value) for slot, value in slot_values.items()]

    def submit(self,dispatcher, tracker, domain):
        print('Printing question slot : {}'.format(tracker.get_slot("question")))
        explanation = "utter_explanation_{}".format(tracker.get_slot('question'))
        print('explanation is ' + explanation)
        dispatcher.utter_template(explanation,tracker)
        return []