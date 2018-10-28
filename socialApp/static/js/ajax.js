$(document).ready(function(){
   $('#conversations').on('click', 'li', function() {
    console.log('click registered');
    var id = $(this).attr('id');
    console.log(id);  
    });                             
});

