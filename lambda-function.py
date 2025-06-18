import boto3
import json

def lambda_handler(event, context):
    db = boto3.client('dynamodb')

    response = db.update_item(
        TableName='VisitorCount',
        Key={'id': {'S': 'home'}},
        UpdateExpression='ADD visit_count :inc',
        ExpressionAttributeValues={':inc': {'N': '1'}},
        ReturnValues='UPDATED_NEW'
    )

    count = response['Attributes']['visit_count']['N']

    return {
        'statusCode': 200,
        'headers': {
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Headers': '*',
            'Access-Control-Allow-Methods': 'GET'
        },
        'body': json.dumps({'count': int(count)})
    }
