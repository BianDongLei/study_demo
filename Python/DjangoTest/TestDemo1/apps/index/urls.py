from django.conf.urls import url

from apps.index import views

urlpatterns = [
    url(r'^$', view=views.note_response),
    url(r"^form/$", view=views.submit_form, name="submit_form")
]
