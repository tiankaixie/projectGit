from django.shortcuts import render,get_list_or_404,get_object_or_404
#from django.template import loader, Context
#from django.http import HttpResponse
from website.models import HistoryPeriod, History
from django.core import serializers
from django.views.decorators.cache import cache_page
import json
# Create your views here.
#@cache_page(60 * 15)
def index(request):
	if not 'historycategory' in request.session:
		historycategorytemp = serializers.serialize("json", History.objects.all())
		request.session["historycategory"] = historycategorytemp
	historycategory =json.loads(request.session["historycategory"])
	return render(request,'index.html',
		{"tittle": "HOME",
		"historycategory":historycategory
		})

#@cache_page(60 * 15)
def historyList(request):
	if not 'historycategory' in request.session:
		historycategorytemp = serializers.serialize("json", History.objects.all())
		request.session["historycategory"] = historycategorytemp
	historycategory =json.loads(request.session["historycategory"])
	return render(request,'historylist.html',
		{"tittle": "History",
		"historycategory":historycategory
		})

#@cache_page(60 * 15)
def particularHistory(request,history_id):
	if not 'historycategory' in request.session:
		historycategorytemp = serializers.serialize("json", History.objects.all())
		request.session["historycategory"] = historycategorytemp
	historycategory =json.loads(request.session["historycategory"])
	history = get_object_or_404(History,pk = history_id)
	periods = get_list_or_404(HistoryPeriod,belongTo_id = history_id)
	return render(request,'particularHistory.html',
		{"tittle": history.name,
		"periods":periods,
		"history":history,
		"historycategory":historycategory})

#@cache_page(60 * 15)
def particularPeriod(request,period_id):
	if 'historycategory' not in request.session:
		historycategorytemp = serializers.serialize("json", History.objects.all())
		request.session["historycategory"] = historycategorytemp
	historycategory =json.loads(request.session["historycategory"])
	period = get_object_or_404(HistoryPeriod,pk = period_id)
	events = period.events.all()
	history = get_object_or_404(History,pk = period.belongTo_id)
	periods = history.periods.all()
	print(periods)
	#print(period.events)
	return render(request,'particularPeriod.html',
		{"tittle": period.name,
		"particularPeriod":period,
		"historycategory":historycategory,
		"events":events,
		"periods":periods
		})
