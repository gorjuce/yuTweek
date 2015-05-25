from django.core.urlresolvers import reverse_lazy
from django.views.generic.edit import UpdateView

class UserUpdate(UpdateView):
    fields = ['username', 'first_name', 'last_name']
    template_name = 'profile/update.html'
    success_url = '/'


    def get_object(self, queryset=None):
        return self.request.user