from django.shortcuts import render

# Create your views here.
def index(request):
    cookie_info = request.COOKIES   # 모든 쿠키정보 가져오기
    test_id = request.COOKIES.get('test','')    # 쿠키정보 1개 읽기 >> None은 ''으로 처리
    
    context = {'cookie_info':cookie_info}
    response =  render(request,'index.html',context)
    if test_id == '':
        response.set_cookie('test','aaa')   # 쿠키 1개 저장 >> max_age 설정 안하면 브라우저 종료 시 삭제
        print('test쿠키 저장')
    else:
        response.delete_cookie('test')  # 쿠키 삭제
        print('test쿠키 삭제')
    
    return response