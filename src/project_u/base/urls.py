from django.urls import  path
from . views import lista_p,detalle_t,login
from django.contrib.auth.views import LogoutView


urlpatterns = [path('',lista_p.as_view(),name='home'),
               path('login/', login.as_view(), name='login'),
               path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
               path('tarea/',detalle_t.as_view(),name='tarea' )

]
