# 11. Continued Learning and Clean Up

Congratulations! You have built a virtual fireplace using the Alexa Smart Home API. Although this tutorial only uses the `Alexa.PowerController` interface to control the power state of the fireplace, you can add additional functionality to your virtual fireplace through the following Smart Home API directives:

* [Change the flame type with `Alexa.ModeController`](/continued-learning/ModeController)
* [Change the number of burners in your fireplace with `Alexa.RangeController`](/continued-learning/RangeController)
* [Change the color of the flame with `Alexa.ColorController`](/continued-learning/ColorController)

Each of these recipes build on this tutorial, and you do not have to do them in any particular order.

If you're finished experimenting with the virtual fireplace, now would be a great time to clean up your AWS resources and avoid incurring any further charges.

## Clean Up

To remove the sample and cleanup the backend:

1. Close any open instance of `setup.txt`
2. Delete the cloned repository from your computer
3. From the Alexa Developer Console, select and then delete the `Fireplace` skill.
4. In the CloudFormation console, select `skill-sample-smarthome-fireplace-python` and then **Delete Stack** from the Actions dropdown.

## Congrats, and well done!!!

___
Return to the [Instructions](README.md)
