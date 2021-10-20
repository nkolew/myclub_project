from django.shortcuts import render
from django.http import HttpResponse
from datetime import date
import calendar
from calendar import HTMLCalendar


def index(request, year=date.today().year, month=date.today().month):
    year = int(year)
    month = int(month)
    if not (2000 <= year <= 2099):
        year = date.today().year
    month_name = calendar.month_name[month]
    title = f"MyClub Event Calendar - {month_name} {year}"
    cal = HTMLCalendar().formatmonth(year, month)
    return HttpResponse(f"<h1>{title}</h1><p>{cal}</p>")
