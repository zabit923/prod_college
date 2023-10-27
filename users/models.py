from django.contrib.auth.models import AbstractUser
from django.db import models




class Facult(models.Model):
    name = models.CharField('Факультет', max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Факультет'
        verbose_name_plural = 'Факультеты'


class Course(models.Model):
    name = models.CharField('Курс', max_length=5)

    def __str__(self):
        return f"{self.name} курс"

    class Meta:
        verbose_name = 'Курс'
        verbose_name_plural = 'Курсы'


class User(AbstractUser):
    password = models.CharField(max_length=128, null=True, blank=True)
    student_id = models.CharField(max_length=128)
    first_name = models.CharField(max_length=150, null=True, blank=False)
    last_name = models.CharField(max_length=150, null=True, blank=False)
    username = models.CharField(unique=True, max_length=150, null=True, blank=True)
    image = models.ImageField(upload_to='users_images', null=True, blank=True)
    is_teacher = models.BooleanField(default=False)
    course = models.ForeignKey(Course, on_delete=models.SET_NULL, null=True, blank=True, default='')
    facult = models.ForeignKey(Facult, on_delete=models.SET_NULL, null=True, blank=True, default='')

    def __str__(self):
        return f'{self.first_name} {self.last_name}' or self.username

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'


class TeacherLink(models.Model):
    teacher = models.ForeignKey(User, on_delete=models.CASCADE)
    faculty = models.ForeignKey(Facult, on_delete=models.CASCADE, default='')
    course = models.ForeignKey(Course, on_delete=models.CASCADE, default='')
    link = models.CharField(max_length=150, null=True, blank=False)

    def __str__(self):
        return f"Ссылка для {self.course} от {self.teacher}"

    class Meta:
        verbose_name = 'Ссылка учителя'
        verbose_name_plural = 'Ссылки учителя'