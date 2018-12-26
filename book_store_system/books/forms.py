from django import forms

from .models import Book

# class BookForm(forms.Form):
#     name = forms.CharField(max_length=20, label='Book Name')
#     price = forms.IntegerField(min_value=1, label='Price')
#     introduction = forms.CharField(label='Introduction', widget=forms.Textarea())

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = '__all__'
        # exclude = () # except

class DeleteConfirmForm(forms.Form):
    check = forms.BooleanField(label='您確定要刪除嗎?')
    