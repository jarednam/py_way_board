# ---------------------------------------- [edit] ---------------------------------------- #
from django.urls import path

from . import views

#네임스페이스 타앱 충돌방지
app_name = 'way_board'

urlpatterns = [
    path('', views.index, name='index'),
    # ---------------------------------------- [상세] ---------------------------------------- #
    path('<int:question_id>/', views.detail, name='detail'),
    # -----------------------------------------[답변]------------------------------------------ #
    path('answer/create/<int:question_id>/', views.answer_create, name='answer_create'),
    # -----------------------------------------[작성]------------------------------------------ #
    path('question/create/', views.question_create, name='question_create'),
    path('question/modify/<int:question_id>/', views.question_modify, name='question_modify'),
    path('question/delete/<int:question_id>/', views.question_delete, name='question_delete'),
    path('answer/modify/<int:answer_id>/', views.answer_modify, name='answer_modify'),
]
# ---------------------------------------------------------------------------------------- #