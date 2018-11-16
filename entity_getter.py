from rasa_core.trackers import DialogueStateTracker
from enum import Enum
from typing import Generator, Dict, Text, Any, Optional, Iterator
from typing import List
from rasa_core.slots import Slot
from rasa_core import events
from rasa_core.actions.action import ACTION_LISTEN_NAME
from rasa_core.conversation import Dialogue
from rasa_core.events import (
    UserUttered, ActionExecuted,
    Event, SlotSet, Restarted, ActionReverted, UserUtteranceReverted,
    BotUttered, Form)

class EntityGetter(DialogueStateTracker):
    # @classmethod
    # def from_dict(cls,
    #               sender_id: Text,
    #               events_as_dict: List[Dict[Text, Any]],
    #               slots: List[Slot],
    #               max_event_history: Optional[int] = None
    #               ) -> 'DialogueStateTracker':
    #     """Create a tracker from dump.
    #     The dump should be an array of dumped events. When restoring
    #     the tracker, these events will be replayed to recreate the state."""

    #     evts = events.deserialise_events(events_as_dict)
    #     return cls.from_events(sender_id, evts, slots, max_event_history)

    # @classmethod
    # def from_events(cls,
    #                 sender_id: Text,
    #                 evts: List[Event],
    #                 slots: List[Slot],
    #                 max_event_history: Optional[int] = None
    #                 ):
    #     tracker = cls(sender_id, slots, max_event_history)
    #     for e in evts:
    #         tracker.update(e)
    #     return tracker

    # def __init__(self, sender_id, slots,
    #              max_event_history=None):
    #     """Initialize the tracker.
    #     A set of events can be stored externally, and we will run through all
    #     of them to get the current state. The tracker will represent all the
    #     information we captured while processing messages of the dialogue."""

    #     # maximum number of events to store
    #     self._max_event_history = max_event_history
    #     # list of previously seen events
    #     self.events = self._create_events([])
    #     # id of the source of the messages
    #     self.sender_id = sender_id
    #     # slots that can be filled in this domain
    #     self.slots = {slot.name: copy.deepcopy(slot) for slot in slots}

    #     ###
    #     # current state of the tracker - MUST be re-creatable by processing
    #     # all the events. This only defines the attributes, values are set in
    #     # `reset()`
    #     ###
    #     # if tracker is paused, no actions should be taken
    #     self._paused = None
    #     # A deterministically scheduled action to be executed next
    #     self.followup_action = ACTION_LISTEN_NAME  # type: Optional[Text]
    #     self.latest_action_name = None
    #     # Stores the most recent message sent by the user
    #     self.latest_message = None
    #     self.latest_bot_utterance = None
    #     self._reset()
    #     self.active_form = {}

    def get_latest_entity(self):
        return (x.get('entity') for x in self.latest_messages.entities)