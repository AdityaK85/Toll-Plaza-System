import {log, callAjax, sweetAlertMsg, showToastMsg , fieldsValidator } from '../CommonJS/common.js';



$('#myModal').on('shown.bs.modal', function () {
    $('#myInput').trigger('focus')
})


window.showUserModel = function(email, phone , discription ) {
    $(`#email`).val(email)
    $(`#phone`).val(phone)
    $(`#discription`).val(discription)
    var model = new bootstrap.Modal(document.getElementById('exampleModal'))
    model.show()
  }

window.RequestModel = function(user_id) {
    var model = new bootstrap.Modal(document.getElementById('requestModel'))
    model.show()
  }



window.ChangePwd = async function(user_id){
    var reason_txt = $("#reason_txt").val()
    var data = {
        'reason_txt': reason_txt,
        'user_id': user_id
    }
    var response = await callAjax('/Changed_pwd/' , data , this , 'Sending' , 'Request Send' )
    if (response.status == 1){
        await showToastMsg('Success', response.msg , 'success')
    }
    else{
        await showToastMsg('Error', 'Something went wrong ! Please try again later')
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