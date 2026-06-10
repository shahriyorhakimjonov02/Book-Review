from src.core.models.base import *
from django.contrib.auth.models import User

class Category(BaseModel):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Book(BaseModel):
    name = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    author = models.CharField(max_length=150)
    book_images = models.ImageField(upload_to="book_images/", null=True,)
    description = models.TextField()
    published_date = models.DateField()

    def __str__(self):
        return self.name

class Comment(BaseModel):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='comments')
    book = models.ForeignKey(Book, on_delete=models.CASCADE , related_name='comments')
    comment = models.TextField()

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.comment

class Rating(BaseModel):

    STAR_CHOICES = (
        (1, "1"),
        (2, "2"),
        (3, "3"),
        (4, "4"),
        (5, "5"),
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey( Book, on_delete=models.CASCADE,  related_name="ratings" )

    rating = models.IntegerField(choices=STAR_CHOICES)


    class Meta:
        unique_together = ("user", "book")
