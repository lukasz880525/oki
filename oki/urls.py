from django.conf.urls import patterns, include, url
from django.contrib import admin


from shelf.views import MainPageView      # przy 2 sposobie nie trzeba tego bo w shelf/views jest to; index_view = MainPageView.as_view()
from contact.views import MessageAddView


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'oki.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^shelf/',include('shelf.urls',namespace='shelf')),
    url(r'^contact/$',MessageAddView.as_view()),
    url(r'^$',MainPageView.as_view(),name='main-page'), # 2 sposob: url(r'^$',shelf.views.index_view',name='main-page')
    url(r'^accounts/', include('allauth.urls')),
)
