from watson_developer_cloud import ToneAnalyzerV3, AssistantV1

# credentials to access the APIs
tone_analyzer = ToneAnalyzerV3(
    version='2017-09-21',
    username='e861f592-79c1-4712-8aa3-4e3792531894',
    password='8NB14E2FiFyv',
    url='https://gateway.watsonplatform.net/tone-analyzer/api'
)
assistant = AssistantV1(
    version='2018-09-20',
    username='b1530d6e-bf39-4e8e-8bda-8cd348f5437f',
    password='ttZyjLhxQpGt',
    url='https://gateway.watsonplatform.net/assistant/api'
)
