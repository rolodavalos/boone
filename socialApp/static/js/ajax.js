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
            success: function(response){
            $("#messages").html(response);    
            },   
         }); 
   });
   
      setInterval(funcgtion(){
           $.ajax({
            url:"/conversations/",  
            success: function(response){
            $("#contacts_content").html(response);    
            },   
         });                      
      },5000);
           
});

