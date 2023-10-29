from django import forms
from task.models import Status, ToDoList, Task


class ListForm(forms.Form):
    name = forms.CharField(max_length=50)


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'


class ListForm2(forms.ModelForm):

    class Meta:
        model = Task
        fields = '__all__'
        labels = {
            'name': 'Title',
            'list_id': 'List name',
        }


    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('request').user
        super().__init__(*args, **kwargs)
        self.fields['list_id'].queryset = ToDoList.objects.filter(user_id_id=self.user)

        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'

