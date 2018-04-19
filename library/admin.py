from django.contrib import admin
from .models import Book, Category, Author, Client, Checkout, CheckoutLine, Payment, GenderCode, AuthorCategoryCode

# Register your models here.
admin.site.register(Book)
admin.site.register(Category)
admin.site.register(Author)
admin.site.register(Client)
admin.site.register(Checkout)
admin.site.register(CheckoutLine)
admin.site.register(Payment)
admin.site.register(GenderCode)
admin.site.register(AuthorCategoryCode)

