import boto3
import random
import json

# DynamoDB connection
dynamodb = boto3.resource("dynamodb")
table = dynamodb.Table("CloudFacts")

# Bedrock client
bedrock = boto3.client("bedrock-runtime", region_name="us-east-1")


def lambda_handler(event, context):

    # Fetch all facts from DynamoDB
    response = table.scan()
    items = response.get("Items", [])

    # Return message if table is empty
    if not items:
        return {
            "statusCode": 200,
            "headers": {
                "Content-Type": "application/json",
                "Access-Control-Allow-Origin": "*",
                "Access-Control-Allow-Methods": "GET, OPTIONS",
                "Access-Control-Allow-Headers": "Content-Type"
            },
            "body": json.dumps({
                "fact": "No facts available in DynamoDB."
            })
        }

    # Pick random fact
    fact = random.choice(items)["FactText"]

    try:

        # Request body for Amazon Nova Lite
        body = {
            "messages": [
                {
                    "role": "user",
                    "content": [
                        {
                            "text": f"Take this cloud computing fact and make it fun, witty, and engaging in 1 short sentence only: {fact}"
                        }
                    ]
                }
            ],
            "inferenceConfig": {
                "maxTokens": 100,
                "temperature": 0.7
            }
        }

        # Invoke Amazon Bedrock model
        resp = bedrock.invoke_model(
            modelId="amazon.nova-lite-v1:0",
            body=json.dumps(body),
            accept="application/json",
            contentType="application/json"
        )

        # Parse Bedrock response
        result = json.loads(resp["body"].read())

        witty_fact = result["output"]["message"]["content"][0]["text"]

        # Fallback if no response
        if not witty_fact:
            witty_fact = fact

    except Exception as e:

        # Show Bedrock error if invocation fails
        witty_fact = f"BEDROCK ERROR: {str(e)}"

    # Return API response
    return {
        "statusCode": 200,
        "headers": {
            "Content-Type": "application/json",
            "Access-Control-Allow-Origin": "*",
            "Access-Control-Allow-Methods": "GET, OPTIONS",
            "Access-Control-Allow-Headers": "Content-Type"
        },
        "body": json.dumps({
            "fact": witty_fact
        })
    }