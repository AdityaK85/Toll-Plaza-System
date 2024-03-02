import {log, callAjax, sweetAlertMsg, showToastMsg , fieldsValidator } from '../CommonJS/common.js';

window.Get_Tax_Details = async function(value) {
    var value = $(value).find("option:selected")
    var selectedId = value.data('id')
    var response = await callAjax('/Get_Tax_Amout/', {'value':selectedId})
    if (response.status == 1) {
        $("#fee_sehedule").val(response.response_amount)
    }
}


window.ClearAllFields = function() {
    var field = document.querySelectorAll('input', 'select')
    field.forEach(function(val){
        val.value = ''
    }) 
}


window.CashCollected = async function(){
    var fields = await fieldsValidator(['vehicle_identification','vehicle_type','fee_sehedule', 'veh_no','payment_by','state','addr' , 'lane_code'])
    if (fields){
        var data = new FormData;
        for ( var key in fields) {
            data.append(key, fields[key])
        }
        var response = await callAjax('/CashCollected/' , data , null , null , null , true )
        if (response.status == 1){
            showToastMsg('Success' , response.msg , 'success')
            // location.reload()
            ClearAllFields()
        }
    }
}
