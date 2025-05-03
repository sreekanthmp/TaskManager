from rest_framework import serializers

class ResponseInfo(object):
    def __init__(self, **args):
        self.response = {
            "data": args.get('data', {}),
            "message": args.get('message', ""),
            "isSuccess": args.get('isSuccess', True),
            "status": args.get('status', ''),
            "errors": args.get("errors", None)
        }
        
        
def serialize_errors(exception):
    errors = {}
    for field, field_errors in exception.detail.items():
        errors[field] = [str(error) for error in field_errors]
    return errors
