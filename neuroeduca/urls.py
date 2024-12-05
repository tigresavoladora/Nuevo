from django.urls import path
from .views import SignUpView, CustomLoginView
from . import views

urlpatterns = [ 
    path('', views.index, name='index'),
    path('cuenta/', views.myaccount, name='myaccount'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path("signup/", SignUpView.as_view(), name="signup"),

    path('crear_persona/', views.crear_persona, name='crear_persona'),
    path('listar_personas/', views.listar_personas, name='listar_personas'),
    path('actualizar_persona/<str:rut>/', views.actualizar_persona, name='actualizar_persona'),
    path('eliminar_persona/<str:rut>/', views.eliminar_persona, name='eliminar_persona'),

    path('crear_curso/', views.crear_curso, name='crear_curso'),
    path('listar_cursos/', views.listar_cursos, name='listar_cursos'),
    path('actualizar_curso/<int:id>/', views.actualizar_curso, name='actualizar_curso'),
    path('eliminar_curso/<int:id>/', views.eliminar_curso, name='eliminar_curso'),
]