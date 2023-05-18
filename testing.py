import config
import requests
import json

filename = 'test.mp3'

with open(filename, 'rb') as file:
    audio_data = file.read()

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
    "spellVersionId": 'rWfZwDXv--SjhzUQXDKXO',
    # Fill in dynamic values for each of your 2 input blocks
    "inputs": {
      "input_2": 'Example text',
      "input": 'Hello World!',
    }
  }),
)


print(response.json())