from django import forms

from .models import Book, Tag, Author

# class BookForm(forms.Form):
#     name = forms.CharField(max_length=20, label='Book Name')
#     price = forms.IntegerField(min_value=1, label='Price')
#     introduction = forms.CharField(label='Introduction', widget=forms.Textarea())

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = '__all__'
        # exclude = () # except

    def __init__(self, *args, **kwargs):
        
        super().__init__(*args, **kwargs)
        
        self.fields["tags"].widget = forms.CheckboxSelectMultiple()
        self.fields["tags"].queryset = Tag.objects.all()

        self.fields["authors"].widget = forms.CheckboxSelectMultiple()
        self.fields["authors"].queryset = Author.objects.all()

class DeleteConfirmForm(forms.Form):
    check = forms.BooleanField(label='您確定要刪除嗎?')
    