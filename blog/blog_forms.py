#encoding=utf-8

from django import forms
from models import Category

STATUS = (('DRAFT', 'draft'), ('PUBLISHED', 'published'))




def getAllCategory():
    count = Category.objects.count()
    # print "category count :%d" %count
    category_objs = Category.objects.all()
    # print "category objs %s" % category_objs
    category_dict = dict()
    for obj in category_objs:
        # print "obj %s" % obj
        code = obj.category_code
        # print "code is %s" % code
        name = obj.category_name
        # print "name is %s" % name
        category_dict[code] = name

    #     code = obj.category_Code
    #     print "get category :%s" % code
    #     name = obj.category_Name
    #     print "get category : %s" % name
    # print "list is %s" % category_dict
    keys = category_dict.keys()
    # 转换成choices需要的类型
    result = [(keys[i], category_dict[keys[i]]) for i in range(len(keys))]
    # print result
    return result

# 获取分类列表
Category_Choices = getAllCategory()


class BlogPublishForm(forms.Form):
    title = forms.CharField(widget=forms.TextInput(attrs={'name': "title", 'type': "text", 'placeholder': "Title?"}))
    content = forms.CharField(widget=forms.Textarea(attrs=
                                                    {'name': "content", 'data-provide': "markdown", 'rows': "20"}
                                                    ))
    category = forms.ChoiceField(label='Category', choices=Category_Choices, widget=forms.Select, initial=Category_Choices[0][0])
    status = forms.ChoiceField(label='status', choices=STATUS, widget=forms.Select, initial=STATUS[0][0])
