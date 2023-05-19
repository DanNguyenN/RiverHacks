# RiverHacks
24/7 Alexa-inspired chatbot address mental health concerns and supportive peers network for ACC students

## Inspiration

We were inspired not only by the prompt - creating a product which addresses student mental health issues - but also by our personal experiences with friends and family members having mental health concerns.

## What it does

While a chatbot cannot fully replace human-to-human communication, we created RiverBOT to be able to address mental health concerns of any ACC student in real-time on a 24/7 basis. We also match certified and trained Riverbats students to student in crises.

## How we built it

We used the Flask web framework with an embedded ChatGPT and Azure API for the backend. We used Figma to design the front end.

## Challenges we ran into

We’ve had many disagreements about how to format the presentation of the project, but we were able to resolve most of them to create a coherent presentation of the project.

We attempted to deploy the project on the cloud so everyone can test it. But Azure failed to provision VMs for it and we ran out of time

## Accomplishments that we're proud of

The entire project is something we’re pretty proud of. Of all the things which could’ve gone wrong but didn’t, this is an amazing feat for all three of us.

## What we learned

How to do prompt engineering and ChatGPT in general.
Using Azure Services in order to make application fully working

## What's next for RiverBOT

So far we have a working backend and front end, but it is not connected togheter. We hope to fully integrate it to serve ACC Riverbats

# TO USE THE PROJECT
You have to create a file call config.py and replace key and endpoint. API used are Respell, Azure, and OpenAI
```
RespellAPI = 'key'
AzureSpeechKey = 'key'
AzureEndpoint = 'endpoint'
OpenAIapi = "key"
```
