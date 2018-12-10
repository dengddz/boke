from django import forms

class AddArtForm(forms.Form):
    # required 代表 必填项 ， error_messages为错误信息重定义
    a_title = forms.CharField(min_length=5, required=True,
                            error_messages={
                                'required': '文章标题是必填项',
                                'min_length': '文章标题不能少于5个字符'
                            })
    a_keywords = forms.CharField(min_length=3, required=True,
                            error_messages={
                                'required': '文章关键字是必填项',
                                'min_length': '文章关键字不能少于3个字符'
                            })
    a_describe = forms.CharField(min_length=5, required=True,
                           error_messages={
                               'required': '文章描述是必填项',
                               'min_length': '文章描述不能少于5符'
                           })
    a_content = forms.CharField(required=True,
                              error_messages={
                                  'required': '文章内容是必填项'
                              })
    a_titlepic = forms.ImageField(required=True,
                            error_messages={
                                'required': '图片内容是必填项'
                            })
    # a_f = forms.IntegerField(required=True)