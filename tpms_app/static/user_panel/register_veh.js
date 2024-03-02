import {log, callAjax, sweetAlertMsg, showToastMsg , fieldsValidator } from '../CommonJS/common.js';


$("#veh_tbl").DataTable()

window.SaveDetails = async function(val_id){
    var fields = await fieldsValidator(['vehicle_no','vehicle_type','owner_info', 'registration_no','vehicle_color','payment_pefernce','insurance'])
    if (fields){
        var data = new FormData;
        for ( var key in fields) {
            data.append(key, fields[key])
        }

        data.append('val_id', val_id )
        var response = await callAjax('/Save_Vehicle_Details/' , data , null , null , null , true )
        if (response.status == 1){
            var msg = (val_id != '') ? 'Modified' : 'Registered'
            var preference = await sweetAlertMsg( msg, response.msg , 'success', 'cancel', 'OK')
            if (preference) {
                location.href = '/manage_vehicle'
            }
        }
    }
}


window.delete_recored = async function(id) {
    var preference = await sweetAlertMsg( 'Delete Vehicle Record', 'Do you want to delete this Vehicle Record' , 'question', 'cancel', 'Yes')
    if (preference) {
        var response = await callAjax('/Delete_Record/', {'id':id})
        if (response.status == 1) {
            showToastMsg('Deleted', 'Vehicle Record Successfully Removed From System', 'success')
            await new Promise(resolve => setTimeout(resolve , 1200));
            location.reload()
        }   
        else {
            showToastMsg('Error', 'Something went wrong', 'error')
        }
    }
}


