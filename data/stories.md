## happy path
* request_contact
    - contact_form
    - form{"name": "contact_form"}
    - form{"name": null}
    - utter_slot_values
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

## insulting
* insulting
    - utter_no_insults_here

## thanks
* thanks
    - utter_thanks

## ok
* ok
    - utter_anything_else
* rien
    - utter_suit_yourself

## rien
* rien
    - utter_suit_yourself

## goodbye
* goodbye
    - utter_goodbye

## request_joke
* request_joke
    - action_joke_generator

## request_contact
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
    - action_restart
* ok
 - utter_anything_else
* thanks
    - utter_thanks

## ask_question
* request_question
    - question_answerer_form
    - form{"name":"question_answerer_form"}
    - slot{"requested_slot":"question"}
* form: inform{"question":"mon_job"}
    - form: question_answerer_form
    - slot{"question":"mon_job"}
    - form{"name":null}
    - slot{"requested_slot":null}
    - action_restart
* ok
 - utter_anything_else
* thanks
    - utter_thanks

## ask_two_questions
* request_question
    - question_answerer_form
    - form{"name":"question_answerer_form"}
    - slot{"requested_slot":"question"}
* form: inform{"question":"mon_job"}
    - form: question_answerer_form
    - slot{"question":"mon_job"}
    - form{"name":null}
    - slot{"requested_slot":null}
    - action_restart
* ok
 - utter_anything_else
* request_question
    - question_answerer_form
    - form{"name":"question_answerer_form"}
    - slot{"requested_slot":"question"}
* form: inform{"question":"mon_job"}
    - form: question_answerer_form
    - slot{"question":"mon_job"}
    - form{"name":null}
    - slot{"requested_slot":null}
    - action_restart
* ok
 - utter_anything_else


## direct_question_respond_form
* question{"mon_job":"Tech Marketer"}
    - action_simple_answer