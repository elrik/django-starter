# -*- coding: utf-8 -*-
from django.views.generic import TemplateView


class WelcomeView(TemplateView):
    template_name = 'core/welcome.html'
