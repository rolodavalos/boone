{% load static %} 
function display_message(conversation_id){
  var parametros = {
    "conversation_id":conversation_id
  };
  $.ajax({
    data: parametros,
    url:"{%url 'display_messages'%}",
    type: 'post',  
    beforeSend: function() {
       $("#messages_container").html("<div class='col-12'><img src='{% static 'img/loading-icon.gif' %}'/><div>");
    },
    success: function(response){
      $("#messages_container").html(response);    
    },
  }); 
}
