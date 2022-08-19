 Invoking a Lambda function without an input event
  $ sam local invoke "HelloWorldFunction"

  Invoking a Lambda function using an event file
  $ sam local invoke "HelloWorldFunction" -e event.json

  Invoking a Lambda function using input from stdin
  $ echo '{"message": "Hey, are you there?" }' | sam local invoke "HelloWorldFunction" --event - 

  sam local invoke "LogUsersFunction" -e event.json