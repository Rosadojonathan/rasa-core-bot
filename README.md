# rasa-core-bot
POC of a RASA Core bot with some basic intent/form/action workflow

![chatbot]('./chatbot.jpg')

## What is RASA?
The **Rasa stack** is made of two libraries, RASA NLU and RASA Core.

**RASA NLU** is an open source NLP (Natural Language Processing) tool for intent classification and entity extraction. Rasa is a set of high level APIs for building your own language parser using existing NLP and ML libraries such as Spacy, Sklearn, Mitie and TenserFlow.

**RASA Core** is an open source tool to build the dialogue flow of your bots with full control.

## Why RASA?

- Runs locally, no need to send https requests and no server round trips required. 
- Customizable : dive into the code and tune models any way you want to get higher accuracy
- Open Source : no vendor lock-in. Can be used in commercial projects as well. You don't depend on Facebook or Google.

## How to run?
`pip install -r requirements.txt`
`make train-nlu` &&
`make train-core`&&
`make run` || `make api` to use it as an API for your website.
