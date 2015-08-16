from django import forms


class BlogPublishForm(forms.Form):
    title = forms.CharField(widget=forms.TextInput(attrs={'name': "title", 'type': "text", 'placeholder': "Title?"}))
    content = forms.CharField(widget=forms.Textarea(attrs=
                                                    {'name': "content", 'data-provide': "markdown", 'rows': "20"}
                                                    ))
