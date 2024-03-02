import {log, callAjax, sweetAlertMsg, showToastMsg , fieldsValidator } from '../CommonJS/common.js';


window.SaveDetails = async function(val_id){
    var fields = await fieldsValidator(['vehicle_type','toll_amt','valid_toll_hr'])
    if (fields){
        var data = new FormData;
        for ( var key in fields) {
            data.append(key, fields[key])
        }

        data.append('val_id', val_id )
        var response = await callAjax('/Save_Toll_info/' , data , null , null , null , true )
        if (response.status == 1){
            var msg = (val_id != '') ? 'Modified' : 'Registered'
            var preference = await sweetAlertMsg( msg, response.msg , 'success')
            if (preference) {
                location.reload()
            }
        }
    }
}


window.delete_recored = async function(id) {
    var preference = await sweetAlertMsg( 'Delete Toll Record', 'Do you want to delete this Toll Record' , 'question', 'cancel', 'Yes')
    if (preference) {
        var response = await callAjax('/Delete_Toll_Record/', {'id':id})
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


