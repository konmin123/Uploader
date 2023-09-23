from django.db import models


class File(models.Model):
    file = models.FileField(
        'Файл',
        upload_to='uploaded_files/'
    )
    uploaded_at = models.DateTimeField(
        'Дата и время загрузки',
        auto_now_add=True
    )
    processed = models.BooleanField(
        'Обработан',
        default=False
    )
