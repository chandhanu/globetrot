from django.views.generic import TemplateView


class IndexPageView(TemplateView):
    template_name = 'main/index.html'


class ChangeLanguageView(TemplateView):
    template_name = 'main/change_language.html'

class AboutView(TemplateView):
    template_name = 'main/about.html'

class ExploreView(TemplateView):
    template_name = 'main/browselocations.html'

