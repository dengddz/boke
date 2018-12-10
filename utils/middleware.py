from django.http import HttpResponseRedirect
from django.utils.deprecation import MiddlewareMixin

from backsys.models import SuperUser
import re

class LoginStatusMiddleware(MiddlewareMixin):

    def process_request(self, request):
        # 在访问 登录和注册的时候，不需要 登录验证  , '/backsys/login/', '/backsys/index/'
        if re.match(r'^/web/', request.path) or request.path == '/backsys/login/':
        # if request.path in ['/web/index/', '/web/about/', '/web/list/', '/web/info/', '/backsys/login/']:
            return None
        user_id = request.session.get('user_id')
        if user_id:
            request.user = SuperUser.objects.get(pk=user_id)
            return None
        else:
            return HttpResponseRedirect('/backsys/login/')

    def process_response(self, request, response):
        return response