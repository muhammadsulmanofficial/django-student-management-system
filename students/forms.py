from django import forms
from students.models import Student

class StudentForm(forms.ModelForm):
    class Meta: # yeah ModelForm ki configuration class hai. Iskey andar hum Django ko btatey hein ki form kis model se related hai aur kon kon sey fields ko form me show karna hai.
        model = Student # iska matlab hai ki ye form Student model se connected hai.
        fields = ['name', 'email', 'age', 'course']
