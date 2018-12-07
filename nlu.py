import json
from watson_developer_cloud import NaturalLanguageUnderstandingV1
from watson_developer_cloud.natural_language_understanding_v1 \
    import Features, EmotionOptions, KeywordsOptions, SentimentOptions, CategoriesOptions

natural_language_understanding = NaturalLanguageUnderstandingV1(
    version='2018-03-16',
    username='63a8e859-3e1a-49b9-87e9-49da3f47c68e',
    password='oQWwNPacKhRD',
    url='https://gateway.watsonplatform.net/natural-language-understanding/api'
)

def getSentimentScore():
    response = natural_language_understanding.analyze(
        text="I have way too many exams this week and I'm stressed out",
        features=Features(sentiment=SentimentOptions())).get_result()

    sentimentScore = response['sentiment']['document']['score']
    return sentimentScore

def getEmotions():
    response = natural_language_understanding.analyze(
        text="I have way too many exams this week and I'm stressed out",
        features=Features(emotion=EmotionOptions())).get_result()

    allEmotions = response['emotion']['document']['emotion']
    emotions = {}
    for e in allEmotions:
        if allEmotions[e] > .3:
            emotions = {e:allEmotions[e]}

    return emotions

score = getSentimentScore()
e = getEmotions()

print("Sentiment Score: ", score)
print("Emotions: ", e)


