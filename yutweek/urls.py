from django.conf import settings
from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import CreateView

from tweeks import views as tweeks_views
from yusers.views import UserUpdate


urlpatterns = patterns('',
    url(r'^', include('tweeks.urls')),
    url(r'^admin/', include(admin.site.urls)),


    url('^accounts/', include('django.contrib.auth.urls')),
    url('^accounts/register/$', CreateView.as_view(
            template_name='registration/register.html',
            form_class=UserCreationForm,
            success_url='/',
    ), name="register"),
    url('^accounts/profile/$', UserUpdate.as_view(), name="profile"),
    url('^users/(?P<user_pk>[0-9])/tweeks/$', tweeks_views.get_user_tweeks, name="user_tweeks"),

)+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
