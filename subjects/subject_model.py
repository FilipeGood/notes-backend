import boto3


# dynamodb = boto3.client("dynamodb")
# # table = dynamodb.Table("subjects")

table = boto3.resource("dynamodb",).Table("subjects")
