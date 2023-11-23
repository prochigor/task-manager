import datetime

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError

from task.models import Worker, Task


class WorkerCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = Worker
        fields = UserCreationForm.Meta.fields + (
            "position",
            "first_name",
            "last_name",
        )


class TaskCreateForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ("name", "description", "deadline", "priority", "task_type")

    def clean_deadline(self):
        data = self.cleaned_data["deadline"]
        if data < datetime.datetime.now():
            raise ValidationError("Deadline can't be less than now")
        return data


class TaskSearchForm(forms.Form):
    name = forms.CharField(
        max_length=255,
        required=False,
        label="",
        widget=forms.TextInput(attrs={"placeholder": "Search by task name"})
    )
