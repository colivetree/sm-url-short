var API_URL = "http://localhost:8080/api/v1/";
var SHORTEN_URL = "shorten/";

$(document).ready(function(){


$("#shorten_url_link").click(function(){

json_data=JSON.stringify({"full_URL":$("#url_to_shorten").val()});

$.ajax({
  type: "POST",
  url: API_URL+SHORTEN_URL,
  data: json_data,
  success: function (data) {
       $("#new_url_area").html("<a href=\""+data.short_URL+"\">"+data.short_URL+"</a>");
  },
  error: function (error) {
    alert("error "+error);
  },
  dataType: "jsonp",
  contentType: 'application/json',
});	
});

});


