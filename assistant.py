from watson_developer_cloud import AssistantV2, NaturalLanguageUnderstandingV1, WatsonApiException
from watson_developer_cloud.natural_language_understanding_v1 \
    import Features, EmotionOptions, SentimentOptions
import time

natural_language_understanding = NaturalLanguageUnderstandingV1(
    version='2018-03-16',
    username='63a8e859-3e1a-49b9-87e9-49da3f47c68e',
    password='oQWwNPacKhRD',
    url='https://gateway.watsonplatform.net/natural-language-understanding/api'
)

assistant = AssistantV2(
    version='2018-11-08',
    username='b1530d6e-bf39-4e8e-8bda-8cd348f5437f',
    password='ttZyjLhxQpGt',
    url='https://gateway.watsonplatform.net/assistant/api'
)
assistant_id = '83f6f620-47c4-40a2-a002-f59644add9b9'

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

    if current_action != 'end_conversation':
        user_input = input('>> ')
        try:
            features = natural_language_understanding.analyze(
                text=user_input,
                features=Features(sentiment=SentimentOptions(), emotion=EmotionOptions())
            ).get_result()
            print(user_input)
            if features.get('sentiment') is not None:
                sentimentScore = features['sentiment']['document']['score']
                print("(Sentiment Score:", sentimentScore, ")")
            if features.get('emotion') is not None:
                allEmotions = features['emotion']['document']['emotion']
                emotions = {}
                for e in allEmotions:
                    if allEmotions[e] > .3:
                        emotions = {e: allEmotions[e]}

                print("(Emotions:", emotions,  ")")
        except WatsonApiException as e:
            continue


assistant.delete_session(
    assistant_id= assistant_id,
    session_id= session_id
)

#get emotions and sentiment score from text
def getFeatures():
    response = natural_language_understanding.analyze(
        text="I have way too many exams this week and I'm stressed out",
        features=Features(sentiment=SentimentOptions(), emotion = EmotionOptions())
    ).get_result()

    sentimentScore = response['sentiment']['document']['score']
    allEmotions = response['emotion']['document']['emotion']
    emotions = {}
    for e in allEmotions:
        if allEmotions[e] > .3:
            emotions = {e: allEmotions[e]}

    print("Sentiment Score: ", sentimentScore)
    print("Emotions: ", emotions)

#getFeatures()