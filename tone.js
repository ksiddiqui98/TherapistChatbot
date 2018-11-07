var ToneAnalyzerV3 = require('watson-developer-cloud/tone-analyzer/v3')

var toneAnalyzer = new ToneAnalyzerV3({
    version: '2017-09-21',
    username: 'e861f592-79c1-4712-8aa3-4e3792531894',
    password: '8NB14E2FiFyv',
    url: 'https://gateway.watsonplatform.net/tone-analyzer/api'
});

var text = 'Team, I know that times are tough! Product '
+ 'sales have been disappointing for the past three '
+ 'quarters. We have a competitive product, but we '
+ 'need to do a better job of selling it!';



var toneParams = {
    tone_input: { 'text': text },
    content_type: 'application/json'
};

var map = new Map();

  
toneAnalyzer.tone(toneParams, function (error, toneAnalysis) {
    if (error) {
        console.log(error);
    } else { 
        var fs = require("fs");
        fs.writeFile("./tone.json", JSON.stringify(toneAnalysis, null, 2), (err) => {
            if(err) {
                console.error(err);
                return;
            }
            console.log("File has been created.");
        });
    }
});
  