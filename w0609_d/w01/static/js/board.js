function writeBtn(){
    if('{{request.session.session_id}}'){
        alert('alert')
    }
        

    // alert('ㅇ');
    if($('.btitle').val().len<1){
        alert('제목을 입력하세요.');
        $('.btitle').focus();
        return;
    }
    writefrm.submit();
}

