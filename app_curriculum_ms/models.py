from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


class UniversityTeacher(models.Model):
    """
    Преподаватель университета

    Таблица данных "University Teacher"
    непосредственно связана со встроенной таблицей "User"
    """

    # Логин преподавателя университета
    login = models.OneToOneField(User, verbose_name="Логин", on_delete=models.CASCADE, unique=True, primary_key=True)

    # Информация о университете, факультете и кафедре, где работает преподаватель
    university_abbreviation = models.CharField("Аббревиатура университета", max_length=10)
    faculty = models.CharField("Факультета университета", max_length=20)
    department = models.CharField("Кафедра университета", max_length=20)

    # Основная информация о преподавателе университета
    academic_title = models.CharField("Ученое звание", max_length=100)
    phone_number = models.CharField("Номер телефона", max_length=20, help_text="+7 (***) ***-**-**")
    avatar = models.ImageField("Аватар", upload_to="img/teachers")

    def __str__(self):
        return 'Логин: %s' % (self.login)

    class Meta:
        verbose_name = "Преподаватель университета"
        verbose_name_plural = "Преподаватели университета"


class SubjectCurriculum(models.Model):
    """
    Дисциплина учебного плана

    Таблица данных "SubjectCurriculum"
    связана связью "много к многим" с таблицей "Curriculum"
    """

    # Основная информация о дисциплине
    id_subject = models.AutoField("ID", primary_key=True)
    subject = models.CharField("Название дисциплины", max_length=100)
    semester = models.PositiveSmallIntegerField("Номер семестра")

    # Другие поля
    # (В процессе...)

    def __str__(self):
        return 'Дисциплина: %s / Семестр: %s' % (self.subject, self.semester)

    class Meta:
        verbose_name = "Дисциплина учебного плана"
        verbose_name_plural = "Дисциплины учебного плана"


class Curriculum(models.Model):
    """
    Учебный план

    Таблица данных "Curriculum"
    связана связью "один ко многим" с таблицей "UniversityTeacher"
    """

    # Идентификатор учебного плана и автор
    id = models.AutoField("ID", primary_key=True)
    creator = models.ForeignKey(UniversityTeacher, verbose_name="Автор", on_delete=models.SET_NULL, null=True)

    # Дата создания и последнего изменения
    date_created = models.DateTimeField("Дата создания", auto_now=True)
    date_last_changed = models.DateTimeField("Дата последнего изменения", auto_now=True)

    # Заголовок учебного плана
    title = models.CharField("Заголовок учебного плана", max_length=300, unique=True)

    # Годы набора и выпуска
    year_of_start = models.PositiveSmallIntegerField("Год набора")
    year_of_end = models.PositiveSmallIntegerField("Год выпуска")

    # Информация об академическом уровне
    academic_level = models.CharField("Академический уровень", max_length=50)
    years_to_study = models.CharField("Срок обучения", max_length=50)

    # Информация о университете, факультете и кафедре учебного плана
    university_abbreviation = models.CharField("Аббревиатура университета", max_length=10)
    faculty = models.CharField("Факультета университета", max_length=20)
    department = models.CharField("Кафедра университета", max_length=20)

    # Информация об отрасли знаний, специальности и образовательной программе
    branch_of_knowledge = models.CharField("Отрасль знаний", max_length=100)
    speciality = models.CharField("Специальность", max_length=100)
    education_program = models.CharField("Образовательная программа", max_length=100)
    speciality_addition_info = models.CharField("Дополнительная информация", max_length=150, blank=True)

    # Subjects
    subjects = models.ManyToManyField(SubjectCurriculum, verbose_name="Дисциплины", related_name="subjects", blank=True)

    # Choices
    CHOICES_FORM_EDUCATION = (
        ('Очная', 'Очная'),
        ('Заочная', 'Заочная')
    )
    CHOICES_CITIZENSHIP = (
        ('Россия', 'Россия'),
        ('Иностранец', 'Иностранец')
    )
    CHOICES_LANGUAGE_INSTITUTION = (
        ('Русский', 'Русский'),
        ('Английский', 'Английский')
    )

    # Other info
    form_education = models.CharField("Форма обучения", max_length=10, choices=CHOICES_FORM_EDUCATION)
    citizenship = models.CharField("Гражданство", max_length=10, choices=CHOICES_CITIZENSHIP)
    language_institution = models.CharField("Язык обучения", max_length=50, choices=CHOICES_LANGUAGE_INSTITUTION)
    enrollment_number = models.PositiveSmallIntegerField("Номер набора")

    def __str__(self):
        return 'Учебный план: %s / Автор: [%s] / Дата последнего изменения: [%s]' % (self.title, self.creator, self.date_last_changed)

    def get_url_detail_curriculum(self):
        return reverse("detail_curriculum", kwargs={"pk": self.id})

    def get_url_edit_curriculum(self):
        return reverse("edit_curriculum", kwargs={"pk": self.id})

    class Meta:
        verbose_name = "Учебный план"
        verbose_name_plural = "Учебные планы"
