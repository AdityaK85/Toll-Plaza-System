import {log, callAjax, sweetAlertMsg, showToastMsg , fieldsValidator } from '../CommonJS/common.js';



$('#myModal').on('shown.bs.modal', function () {
    $('#myInput').trigger('focus')
})


window.showUserModel = function(email , phone , about) {
    $("#email").val(email)
    $("#phone").val(phone)
    $("#discription").val(about)
    var model = new bootstrap.Modal(document.getElementById('exampleModal'))
    model.show()
  }


window.RequestModel = function() {
    var model = new bootstrap.Modal(document.getElementById('requestModel'))
    model.show()
  }

window.SendRequest = async function(user_id){
    var request_txt = $("#request_text").val()
    if (request_txt.trim() == ""){
        showToastMsg("Error", "Please Enter Reason For Changing Password")
        request_txt.focus()
    }
    else{
        var data = {
            'user_id' : user_id ,
            'request_txt' : request_txt
        }
        var response = await callAjax('/SendRequest/', data)
        if (response.status == 1) {
            showToastMsg("Success" , response.msg , 'success')
            await new Promise(resolve => setTimeout(resolve , 1200));
            location.reload()

        }
        else {
            showToastMsg("Error" , 'Something went wrong' , 'error')
        }

    }
}




  window.SaveChanges = async function(user_id, user){

    var email = $("#email").val()
    var phone = $("#phone").val()
    var discription = $("#discription").val()
    var profile = document.getElementById('profile').files[0]
    
    if (email.trim() == "" )
    {
        showToastMsg('Error', 'Please enter email', 'error')
        $("#email").focus();
    }
    else if (phone.trim() == "" )
    {
        showToastMsg('Error', 'Please enter phone', 'error')
        $("#phone").focus();
    }
    else {

        var data = new FormData;
        data.append('user_id' , user_id)
        data.append('user' , user)
        data.append('email' , email)
        data.append('phone' , phone)
        data.append('discription' , discription)
        data.append('profile' , profile)

        var response = await callAjax('/Save_Profile_Changes/' , data , null , null , null , true )
        if (response.status == 1){
            location.reload()
        }
        else{
            await showToastMsg('Error', 'Something went wrong ! Please try again later')
        }
    }
}