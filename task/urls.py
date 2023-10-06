from django.urls import path
from . import views

urlpatterns = [

    path('task/', views.task, name='dashboard-task'),
    path('create/request/', views.create_request, name='task-create-request'),
    path('assign/', views.assign, name='task-assign'),
    path('repair/', views.repair, name='task-repair'),
    path('movement/', views.movement, name='task-movement'),
    path('maintenance/', views.maintenance, name='task-maintenance'),
    path('desktop/select/move/', views.desktop_select_move, name='task-desktop-select-move'),
    path('laptop/select/move/', views.laptop_select_move, name='task-laptop-select-move'),
    path('desktop/select/', views.desktop_select, name='task-desktop-select'),
    path('issuance/<int:pk>/', views.desktop_issuance, name='task-issuance'),
    path('laptop/select/issue/', views.laptop_select_issue, name='task-laptop-select-issue'),

]