var prompt = require('prompt-sync')();
var AssistantV1 = require('watson-developer-cloud/assistant/v1');

var assistant = new AssistantV1({
    version: '2018-09-20',
    username: 'b1530d6e-bf39-4e8e-8bda-8cd348f5437f',
    password: 'ttZyjLhxQpGt',
    url: 'https://gateway.watsonplatform.net/assistant/api'
});

var workspace_id = '1e7277b6-c5ec-4e49-b872-4f4a4caf5d25';

assistant.message({
    workspace_id: workspace_id
}, processResponse);

// Process the service response.
function processResponse(err, response) {
    if (err) {
        console.error(err); // something went wrong
        return;
    }

    // If an intent was detected, log it out to the console.
    if (response.intents.length > 0) {
        console.log('Detected intent: #' + response.intents[0].intent);
    }

    // Display the output from dialog, if any. Assumes a single text response.
    if (response.output.generic.length != 0) {
        console.log(response.output.generic[0].text);
    }


    // Prompt for the next round of input.
    var newMessageFromUser = prompt('>> ');
    // Send back the context to maintain state.
    assistant.message({
        workspace_id: workspace_id,
        input: { text: newMessageFromUser },
        context: response.context,
    }, processResponse)
}
