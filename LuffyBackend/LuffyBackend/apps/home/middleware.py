from django.contrib.sessions.middleware import MiddlewareMixin


class CorsMiddleware(MiddlewareMixin):
    def process_response(self, request, response):
        # 处理非简单请求
        if request.method == 'OPTIONS':
            response['Access-Control-Allow-Headers'] = '*'
            response['Access-Control-Allow-Methods'] = '*'
            return response

        # 在响应头中加入Access-Control-Allow-Origin, 处理了简单请求
        response['Access-Control-Allow-Origin'] = '*'
        return response
