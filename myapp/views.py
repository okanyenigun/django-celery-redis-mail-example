from django.views.generic.edit import FormView
from django.http import HttpResponse
from myapp.forms import SubscribeForm
from myapp.tasks import send_notification_mail

class IndexView(FormView):
    template_name = 'index.html'
    form_class = SubscribeForm

    def form_valid(self, form):
        mail = form.cleaned_data["mail"]
        message = form.cleaned_data["message"]
        send_notification_mail.delay(mail, message)
        return HttpResponse('We have sent you a confirmation mail!')




