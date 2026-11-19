from django.shortcuts import render, redirect, get_object_or_404
from students.models import Student
from students.forms import StudentForm

# Create your views here.
def home(request):
    return render(request, 'students/home.html')


def add_student(request):
    if request.method == 'POST': 
        form = StudentForm(request.POST) # request.POST mein submitted form data hota hai.
        if form.is_valid():
            form.save()

            return redirect('student_list')
    else:
        form = StudentForm()
    return render(request, 'students/student_form.html', {'form': form, 'title': 'Add Student', 'button_text': 'Save Student'})


def student_list(request):
    students = Student.objects.all()

    return render(request, 'students/student_list.html', {'students': students})


def update_student(request, student_id):
    student = get_object_or_404(Student, id=student_id) # Database me Student Model ka wo record find karo jis ki ID URL say ayi ha. Agar student_id mil gya to object return ho ga, warna 404 error show ho ga.

    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student) # instance=student instance ka matlab hai yeah form ik existing student object ki saath connected hai. Jab user UPDATE page open kare ga To FORM me pehlye sa existing student ka data show hoga. Means Existing record ko update karney wala submited form.
        if form.is_valid():
            form.save()

            return redirect('student_list')
    else:   
        form = StudentForm(instance=student) # Existing data ke saath form

    return render(request, 'students/student_form.html', {'form': form, 'title': 'Edit Student', 'button_text': 'Update Student'})

    # Notice karo ke humne Create aur Update dono mein same student_form.html use ki hai!

def delete_student(request, student_id):
    student = get_object_or_404(Student, id=student_id)

    if request.method == 'POST':
        student.delete()

        return redirect('student_list')
    return render(request, 'students/student_confirm_delete.html', {'student': student})