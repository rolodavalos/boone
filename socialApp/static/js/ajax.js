$(document).ready(function(){
   $('#conversations').on('click', 'li', function() {
    console.log('click registered');
    var id = $(this).attr('id');
    console.log(id);
      
      var parametros = {
         "conversation_id":id
         };  
         $.ajax({
            data: parametros,
            url:"/conversation/messages/",
            type: 'post',  
            success: function(response){
            $("#messages_container").html(response);    
            },   
         }); 
      setInterval(function() {
         $(this).trigger('click');
      },5000);
   });                             
});

