from django.urls import path

from manager.views import AboutDataView, CombinedDataView, ContactDataView, FaqDataView,GlobalDataView, HomeDataView, PracticeDataView, TeamDataView
urlpatterns = [
    path('api/combined-data/', CombinedDataView.as_view(), name='combined-data'),
    path('global-data', GlobalDataView.as_view(), name='global-data'),

    path('home', HomeDataView.as_view(), name='home'),
    path('about', AboutDataView.as_view(), name='about'),
    path('team', TeamDataView.as_view(), name='team'),
    path('faq', FaqDataView.as_view(), name='faq'),
    path('practice-area', PracticeDataView.as_view(), name='practice-area'),
    path('contact', ContactDataView.as_view(), name='contact'),
]
