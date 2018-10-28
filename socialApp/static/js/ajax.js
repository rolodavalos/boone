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
         beforeSend: function() {
         $("#messages_container").html("<div class='col-12'><img src='/static/img/loading-icon.gif'><div>");
         },
         success: function(response){
         $("#messages_container").html(response);    
         },   
      });    
   });                             
});

