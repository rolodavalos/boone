$(document).ready(function(){
   $("#sendButton").on('click', function (e)  {
    e.preventDefault(); // avoid to execute the actual submit of the form.
    var form = $("#formConversation")
    var url = form.attr('action');
    $.ajax({
           type: "POST",
           url: url,
           data: form.serialize(), // serializes the form's elements.
           beforeSend: function() {
            $("#messages").html("<div class='col-12'><img src='/static/img/loading3.gif'/><div>");
            },
           success: function(response){
            $("#messages").html(response);    
            },    
         });   
   });
   
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
            $("#messages").html("<div class='col-12'><img src='/static/img/loading3.gif'/><div>");
            },
            success: function(response){
            $("#messages").html(response);    
            },   
         }); 
   });                                  
});

