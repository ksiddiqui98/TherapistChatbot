from watson_developer_cloud import AssistantV2
import time

assistant = AssistantV2(
    version='2018-11-08',
    username='b1530d6e-bf39-4e8e-8bda-8cd348f5437f',
    password='ttZyjLhxQpGt',
    url='https://gateway.watsonplatform.net/assistant/api'
)
assistant_id = 'fc12d1d1-4027-4295-ad7a-a0ac1bba7418'

session_id = assistant.create_session(
    assistant_id = assistant_id
).get_result()['session_id']

user_input = ''
current_action = ''

while current_action != 'end_conversation':
    current_action = ''

    response = assistant.message(
        assistant_id,
        session_id,
        input = {
            'text': user_input
        }
    ).get_result()

    if response['output']['generic']:
        print(response['output']['generic'][0]['text'])

    if 'actions' in response['output']:
        if response['output']['actions'][0]['type'] == 'client':
            current_action = response['output']['actions'][0]['name']

    if current_action == 'display_time':
        print('The current time is ' + time.strftime('%I:%M:%S %p') + '.')
    if current_action != 'end_conversation':
        user_input = input('>> ')

assistant.delete_session(
    assistant_id= assistant_id,
    session_id= session_id
)