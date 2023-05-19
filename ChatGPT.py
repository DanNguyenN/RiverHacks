import os
import config
import requests
import json

def chat_gpt(text):
  response = requests.post(
    "https://api.respell.ai/v1/run",
    headers={
      # This is your API key
      'Authorization': config.RespellAPI,
      'Accept': 'application/json',
      'Content-Type': 'application/json'
    },
    data=json.dumps({
      "spellId": "w-l-6DvhFI0GRacjxJYqr",
      # This field can be omitted to run the latest published version
      "spellVersionId": 'V2fPoHAjQRrOoj5bs24A4',
      # Fill in dynamic values for each of your 2 input blocks
      "inputs": {
        "input": text,
        "input_2": '...'
      }
    }),
  )
  return response.json()['outputs']['output']
