from django.views.generic import TemplateView

class DashboardView(TemplateView):
    template_name = 'dashboard.html'

class HomePageView(TemplateView):
    template_name = 'home.html'
