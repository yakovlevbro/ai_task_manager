from django.db import models

from django.db import models


class GanttChart(models.Model):
    project_name = models.CharField(max_length=255)
    chart_html = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.project_name
