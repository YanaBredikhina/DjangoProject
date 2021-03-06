from django.shortcuts import render, redirect
from django.views.generic import View
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpRequest, HttpResponse
from django.forms import Form

from .forms import SimpleForm

class Index(View):

    def get(self, request: HttpRequest) -> HttpResponse:
        form: Form = SimpleForm()
        return render(request, 'input_mail/index.html', context={'form': form})

    def post(self, request: HttpRequest) -> HttpResponse:
        return redirect('input_mail:index')


@method_decorator(csrf_exempt, name='dispatch')
class Api(View):

    def get(self, request: HttpRequest) -> HttpResponse:
        return HttpResponse(status=404)

    def post(self, request: HttpRequest) -> HttpResponse:
        if request.GET.get('method') == 'ping':
            return HttpResponse(status=200)
        return HttpResponse(status=400)
