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


def clean_license_number_form(data):
    if data < datetime.datetime.now():
        raise ValidationError("Deadline can't be less than now")
    return data


class TaskCreateForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ("name", "description", "deadline", "priority", "task_type")

    def clean_deadline(self):
        data = self.cleaned_data["deadline"]
        return clean_license_number_form(data)

# class CarForm(forms.ModelForm):
#     drivers = forms.ModelMultipleChoiceField(
#         queryset=get_user_model().objects.all(),
#         widget=forms.CheckboxSelectMultiple,
#         required=False
#     )
#
#     class Meta:
#         model = Car
#         fields = "__all__"
