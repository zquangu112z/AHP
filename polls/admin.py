from django.contrib import admin

# Register your models here.
from .models import Question, Choice

# class ChoiceInline(admin.StackedInline):
class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3

class QuestionAdmin(admin.ModelAdmin):
    # list question page
    list_display = ('question_text', 'pub_date', 'was_published_recently')
    #panel filter 
    list_filter = ['pub_date']
    # list_filter = ['question_text'] neu co nhieu list_filter thi chi co tac dung cai sau cung
    search_fields = ['question_text']
	#add question page
    fieldsets = [
        ('Important',               {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']})
    ]
    inlines = [ChoiceInline]
	# fields = ['question_text' ,'pub_date' ]
admin.site.register(Question, QuestionAdmin)

# admin.site.register(Question)
admin.site.register(Choice)