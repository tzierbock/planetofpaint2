from django.contrib import admin
from models import Canvas, Point

class PointInlineAdmin(admin.TabularInline):
	model = Point

	def get_extra(self, request, obj=None, **kwargs):
		return 0

class CanvasAdmin(admin.ModelAdmin):
	inlines = [PointInlineAdmin]


# Register your models here.
admin.site.register(Canvas, CanvasAdmin)
admin.site.register(Point)