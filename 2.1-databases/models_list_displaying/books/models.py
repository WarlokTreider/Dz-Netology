from django.db import models


class Book(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField("Название", max_length=64)
    author = models.CharField("Автор", max_length=64)
    pub_date = models.DateField("Дата публикации")

    def __str__(self):
        return self.name + " " + self.author

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=("name", "author", "pub_date"), name="unique_book"
            )
        ]
