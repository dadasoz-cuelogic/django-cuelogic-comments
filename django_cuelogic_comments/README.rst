# django-cuelogic-comments

django-cuelogic-comments is a simple Django app to conduct Web-based Comments. 

Installation
-----------

pip install django-cuelogic-comments

Quick start
-----------

1. Add "comments" to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = (
        ...
        'django_cuelogic_comments',
    )

2. Run `python manage.py migrate` to create the comments models.

3. In your view file import the module 
    
    from django_cuelogic_comments import Comments

4. Create a instance in your view file/where you want to include comments
    
<<<<<<< HEAD
    comments = Comments.get(post_id,edit=True,delete=True,reply=True,user="User Name")
=======
    comments = Comments.get(request,post_id,delete=True,reply=True,"Username")
>>>>>>> Updates

5. Pass this comments data to your template
   
   render_to_response('your template file', RequestContext(request, {"comments":comments}))

6. Print in Template

   {{comments}}
    
