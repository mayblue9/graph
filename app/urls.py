# -*- coding: utf-8 -*-
from django.conf.urls import include, url
from django.contrib import admin

from zcore.views import HeapInfo


urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    #url(r'^zcore/', include('zcore.urls', namespace='zcore')),
    url(r'^syscheck/', include('syscheck.urls', namespace='syscheck')),
]

urlpatterns += [

    #
    #
    # view-cтраницы, имеющие шаблоны в каталоге templates
    url(r'^$', 'zcore.views.index', name='index'),
    url(r'^force-d3/(?P<id>[-\w]+)/(?P<graphFilter>.*)/(?P<nodesList>.*)/(?P<color>.*)/$', 'zcore.views.view_force_d3', name='viewForceD3'),
    url(r'^force-react/(?P<id>[-\w]+)/(?P<graphFilter>.*)/$', 'zcore.views.view_force_react', name='viewForceReact'),
    url(r'^chord/(?P<id>[-\w]+)/$', 'zcore.views.view_chord', name='viewChord'),
    url(r'^timeline/(?P<id>[-\w]+)/$', 'zcore.views.view_timeline', name='viewTimeline'),
    url(r'^new-project/$', 'zcore.views.view_new_project', name='viewNewProject'),
    url(r'^graph/(?P<id>[-\w]+)/$', 'zcore.views.view_graph', name='viewGraph'),
    url(r'^map/(?P<gid>[-\w]+)/(?P<nid>[-\w]+)/$', 'zcore.views.view_map', name='viewMap'),
    url(r'^create-project/(?P<graphFilter>.*)/$', 'zcore.views.create_project'),
    # /view-cтраницы
    #
    #


    #
    #
    # json-данные
    url(r'^json-heap-info/$', HeapInfo.as_view(), name='heapInfo'),
    url(r'^json-force-react/(?P<id>[-\w]+)/(?P<gfilter>.*)/$', 'zcore.views.json_force_react', name='jsonForceReact'),
    #url(r'^json-force-react/(?P<id>[-\w]+)/(?P<graphFilter>.*)/$', 'zcore.views.json_force_react', name='jsonForceReact'),
    url(r'^json-force-d3/(?P<id>[-\w]+)/(?P<graphFilter>.*)/(?P<nodesList>.*)/(?P<color>.*)/$', 'zcore.views.json_force_d3', name='jsonForced3'),
    url(r'^json-chord/(?P<id>[-\w]+)/(?P<gfilter>.*)/$', 'zcore.views.json_chord', name='jsonChord'),
    url(r'^json-timeline/(?P<id>[-\w]+)/(?P<gfilter>.*)/$', 'zcore.views.json_timeline', name='jsonTimeline'),
    url(r'^json-main-graph/(?P<id>[-\w]+)/$', 'zcore.views.json_main_graph', name='jsonMainGraph'),
    url(r'^json-main-graph/(?P<id>[-\w]+)/(?P<gfilter>.*)/$', 'zcore.views.json_main_graph', name='jsonMainGraph'),
    url(r'^json-transfers/(?P<gid>[-\w]+)/(?P<nid>[-\w]+)/$', 'zcore.views.json_transfers', name='jsonTransfers'),
    
    # вывод справочников
    url(r'^json-attributes/$', 'zcore.views.json_attributes', name='jsonAttributes'),
    url(r'^json-taxonomy/$', 'zcore.views.json_taxonomy', name='jsonTaxonomy'),
    # /json-данные
    #
    #
]


