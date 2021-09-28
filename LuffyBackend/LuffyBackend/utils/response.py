from rest_framework.response import Response


class APIResponse(Response):
    def __init__(self, status=None, headers=None, **kwargs):
        data = {'code': 200, 'msg': 'Success'}
        if kwargs:
            data.update(kwargs)

        super().__init__(status=status, headers=headers, data=data)
