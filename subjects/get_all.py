from subjects import subject_model
import uuid
import logging


def get_all(event, context):

    subjects = subject_model.table.scan()

    response = {"statusCode": 200, "body": subjects["Items"], "sub": subjects}

    return response
