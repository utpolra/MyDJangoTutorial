from .views import (
    addcomment,likepost,addphoto,
    search,filter,contact,
    postview,postcreate,PostDeleteView, 
    subview,ContactView,PostEditView,
    PostCreateView,PostListView,PostDetailView,commentdelete,apply
    )
from .pdf import contact_pdf
from django.urls import path
app_name='tuition'
urlpatterns = [
    # path('contact/',contact,name="contact"),
    # path('postview/',postview,name="postview"),
    path('create/',postcreate,name="create"),
    # path('contact2/',ContactView.as_view(form_class=ContactFormtwo, template_name="contact2.html"),name="contact2"),
    path('search/',search,name="search"),
    path('filter/',filter,name="filter"),
    path('pdf/',contact_pdf,name="pdf"),
    path('likepost/<int:id>/',likepost,name="likepost"),
    path('addphoto/<int:id>/',addphoto,name="addphoto"),
    path('commentdelete/<int:id>/',commentdelete,name="commentdelete"),
    path('addcomment/',addcomment,name="addcomment"),
    path('contact/',ContactView.as_view(),name="contact"),
    path('posts/',postview,name="posts"),
    path('subjects/',subview,name="subjects"),
    path('postlist/',PostListView.as_view(),name="postlist"),
    path('postdetail/<int:pk>/',PostDetailView.as_view(),name="postdetail"),
    path('delete/<int:pk>/',PostDeleteView.as_view(),name="delete"),
    path('edit/<int:pk>/',PostEditView.as_view(),name="edit"),
    path('apply/<int:id>/',apply,name="apply"),
    # path('create/',PostCreateView.as_view(),name="create"),
]