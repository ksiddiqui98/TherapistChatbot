import json
from watson_developer_cloud import ToneAnalyzerV3, AssistantV1

assistant = AssistantV1(
    version='2018-09-20',
    username='b1530d6e-bf39-4e8e-8bda-8cd348f5437f',
    password='ttZyjLhxQpGt',
    url='https://gateway.watsonplatform.net/assistant/api'
)

user_input = ''
context = {}
current_action = ''

while current_action != 'EXIT':
    response = assistant.message(
        workspace_id='1e7277b6-c5ec-4e49-b872-4f4a4caf5d25',
        input={
            'text': user_input
        }
    ).get_result(),
    context = context

    # If an intent was detected, print it to the console. Assumes a single text response.
    if response['intents']:
        print('Detected intent: #' + response['intents'][0]['intent'])

    # Print the output from dialog, if any.
    if response['output']['generic']:
        print(response['output']['generic'][0]['text'])

    context = response['context']

    # Prompt for next round of input.
    user_input = input('>> ')


#out_file = open("conversation.json", 'w')
#out_file.write(json.dumps(response, indent=2))
