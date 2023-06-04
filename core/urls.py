
from django.urls import path
from .views import home,cad,update,editar,delete,usercreate,login,plataforma,logout


urlpatterns = [
    path("", home,name="home"),
    path("create",cad,name="create"),
    path("editar/<int:id>",editar,name="editar"),
    path("update/<int:id>",update,name="update"),
    path("delete/<int:id>",delete,name="delete"),
    path("usercreate",usercreate,name="usercreate"),
    path("login",login,name="login"),
    path("plataforma",plataforma,name="plataforma"),
    path("admin/logout/",logout,name="logout")
  
   

]
