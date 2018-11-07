import json
from watson_developer_cloud import ToneAnalyzerV3, AssistantV1

# credentials to access the APIs
tone_analyzer = ToneAnalyzerV3(
    version='2017-09-21',
    username='e861f592-79c1-4712-8aa3-4e3792531894',
    password='8NB14E2FiFyv',
    url='https://gateway.watsonplatform.net/tone-analyzer/api'
)

text = 'Team, I know that times are tough! Product '\
    'sales have been disappointing for the past three '\
    'quarters. We have a competitive product, but we '\
    'need to do a better job of selling it!'

tone_analysis = tone_analyzer.tone(
    {'text': text},
    'application/json'
).get_result()

tone_analysis['text'] = text
def getSentences(analysis):
    ret = {}
    text = analysis['text']
    if analysis.get('sentences_tone') is not None:
        analysis = analysis['sentences_tone']
        for sentence in analysis:
            curr = sentence['text']
            tones = []
            for s in sentence['tones']:
                tones.append(s['tone_name'])
            ret[curr] = tones
    else:
        analysis = analysis['document_tone']
        tones = []
        for t in analysis['tones']:
            tones.append(t['tone_name'])
        ret[text] = tones
    return ret

tone_analysis = getSentences(tone_analysis)

out_file = open("toneOutput.json", 'w')
out_file.write(json.dumps(tone_analysis, indent=2))


