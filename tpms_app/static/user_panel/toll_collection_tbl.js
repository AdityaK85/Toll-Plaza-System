import {log, callAjax, sweetAlertMsg, showToastMsg , fieldsValidator } from '../CommonJS/common.js';


window.delete_recored = async function(id) {
    var preference = await sweetAlertMsg( 'Delete Record', 'Do you want to delete this Toll Collected Record' , 'question', 'cancel', 'Yes')
    if (preference) {
        var response = await callAjax('/Delete_Toll_Collected_Record/', {'id':id})
        if (response.status == 1) {
            showToastMsg('Deleted', response.msg , 'success')
            await new Promise(resolve => setTimeout(resolve , 1200));
            location.reload()
        }   
        else {
            showToastMsg('Error', 'Something went wrong', 'error')
        }
    }
}