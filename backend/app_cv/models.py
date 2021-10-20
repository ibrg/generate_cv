from django.db import models


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

    def __str__(self):
        return self.title
