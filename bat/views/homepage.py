from django.http.response import HttpResponse
from django.views.generic import TemplateView
from django.urls import reverse
from django.shortcuts import redirect

class HomePageView(TemplateView):
    template_name = "homepage/homepage.html"

    # def get(self, request, *args, **kwargs):
    #     url = reverse("admin:index")
    #     return redirect(url)