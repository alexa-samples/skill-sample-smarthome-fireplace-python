# 4. Create the Backend Resources

For this sample you will need backend AWS resources that support the skill. You will create a CloudFormation stack using a provided template that generates the following in your AWS account:

- An IAM Lambda Execution role with a restrictive policy
- A basic AWS Lambda function with triggers configured for Alexa
- A Simple Queue Service (SQS) queue for managing messages for the virtual fireplace
- A Cognito Identity Pool to allow the client web application (the virtual fireplace) to read from the SQS queue

## Deploy the CloudFormation Template

Access the AWS CloudFormation console in your preferred region and load a template file to provision backend resources.

1. Login to the AWS Console for CloudFormation at [https://console.aws.amazon.com/cloudformation/home](https://console.aws.amazon.com/cloudformation/home) (then select the region that is most appropriate for your smart home locale of choice, eg. for North America choose *us-east-1*, for Europe and India choose *eu-west-1* and for Far East choose *us-west-1*).
2. Click the **Create stack** dropdown, and select **With new resources (standard)**.
3. Select **Template is ready** and **Upload a template file**. Click the **Choose file** button and navigate to "template.json" in the _cloudformation_ directory of this repo.
4. Click **Next**.
5. For the **Stack name** on the *Stack Details* page, enter `skill-sample-smarthome-fireplace-python`.
6. In the **AlexaSkillId** field of the *Parameters*, enter the Alexa Skill ID of the previously created skill stored in the **[Alexa Skill Application ID]** section of the `setup.txt` file.
7. Click the **Next** button.
8. On the *Options* page, no changes are needed and you can just click the **Next** button.
9. On the *Review* page, scroll to the bottom and check the **I acknowledge that AWS CloudFormation might create IAM resources.** check box and then click the **Create stack** button.

> The status of the stack should start as `CREATE_IN_PROGRESS` and complete with a couple of minutes. You can view the status of the stack creation on the CloudFormation console.

## Collect the CloudFormation Stack Outputs

After the stack completes, collect the created resource identifiers:

1. When the *skill-sample-smarthome-fireplace-python* stack is created, you will see its *Status* reported as `CREATE_COMPLETE`.
2. From the *Outputs* tab of the stack, collect value of the `FireplaceFunctionLambdaArn` key and store it into the **[AWS Lambda ARN]** section of the `setup.txt` file in your working directory. It will look something like the following: `arn:aws:lambda:region:XXXXXXXXXXXX:function:skill-sample-smarthome-fireplace`.
3. While in the *Outputs* tab, also collect the `FireplaceSqsQueueUrl` value and store it in the **[Amazon SQS Queue Url]** section of the `setup.txt` file.
4. Finally, from the same *Outputs* tab, collect the `FireplaceCognitoIdentityPool` value and store it in the **[Amazon Cognito Identity Pool]** section of the `setup.txt` file.

	```
	[AWS Lambda ARN]
	arn:aws:lambda:region:XXXXXXXXXXXX:function:skill-sample-smarthome-fireplace-python

	[Amazon SQS Queue Url]
	https://sqs.region.amazonaws.com/XXXXXXXXXXXX/FireplaceEventQueue

	[Amazon Cognito Identity Pool]
	region:XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX
	```

Next [5. Create a Security Profile](create-a-security-profile.md)

___
Return to the [Instructions](README.md)