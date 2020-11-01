# 2. Get the Sample

Follow either of the steps below to get the sample code. 

## Option 1: Clone the Sample using Git

1. Run the following command to clone the sample:
```
git clone git@github.com:alexa/skill-sample-smarthome-fireplace-python.git
```

2. Once the clone is complete, you should have a folder named *skill-sample-smarthome-fireplace-python* in your working directory.

## Option 2: Download the Sample Code from GitHub

Download the zipped sample code.

1. Download the sample from [https://github.com/alexa/skill-sample-smarthome-fireplace-python/archive/master.zip](https://github.com/alexa/skill-sample-smarthome-fireplace-python/archive/master.zip).
2. Unzip the contents of `skill-sample-smarthome-fireplace-python.zip`.


## Checkpoint
- You should have a folder on your working directory like *skill-sample-smarthome-fireplace-python* that contains the sample code with the `README.md` file at the root.

The sample code project structure looks like the following:

```
/client
	Contains the client script for interacting with the SQS Queue.
/cloudformation
	Contains the provisioning template for setting up backend resources.
/instructions
	The instructions for implementing this sample.
/lambda
	The source code for the Lambda skill handler.
README.md
	The readme for this sample.
```

Next to Step [3. Create the Skill](create-the-skill.md)

___
Return to the [Instructions](README.md)
