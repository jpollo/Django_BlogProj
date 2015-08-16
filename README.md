# Django_BlogProj

学习中

#### Preparation
sudo pip install MySQL-python
sudo pip install south



### 模板层次
base
blog_base
home | articel | about | archive


### TODO
1. admin 页面



### QA
##### CSRF verification failed. Request aborted  
   ``` 
   <form method="post">
        {% csrf_token %}
    return render_to_response('publish_page/pform.html', {'form': form}, context_instance=RequestContext(request))
    ```


