from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/<str:title>",views.entry, name="entry"),
    path("search",views.search, name="search"),
    path("createpage",views.createPage,name="createPage"),
    path("save",views.savePage,name="savePage"),
    path("edit/<str:title>",views.edit,name="edit"),
    path("saveEdits",views.saveEdits,name="saveEdits"),
    path("randomPage",views.randomPage,name="randomPage")
]
