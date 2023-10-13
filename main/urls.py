from django.urls import path
from . import views

urlpatterns = [
    path('', views.alunoView, name='aluno_lista'),

    path('alunoID/<int:id>', views.alunoIDview, name='aluno_detalhe'),

    path('contact', views.contact_view, name='aluno-contact'),

    path('aluno/create/', AlunoCreateView.as_view(), name='aluno-create'),
    path('aluno/<int:pk>/update/', AlunoUpdateView.as_view(), name='aluno-update'),


]
