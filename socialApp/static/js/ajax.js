$(document).ready(function(){
   
   $("#busy").effect("highlight", {}, 2000); 
   
   $('#conversations').on('click', 'li', function() {
    console.log('click registered');
    var id = $(this).attr('id');
    console.log(id);
      var parametros = {
         "conversation_id":id
         };  
         $.ajax({
            data: parametros,
            url:"/contact/",
            type: 'post',  
            success: function(response){
            $("#contact-profile").html(response);    
            },   
         }); 
         $.ajax({
            data: parametros,
            url:"/conversation/messages/",
            type: 'post',  
            beforeSend: function() {
            $("#messages").html("<div class='col-12'><img src='/static/img/loading2.gif'/><div>");
            },
            success: function(response){
            $("#messages").html(response);    
            },   
         }); 
   });                                  
});

