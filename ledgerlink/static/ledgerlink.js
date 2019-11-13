
function crud_form_loaded(formName, action){
    if(formName === "VslaForm"){
        vsla_form_loaded();
    }
}

function vsla_form_loaded(){

    var vslaCode = generateVslaCode(4) + "" + new Date().getUTCFullYear() + "" + (new Date().getMonth()+1) + "" + new Date().getDate() + "" + new Date().getMilliseconds();
    if($("#id_VslaCode").val().length === 0) {
        $("#id_VslaCode").val(vslaCode);
    }
    $("#id_VslaCode").prop("readonly", true);
}

function generateVslaCode(length) {
   var result           = '';
   var characters       = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ';
   var charactersLength = characters.length;
   for ( var i = 0; i < length; i++ ) {
      result += characters.charAt(Math.floor(Math.random() * charactersLength));
   }
   return result;
}