"""actkx URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
import actkx.views as views
import actkx.views_kj as views_kj
import dxs.dxs_views as dxs_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/index/num', views.get_online_user_num),
    path('api/index/num_three', views.get_online_user_num_three),
    path('api/dkp/get_per', views.get_per),
    path('api/dkp/get_org', views.get_org),
    path('api/dkp/get_art', views.get_art),
    path('api/dkp/get_top_words', views.get_top_words),

    path('api/dkp/get_museum_map', views.get_museum_map),
    path('api/dkp/get_museum_list', views.get_museum_list),
    path('api/dkp/get_museum_info', views.get_museum_info),
    path('api/dkp/get_museum_abstract', views.get_museum_abstract),

    path('api/dkp/get_kpnrst_hot', views.get_kpnrst_hot),
    path('api/dkp/get_knprst_trend', views.get_knprst_trend),
    
    path('api/kj/get_num', views_kj.get_online_user_num),
    path('api/kj/get_male', views_kj.get_male_user_num),
    path('api/kj/get_map_nums', views_kj.get_map_nums),
    path('api/kj/get_active_areas', views_kj.get_active_areas),
    path('api/kj/get_news', views_kj.get_news),
    path('api/kj/get_hotworld', views_kj.get_hotWorld),
    path('api/kj/get_member_num', views_kj.get_member_num),
    path('api/kj/get_org_num', views_kj.get_org_num),
    path('api/kj/get_org_news', views_kj.get_org_news),
    path('api/kj/get_dynamic', views_kj.get_dynamic),
    path('api/kj/get_collect', views_kj.get_collect),

    path('api/dxs/dxs_url_demo', dxs_views.dxs_url_demo),
    path('api/dxs/get_xuehui_list_data', dxs_views.get_xuehui_list_data),
    path('api/dxs/get_china_map_data', dxs_views.get_china_map_data),
    path('api/dxs/get_world_map_data', dxs_views.get_world_map_data),
    path('api/dxs/get_s_e_data', dxs_views.get_s_e_data),
    path('api/dxs/get_redian_data', dxs_views.get_redian_data),
    path('api/dxs/get_sci_ei_data', dxs_views.get_sci_ei_data),
    path('api/dxs/get_huodong_data', dxs_views.get_huodong_data),
]
