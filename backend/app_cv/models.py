from django.db import models


class WorkExperience(models.Model):
    """Дополнительная часть Опыт работы"""
    company_name = models.CharField(verbose_name='Компания', max_length=100, blank=True, null=True)
    work_position = models.CharField(verbose_name='Должнолсть', max_length=100, blank=True, null=True)
    work_start = models.DateField(verbose_name='Дата начала', blank=True, null=True)
    work_end = models.DateField(verbose_name='Дата завершения', blank=True, null=True)
    work_now = models.BooleanField(blank=True, null=True)
    description = models.TextField(max_length=1000, help_text="Обязанности, достижения", blank=True, null=True)

    def __str__(self):
        return self.company_name


class Education(models.Model):
    """Дополнительная часть Образование"""
    education_name = models.CharField(verbose_name='Описание', max_length=255,
                                      help_text='Специальность, учебное заведение', blank=True, null=True)
    education_start = models.DateField(verbose_name='Дата начала', blank=True, null=True)
    education_end = models.DateField(verbose_name='Дата завершения', blank=True, null=True)
    studying_now = models.BooleanField(blank=True, null=True)

    def __str__(self):
        return self.education_name


class CV(models.Model):
    ENGLISH_LEVEL = [
        ('0', 'Не знаю'),
        ('a1', 'A1 - Начальный уровень'),
        ('a2', 'A2 - Элементарный уровень '),
        ('b1', 'B1 - Средний уровень'),
        ('b2', 'B2 - Средне-продвинутый уровень'),
        ('c1', 'C1 - Продвинутый уровень '),
        ('c2', 'C2 - Владение в совершенств'),
    ]
    title = models.CharField(
        max_length=150,
        verbose_name='Название',
        help_text="Python программист, iOS-разработчик, итд."
    )
    fullname = models.CharField(
        max_length=255,
        verbose_name='Фамилия и имя',
        help_text="Иванов Иван"
    )
    english = models.CharField(
        max_length=2,
        choices=ENGLISH_LEVEL,
        verbose_name='Владение английским')
    email = models.EmailField()
    linkedin = models.URLField(
        help_text='Ссылка на профиль, пример: linkedin.com/in/you_name',
        blank=True)
    github = models.URLField(
        help_text='Ссылка на профиль, пример: github.com/you_name',
        blank=True)
    contact = models.CharField(
        max_length=100,
        verbose_name='Контакт',
        help_text='Предпочитаемый способ связи (емайл, линкендин, телеграмм и т.п.)')
    description = models.TextField(
        max_length=1000,
        verbose_name='Описание',
        blank=True)
    skills = models.TextField(
        max_length=1000,
        verbose_name='Навыки',
        help_text='Знаю React.js, пользуюсь Vim, Работал с AWS')
    awards = models.TextField(
        max_length=1000,
        verbose_name='Награды, сертификаты',
        help_text='Участие в олимпиадах, хакатонах, других профильных меропритиях. Курсы.',
        blank=True)
    education = models.ManyToManyField(Education, blank=True)
    work_experience = models.ManyToManyField(WorkExperience, blank=True)

    def __str__(self):
        return self.title
