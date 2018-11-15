## happy path
* request_contact
    - contact_form
    - form{"name": "contact_form"}
    - form{"name": null}
    - utter_slots_values
* thanks
    - utter_thanks

## greet
* greet
    - utter_name
* my_name_is{"name":"Pierre"}
    - utter_greet

## name
* my_name_is{"name":"Pierre"}
    - utter_greet


### request_contact
* request_contact
    - contact_form
    - form{"name":"contact_form"}
    - slot{"requested_slot":"message"}
* form: inform{"message":"proposition"}
    - form: contact_form
    - slot{"message":"proposition"}
    - slot{"requested_slot":"email"}
* form: inform{"email":"marakrian@gmail.com"}
    - form: contact_form
    - slot{"email":"marakrian@gmail.com"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - utter_slots_values
* thanks
    - utter_thanks