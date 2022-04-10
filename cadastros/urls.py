from django.urls import path

from .views import AtividadesUpdate, CampoUpdate, ConquistasUpdate, IdeiasCreate, IdeiasUpdate, MeusProjetosCreate, CampoCreate, AtividadesCreate, MeusProjetosUpdate, RelatoriosCreate, ConquistasCreate, RelatoriosUpdate, CampoDelete, MeusProjetosDelete, AtividadesDelete, RelatoriosDelete, IdeiasDelete, ConquistasDelete, CampoList, MeusProjetosList, RelatoriosList, IdeiasList, AtividadesList, ConquistasList

urlpatterns = [
    path('cadastrar/campo/', CampoCreate.as_view(), name='cadastrar-campo'),
    path('cadastrar/meusprojetos/', MeusProjetosCreate.as_view(), name='cadastrar-meusprojetos'),
    path('cadastrar/atividades/',
         AtividadesCreate.as_view(), name='cadastrar-atividades'),
    path('cadastrar/relatorios/', RelatoriosCreate.as_view(), name='cadastrar-relatorios'),
    path('cadastrar/ideias/', IdeiasCreate.as_view(), name='cadastrar-ideias'),
    path('cadastrar/conquistas/', ConquistasCreate.as_view(), name='cadastrar-conquistas'),

    path('editar/campo/<int:pk>/', CampoUpdate.as_view(), name='editar-campo'),
    path('editar/relatorios/<int:pk>/',
         RelatoriosUpdate.as_view(), name='editar-relatorios'),
    path('editar/atividades/<int:pk>/',
         AtividadesUpdate.as_view(), name='editar-atividades'),
    path('editar/ideias/<int:pk>/', IdeiasUpdate.as_view(), name='editar-ideias'),
    path('editar/conquistas/<int:pk>/',
         ConquistasUpdate.as_view(), name='editar-conquistas'),
    path('editar/meusprojetos/<int:pk>/',
         MeusProjetosUpdate.as_view(), name='editar-meusprojetos'),

    path('excluir/campo/<int:pk>/', CampoDelete.as_view(), name='excluir-campo'),
    path('excluir/meusprojetos/<int:pk>/', MeusProjetosDelete.as_view(),
         name='excluir-meusprojetos'),
    path('excluir/atividades/<int:pk>/', AtividadesDelete.as_view(),
         name='excluir-atividades'),
    path('excluir/relatorios/<int:pk>/', RelatoriosDelete.as_view(),
         name='excluir-relatorios'),
    path('excluir/ideias/<int:pk>/', IdeiasDelete.as_view(), name='excluir-ideias'),
    path('excluir/conquistas/<int:pk>/', ConquistasDelete.as_view(),
         name='excluir-conquistas'),

    path('listar/campo/', CampoList.as_view(), name='listar-campo'),
    path('listar/meusprojetos/', MeusProjetosList.as_view(),
         name='listar-meusprojetos'),
    path('listar/atividades/', AtividadesList.as_view(),
         name='listar-atividades'),
    path('listar/relatorios/', RelatoriosList.as_view(),
         name='listar-relatorios'),
    path('listar/ideias/', IdeiasList.as_view(), name='listar-ideias'),
    path('listar/conquistas/', ConquistasList.as_view(),
         name='listar-conquistas'),

]
