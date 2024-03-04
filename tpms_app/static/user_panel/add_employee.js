import {log, callAjax, sweetAlertMsg, showToastMsg , fieldsValidator } from '../CommonJS/common.js';



window.AddEmployee = async function(this_, val_id){
    var fields = await fieldsValidator(['username','email','password'])
    if (fields){
        var data = new FormData;
        for ( var key in fields) {
            data.append(key, fields[key])
        }

        data.append('val_id', val_id )
        var response = await callAjax('/Add_Employee/' , data , this_ , 'Saving' , 'Saved' , true )
        if (response.status == 1){
            var preference = await sweetAlertMsg( 'Success', response.msg , 'success')
            if (preference) {
                location.href = '/employee'
            }
        }
    }
}



window.DeleteEmp = async function(id) {
    var preference = await sweetAlertMsg( 'Delete Employee', 'Do you want to delete this Employee Record' , 'question', 'cancel', 'Yes')
    if (preference) {
        var response = await callAjax('/Delete_Employee/', {'id':id})
        if (response.status == 1) {
            showToastMsg('Deleted', 'Employee Deleted Successfully', 'success')
            await new Promise(resolve => setTimeout(resolve , 1200));
            location.reload()
        }   
        else {
            showToastMsg('Error', 'Something went wrong', 'error')
        }
    }
}

window.blockUser = async function(id , type) {
    var preference = await sweetAlertMsg( `${type} Employee`, `Do you want to ${type} this employee` , 'question', 'cancel', 'Yes')
    if (preference) {
        var response = await callAjax('/Block_Employee/', {'user_id':id , 'type': type})
        if (response.status == 1) {
            showToastMsg(`${type}`, `Employee ${type} Successfully`, 'success')
            await new Promise(resolve => setTimeout(resolve , 1200));
            location.reload()
        }   
        else {
            showToastMsg('Error', 'Something went wrong', 'error')
        }
    }
}




window.NewPassModel = function(user_id) {
    $("#user_id").val(user_id)
    var model = new bootstrap.Modal(document.getElementById('NewPassModel'))
    model.show()
  }



  window.ChangePassword = async function() {
    var password = $('#password').val()
    var user_id = $('#user_id').val()
    if (password.trim() == '') {
        showToastMsg("Error", 'Please enter new password', 'error')
    }
    else{
        var preference = await sweetAlertMsg( 'Changed Password', 'Do you want to delete this Change the Password' , 'question', 'cancel', 'Yes')
        if (preference) {
        var response = await callAjax('/Change_Employee/', {'user_id':user_id , 'password': password})
        if (response.status == 1) {
            showToastMsg('Changed', 'Password Changed Successfully', 'success')
            await new Promise(resolve => setTimeout(resolve , 1200));
            location.reload()
        }   
        else {
            showToastMsg('Error', 'Something went wrong', 'error')
        }
    }
    }
}