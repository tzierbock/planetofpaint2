from django.contrib import admin
from models import Canvas, Point, Line

class PointInlineAdmin(admin.TabularInline):
	model = Point

	def get_extra(self, request, obj=None, **kwargs):
		return 0

class LineInlineAdmin(admin.TabularInline):
	model = Line

	def get_extra(self, request, obj=None, **kwargs):
		return 0

class CanvasAdmin(admin.ModelAdmin):
	inlines = [LineInlineAdmin]

class LineAdmin(admin.ModelAdmin):
	inlines = [PointInlineAdmin]

# Register your models here.
admin.site.register(Canvas, CanvasAdmin)
admin.site.register(Line, LineAdmin)
admin.site.register(Point)