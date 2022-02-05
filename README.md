## learning-django


#### Creating a new project 
```py
django-admin startproject <project name>
```

In the project directory, create a new app: 
```py 
python manage.py startapp <app name>
```


Some first steps to follow after creating a new Django project:  
1. Create `urls.py` and `views.py` in the app directory  
2. Add the name of the app to `INSTALLED_APPS` list, add template dir: `BASE_DIR / 'templates'` in `project dir/settings.py` 
3. Create `templates` folder in the root dir to store all the html files  
4. In project `dir/urls.py`, add `path('', include('<app name>/urls'))` to `urlpatterns` to include urls from the app  
5. In `app/models.py`, create class(es) to store database objects. After any change in this file, run the two commands under the `Database` heading below to update the DB with the changes.  
6. To register the DB(classes in `models.py`), add this line to `app dir/admin.py`: `admin.site.register(<class name>)` 




#### Starting the Django server  
```py 
python manage.py runserver 
```    


#### Database  

```py 
python manage.py makemigrations   
python manage.py migrate 
```   


#### admin credentials  

```py 
python manage.py createsuperuser 
```   
