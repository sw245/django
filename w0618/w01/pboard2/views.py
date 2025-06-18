from django.shortcuts import render
import requests
import json




# Create your views here.
def list_p2(request):
    
    pageNo = 17
    service_key = '%2FjAVLJGJZwHZGVorf%2Fajiyz7RdhV3oK%2Fblc9UUxnyUtQHw6smo%2B%2BPq4zUs4viIvtUAxG6Zj3YNu%2Bnt6xQ8WnZw%3D%3D'
    url = f'http://apis.data.go.kr/B551011/PhotoGalleryService1/galleryList1?serviceKey={service_key}&numOfRows=10&pageNo={pageNo}&MobileOS=ETC&MobileApp=AppTest&arrange=A&_type=json'
    
    # 공공데이터 가져오기
    response = requests.get(url)    # 공공데이터 타입 >> strrrrrr
    json_data = json.loads(response.text) # json타입으로 변경 -- dict 타입
    
    dlist = json_data['response']['body']['items']['item']
    context = {'list':dlist}
    
    return render(request,'pboard2/list_p2.html',context)


def view(request):
    return render(request,'pboard2/view.html')