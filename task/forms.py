from django import forms
from account.models import Profile, User
from task.models import Status, ToDoList


class ListForm(forms.Form):
    name = forms.CharField(max_length=50)
    # user_id = forms.ModelChoiceField(queryset=User.objects.all())
    # print(user_id)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'


    # def clean_descriptions(self):
    #     initial = self.cleaned_data['description']
    #     sentences = re.sub(r'\s*\.\s*', '.', initial).split('.')
    #     return '. '.join(sentence.capitalize() for sentence in sentences)
    #
    # def clean(self):
    #     result = super().clean()
    #     if result['genre'].name == 'Comedy' and result['rating'] > 5:
    #         self.add_error('genre', '')
    #         self.add_error('rating', '')
    #         raise ValidationError(
    #             "Commedies aren't so good to be rated over 5"
    #         )
    #
    #     return result

class ListForm2(forms.Form):

    name = forms.CharField(max_length=50)
    list_id = forms.ModelChoiceField(queryset=None)
    description = forms.CharField(widget=forms.Textarea, required=False)
    deadline = forms.DateTimeField()
    status = forms.ModelChoiceField(queryset=Status.objects)
    # added = forms.DateTimeField(auto_now_add=True)

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request')
        super().__init__(*args, **kwargs)
        self.fields['list_id'].queryset = ToDoList.objects.filter(user_id_id=self.request.user)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'

