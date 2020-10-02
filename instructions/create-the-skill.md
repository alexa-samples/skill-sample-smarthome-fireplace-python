# 3. Create the Skill

In this step you will create an Alexa skill that will respond to Smart Home commands.

## Create a Skill using the Alexa Skills Kit Developer Console

1. In a web browser open the *Alexa Skills Kit Developer Console* at [https://developer.amazon.com/alexa/console/ask](https://developer.amazon.com/alexa/console/ask). If not already authenticated, you may have to sign in with your Amazon Developer Account.
2. Click the **Create Skill** button.
3. For the _Skill name_, enter `Fireplace` (or a proper translation if you want to use another locale).
4. In _Default language_ you'll see **English (US)**, leave it as is or change it to your preferred locale. 
5. Under _Choose a model to add to your skill_ select the **Smart Home** model. 
6. Under _Choose a method to host your skill's backend resources_, **Provision your own** will be automatically selected.
7. Back at the top of the page, click the **Create skill** button.
8. You will see the Skill ID that was generated for your skill in the middle of the screen. Click on **Copy to clipboard**
9. Using a text editor, open the `setup.txt` file in your working directory `instructions` folder.
10. Paste the copied Skill ID value in step 6 into the **[Alexa Skill Application ID]** section overwriting the placeholder.

	```
	[Alexa Skill Application ID]
	amzn1.ask.skill.XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX
	```

	> You will use the `setup.txt` file to collect the required ARNs, Credentials, IDs, & URLs.

11. Leave this tab open. You will come back to it soon to fill out the **Default endpoint** value. 

## Checkpoint
- You should have a folder called *skill-sample-smarthome-fireplace-python* that contains the sample code with the README.md file at the root.
- You should have a skill with the Smart Home model and should have captured the Alexa Skill Application ID generated during skill creation into the `setup.txt` file. 

Next to Step [4. Create the Backend Resources](create-the-backend-resources.md)

___
Return to the [Instructions](README.md)
