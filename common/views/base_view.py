from rest_framework.status import HTTP_200_OK
from rest_framework.response import Response
from common.response import ResponseInfo
from common.custom_renderer import CustomRenderer


class BaseView:
    """
    Used for non-authenticated views
    """
    renderer_classes = [CustomRenderer, ]

    def response(self, token="", status=HTTP_200_OK, is_success=True, data={}, message=""):
        response = ResponseInfo(token=token, data=data, status=status, isSuccess=is_success,
                                message=message).response
        return Response(response)

    def log(self, **kwargs):
        pass

    def destroy(self, *args, **kwargs):
        """ delete method call will be returning deleted object"""
        serializer = self.get_serializer(self.get_object())
        super().destroy(*args, **kwargs)
        return Response(serializer.data)
