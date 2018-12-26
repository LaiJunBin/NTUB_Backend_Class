from django import forms

class DeleteConfirmForm(forms.Form):
    check = forms.BooleanField(label='您確定要刪除嗎?')