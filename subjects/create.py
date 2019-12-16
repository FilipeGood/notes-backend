from subjects import subject_model
import uuid
from datetime import datetime
import logging


def create(event, context):

    data = event["body"]

    try:
        notes = [{}]
        notes = data["notes"]
        for note in notes:
            note["id"] = str(uuid.uuid1())
    except:
        response = {"statusCode": 400, "body": "Error in for"}
        return response
    try:

        timestamp = str(datetime.utcnow())

        item = {
            "id": str(uuid.uuid1()),
            "name": data["name"],
            "notes": notes,
            "createdAt": timestamp,
            "updatedAt": timestamp,
        }
        # subject_model.dynamodb.put_item(TableName="subjects", Item=subject)

        subject_model.table.put_item(Item=item)
    except:
        logging.error("Can not create team")
        response = {"statusCode": 400, "body": "Error Creating Subject"}
        return response

    response = {"statusCode": 200, "body": item}

    return response

