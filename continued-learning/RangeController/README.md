# Smart Home API Alexa.RangeController Recipe

## Prerequisite

**You should have completed the [Virtual Fireplace](https://github.com/alexa/skill-sample-smarthome-fireplace-python) tutorial before continuing with this recipe.**

## About this Recipe

This add-on builds on top of an Alexa-enabled virtual fireplace. It adds a new capability to the fireplace through the Alexa Smart Home SKill API. A device, or _endpoint_, can implement the combination of capability interfaces that best represent its features. For example, a light that can be turned on and off and dimmed might implement two interfaces: PowerController and BrightnessController. A similar light that has these two features and also supports tunable white light might also implement ColorTemperatureController.

In this example, you'll use the [`Alexa.RangeController`](https://developer.amazon.com/en-US/docs/alexa/device-apis/alexa-rangecontroller.html) (RangeController) interface to change the type of number of burners your virtual fireplace uses. When you use the RangeController interface, the voice interaction model is already built for you, so you won't need to worry about setting up invocation phrases like "Alexa, set the fireplace to X," and you can instead focus on the logic that brings your fireplace to life.

When you've completed the steps in this recipe, you'll be able to adjust the width of flame (i.e., the _range_) to "low", "normal", or "high", or set the number of burners to a value of 1, 2, or 3 (_low_, _normal_, and _high_, respectively). Let's get started.

![](./img/fireplace-ranges.gif)

## Step 1. Start your virtual fireplace client

1. From the command line, navigate to the client directory of your *skill-sample-smarthome-fireplace-python* directory. Remember, this was the directory created when you completed [the base project that this recipe builds on](https://github.com/alexa/skill-sample-smarthome-fireplace-python).
2. Run the command `npm run start` to start the client.
3. Once started, visit [http://localhost:9000/](http://localhost:9000) to view the virtual fireplace.
4. Leave the web page open and the client running in the background and proceed with the next step.

## Step 2. Add support for the Alexa.RangeController interface to your AWS Lambda project

When your Lambda skill was created in the "Create the Backend Resources" step of [the previous tutorial](https://github.com/alexa/skill-sample-smarthome-fireplace-python), a __capabilities__ folder was created in your Lambda deployment package. Let's add a new capability to your virtual fireplace by copying the contents of [RangeController.json](./capabilities/RangeController.json) and pasting to a new file in your Lambda's __capabilities__ folder:

Right-click on "capabilities", the select "New File." Name the file "RangeController.json", and paste the contents you just copied. Save the file when you're done.

![](./img/new-file.png)

## Step 3. Add the RangeController capability to your virtual fireplace

Update "index.py" to handle `Alexa.RangeController` requests from your skill. Locate the `# Flatten capabilities into a single list` comment and add the following code just above it:

```
...

## RangeController
range_controller_capabilities = load_capability_definition("RangeController")
capabilities.append(range_controller_capabilities)

# Flatten capabilities into a single list
capabilities = list(itertools.chain.from_iterable(capabilities))
...        
```

When you've added the code, it should look like the following:

![](./img/add-range-controller.png)

## Step 4. Add code to handle the `Alexa.RangeController` namespace

When a user of your skill interacts with your virtual fireplace, a JSON request with a "namespace" is sent to your skill. Search the code in "index.py" to find `if namespace == 'Alexa.PowerController':`. This code block handles the `Alexa.PowerController` namespace, which you'll remember can control the power of your virtual fireplace.

There are placeholder comments for various capabilities. Look for the code block

```
if namespace == 'Alexa.RangeController':
    # Continue your learning!
    # You can implement Alexa.RangeController for your virtual fireplace via 
    #   https://github.com/alexa/skill-sample-smarthome-fireplace-python/tree/main/continued-learning/RangeController
    pass
```

and replace it with the following:

```
if namespace == 'Alexa.RangeController':
    endpoint_id = request['directive']['endpoint']['endpointId']
    token = request['directive']['endpoint']['scope']['token']
    correlation_token = request['directive']['header']['correlationToken']

    if name == 'SetRangeValue':
        
        range_value = request['directive']['payload']['rangeValue']
        logger.info('+++++ range_value')
        logger.info(range_value)
        
        message = {
            'endpointId':endpoint_id, 
            'namespace':'Alexa.RangeController', 
            'name':'range', 
            'value':range_value
        }
        
        if send_device_state_message(message):
            response = AlexaResponse({
                'correlationToken': correlation_token,
                'token': token,
                'endpointId': endpoint_id
            })
            
            response.add_context_property({
                'namespace':'Alexa.RangeController', 
                'instance':'Fireplace.Burners', 
                'name': 'rangeValue', 
                'value': range_value
            })
            response = response.get()
            return send_response(response)
    else:
        response = AlexaResponse({
            'name': 'ErrorResponse',
            'payload': {
                'type': 'INVALID_VALUE',
                'message': 'Range setting not handled by fireplace'
            }
        }).get()
        return send_response(response)
```

Note that Python is sensitive to proper indentation. Make sure the code block you pasted is indented properly, and deploy index.py by clicking the "Deploy" button:

![](./img/deploy.png)

## Step 5. Send a Smart Home test event

First, ensure that you have deployed your changes in "index.py". Then, add a test event for the `RangeController` directive to your Lambda function.

1. On the function page for _skill-sample-smarthome-fireplace-python_, select the **Select a test event** dropdown from the top menu of the function and click **Configure test events**.

    ![](./img/test-event.png)

2. In the dialog that opens, leave **Create new test event** selected and leave the default template.
3. For the _Event name_ enter: `directiveRangeController`.
4. Copy and paste the contents of [RangeController.request.json](./events/RangeController.request.json) into the text field at the bottom of the dialog replacing its contents.
5. Click **Create**.
6. With the *directiveRangeController* test selected in the dropdown, click **Test**.
7. Open the **Execution result** details to inspect the result and notice that your handler now a response where the `rangeValue` has a value of _3_.

If your virtual fireplace client is running, you'll notice that the flame radius has expanded as if another burner was turned on.

![](./img/fireplace-range-high.png)
 
## Step 6. Notify Alexa that your virtual fireplace has a new capability

There are a few ways to notify Alexa that your virtual fireplace has a new capability. One such way is using a proactive notification, which sends an updated list of capabilities from your device to [the Alexa Event Gateway](https://developer.amazon.com/en-US/docs/alexa/smarthome/send-events-to-the-alexa-event-gateway.html). Another way, and the one used in this recipe, is to simply re-discover your devices so that a discovery event can be sent to your skill and receive an updated list of capabilities in return.

Rediscover your devices:

1. Visit your Devices list at [https://alexa.amazon.com/spa/index.html#appliances](https://alexa.amazon.com/spa/index.html#appliances). You may need to login with your Amazon account.
2. Scroll to the bottom of your list and click the "Discover" button. 

![](./img/discover.png)

3. After 20-30 seconds, your devices will be rediscovered, and the capability you just added will now be available to you.

![](./img/discovering.png)

## Step 7. Test your virtual fireplace's new capability

You have now added a capability to your virtual fireplace, and a handler to handle incoming requests to change the number of burners used to create the virtual flame. Let's interact with your fireplace to see the RangeController in action. You can use an Alexa device, or the Alexa Developer Console:

### Option 1: Control your virtual fireplace through an Alexa device

1. Say the following: `Alexa, set the fireplace to high`

    If successful, Alexa should respond with an "OK", and in your browser you should notice the flame change to a wider flame that takes up most of the base of your fireplace.

2. Type or say the following: `Alexa, set the fireplace to 2`

    If successful, Alexa should respond with an "OK", and in your browser you should notice the flame return to its original state. You could also say `Alexa, set the fireplace to normal`, to achieve the same result.

3. Type or say the following: `Alexa, set the fireplace to low`

    If successful, Alexa should respond with an "OK", and in your browser you should notice the flame change to its lowest range, which is a flame mostly contained within the logs.

If you don't notice a change in your fireplace, Alexa may respond with _"There was a problem with the requested skill's response"_. If your skill does not work correctly, you will need to review your logs and troubleshoot.

### Option 2: Send an utterance to Alexa using the Alexa Developer Console

1. Navigate to the ASK developer console at [https://developer.amazon.com/alexa/console/ask](https://developer.amazon.com/alexa/console/ask) and select the *Fireplace* skill that you created [the previous tutorial](https://github.com/alexa/skill-sample-smarthome-fireplace-python).

2. Open the **Test** tab from the top menu.

3. Type or say the following: `set the fireplace to high`

    If successful, Alexa should respond with an "OK", and in your browser you should notice the flame change to a wider flame that takes up most of the base of your fireplace.

4. Type or say the following: `set the fireplace to 2`

    If successful, Alexa should respond with an "OK", and in your browser you should notice the flame return to its original state. You could also say `Alexa, set the fireplace to normal`, to achieve the same result.

5. Type or say the following: `set the fireplace to low`

    If successful, Alexa should respond with an "OK", and in your browser you should notice the flame change to its lowest range, which is a flame mostly contained within the logs.

If you don't notice a change in your fireplace, Alexa may respond with _"There was a problem with the requested skill's response"_. If your skill does not work correctly, you will need to review your logs and troubleshoot.

## Congratulations

Congratulations! You have implemented `Alexa.RangeController` into your virtual fireplace, and can change the width of flame your fireplace produces. Be sure to check out other capabilities for your fireplace via the following recipes:

* [Change the flame type with `Alexa.ModeController`](/continued-learning/ModeController)
* [Change the color of the flame with `Alexa.ColorController`](/continued-learning/ColorController)

## Resources

### Documentation

[Request and Response JSON Reference](https://developer.amazon.com/docs/custom-skills/request-and-response-json-reference.html)

[Alexa.RangeController Interface](https://developer.amazon.com/en-US/docs/alexa/device-apis/alexa-rangecontroller.html)

### Community

[Amazon Developer Forums](https://forums.developer.amazon.com/spaces/165/index.html)

[Alexa Skills - User Voice](https://alexa.uservoice.com)

## License

This library is licensed under the Amazon Software License.
