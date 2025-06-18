from django.shortcuts import render
from django.http import HttpResponse
import requests
import json

# Create your views here.
def list_p3(request):
    service_key = '6c5ddcf429f5f5c5f3cd05571911c14e'
    url = f'https://kobis.or.kr/kobisopenapi/webservice/rest/boxoffice/searchDailyBoxOfficeList.json?key={service_key}&targetDt=20250617'
    
    response = requests.get(url) 
    json_data = json.loads(response.text)
    
    # print(json_data)
    
    mlist = json_data['boxOfficeResult']['dailyBoxOfficeList']
    
    print(mlist)
    
    context = {'list':mlist}
    return render(request, 'pboard3/list_p3.html',context)



def view(request,movieCd):
    service_key = '6c5ddcf429f5f5c5f3cd05571911c14e'
    url = f'https://kobis.or.kr/kobisopenapi/webservice/rest/boxoffice/searchDailyBoxOfficeList.json?key={service_key}&targetDt=20250617'
    
    response = requests.get(url) 
    json_data = json.loads(response.text)
    
    # print(json_data)
    
    mlist = json_data['boxOfficeResult']['dailyBoxOfficeList']
    
    for m in mlist:
        if m['movieCd'] == movieCd:
            context = {'movie':m}        
            return render(request, 'pboard3/view.html',context)
        
    return HttpResponse("잘못된 접근입니다.")