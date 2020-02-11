from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views import View


class Login(View):
    def get(self, request):
        return render(request, 'login.html')


class Home(View):
    @method_decorator(login_required, name='dispatch')
    def get(self, request):
        return render(request, 'home.html', {'user': request.user})
