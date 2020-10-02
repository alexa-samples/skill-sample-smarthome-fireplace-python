# 5. Create a Security Profile

For the sample environment, a development security profile will be used for configuring [Account Linking](https://developer.amazon.com/en-US/docs/alexa/account-linking/understand-account-linking.html), which is required for the Smart Home model. We'll use [Login with Amazon](https://developer.amazon.com/docs/login-with-amazon/documentation-overview.html) (LWA) for this demo, but you may have your own OAuth service that should be used in order to enable your customers to link their accounts with Alexa.

> If you already have a valid `Skill Sample` security profile created from a previous sample, you can reuse that profile and skip creating and configuring a new security profile. You can see your created profiles [here](https://developer.amazon.com/settings/console/securityprofile/overview.html).

## Create a Security Profile

To facilitate account linking in the sample, a security profile is needed to generate a `Client ID` and `Client Secret` to use during the configuration of the Alexa skill.

1. In your web browser, go to the Security Profile creation page at [https://developer.amazon.com/iba-sp/create-security-profile.html](https://developer.amazon.com/iba-sp/create-security-profile.html). You can also access this page by navigating to then Amazon Developer Console and going to the *Settings > Security Profiles* section.

	> You will need to authenticate with your AWS credentials to access the Amazon Developer Console.
	
2. On the *Security Profile Management* page, enter `Skill Sample` for the Security Profile Name.
3. For the *Security Profile Description* enter `A security profile for Alexa Skill samples`.
4. Click **Save** on the *Security Profile Management* page.
5. On the *Web Settings* tab, copy the displayed Client ID and Client Secret values of the *Skill Sample - Security Profile* and save them to the `setup.txt` file in the `instructions` directory of the sample replacing the format example entries for **[Security Profile Client ID]** and **[Security Profile Client Secret]** respectively.

	```
	[Security Profile Client ID]
	amzn1.application-oa2-client.XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX

	[Security Profile Client Secret]
	XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
	```

Further configuration of the Security Profile Allowed Return URLs will be done later in this tutorial, during configuration of the Alexa Skill Account Linking.

## Checkpoint
You should now have what you need for identifying the application to Amazon:

- A created `Skill Sample` security profile
- Valid `Client ID` and `Client Secret` credentials for our skill saved into `setup.txt`

Next to Step [6. Configure the Skill](configure-the-skill.md)

___
Return to the [Instructions](README.md)
