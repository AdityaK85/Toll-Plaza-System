import {log, callAjax, sweetAlertMsg, showToastMsg} from '../CommonJS/common.js';



window.LoginUser = async function(){
    var username = $("#username").val()
    var password = $("#password").val()

    if (username.trim() == "") {
        showToastMsg('Error','Please Enter Username', 'error')
    }
    else if (password.trim() == '') {
        showToastMsg('Error','Please Enter Password', 'error')
    }
    else {
        var data = {
            'username':username,
            'password':password
        }
        
        var response = await callAjax('/UserLogin/', data )
        if (response.status == 1){
            if (response.type == 'Admin') {

                location.href = '/Dashboard'
            }
            else{
                
                location.href = '/register_vehicle'
            }
        }
        else {
            showToastMsg('Error', "Invalid Credentials", 'error')
        }
    }
}