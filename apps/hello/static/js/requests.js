// using jQuery
function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie != '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) == (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
var csrftoken = getCookie('csrftoken');

function csrfSafeMethod(method) {
    // these HTTP methods do not require CSRF protection
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}
$.ajaxSetup({
    beforeSend: function(xhr, settings) {
        if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
            xhr.setRequestHeader("X-CSRFToken", csrftoken);
        }
    }
});

$('#requests').on('mouseenter', function(){
    $.post( "/api/counter/", { 'reset': 1} );
    get_title();
});


/* AJAX request to requests */
function callServerAsync(){
    $.ajax({
    dataType: "json",
    url: '/api/requests/',
    success: function(response) {
        successCallback(response);
    }
});
};

function successCallback(responseObj){
    var transform = {'tag':'li','html':'Request method: ${request_method}; Full path: ${full_path}; Remote_addr: ${remote_addr}; http user agent: ${http_user_agent}; http referer: ${http_referer}; http accept language: ${http_accept_language}'};
    document.getElementById('requests').innerHTML = json2html.transform(responseObj,transform);
};

get_title();
function get_title(){
    $.getJSON('/api/counter/',function(data){
    document.title="(" + data['counter'] + ") Request Page | 42-test-skl1f";
});
} 

callServerAsync();
setInterval(callServerAsync,10000);
setInterval(get_title, 10000);