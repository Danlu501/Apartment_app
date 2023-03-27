$(document).ready(function(){
  $('.open-popup').click(function(){
    $.ajax({
      type: 'GET',
      url: "/new",
      success: function(data){
        $('.popup-content').html(data);
        $('.popup').show();
      }
    });
  });
});