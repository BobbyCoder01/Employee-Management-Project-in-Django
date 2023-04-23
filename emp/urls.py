
from django.urls import path
from .views import *


urlpatterns = [
    path('' , home),
    path('add/' , add_emp),
    path('delete_emp/<int:emp_id>' , delete_emp),
    path('update_emp/<int:emp_id>' , update_emp),
    path('do_update/<int:emp_id>' , do_update),
]