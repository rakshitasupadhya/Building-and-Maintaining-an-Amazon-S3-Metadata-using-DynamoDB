# Building-and-Maintaining-an-Amazon-S3-Metadata-using-DynamoDB
This is a demonstration on maintaining metadata of S3 files in DynamoDB using Lambda

# Architecture
<img width="452" alt="image" src="https://github.com/rakshitasupadhya/Building-and-Maintaining-an-Amazon-S3-Metadata-using-DynamoDB/assets/107621546/fe1477de-3159-494b-8840-9c48ba7b2678">


# Implementation
1. Create IAM Role for Lambda with policies- DynamoDB Full access, S3ReadOnly Access, CloudWatchFullAccess
2. Create S3 bucket
3. Create DynamoDB with partition key
4. Create Lambda function by adding existing Role created above
5. Add S3 as triggers: 1 for All object and another for permanently delete event types.
6. Upload file in S3 and check the CloudWatch logs
7. Add and delete few files in S3 and check the records in DynamBD
