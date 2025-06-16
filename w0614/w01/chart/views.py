from django.shortcuts import render
from chart.models import Profit

# Create your views here.

# 차트페이지 호출
def chlist(request):
    qs = Profit.objects.filter(year=24)
    print(qs)
    qs_list = list(qs.values())
    p_list = []
    m_list = []
    for d in qs_list:
        p_list.append(d['profit'])
        m_list.append(d['monthly'])
    context = {'profit':p_list,'monthly':m_list}
    return render(request,'chart/chlist.html',context)