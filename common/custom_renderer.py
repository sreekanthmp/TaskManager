from rest_framework.renderers import JSONRenderer
from common.response import ResponseInfo


class CustomRenderer(JSONRenderer):

    def render(self, data, accepted_media_type=None, renderer_context=None):
        status_code = renderer_context['response'].status_code
        is_success = True
        message=''
        response_data=data
        if 'message' in data:
            message = data['message']
            response_data=data.get('data')
        
        if not str(status_code).startswith('2'):
            is_success = False
            try:
                message = data["detail"]
                data={}
            except KeyError:
                pass

        response = ResponseInfo(data=response_data, status=status_code, isSuccess=is_success, message=message).response
        return super(CustomRenderer, self).render(response, accepted_media_type, renderer_context)
