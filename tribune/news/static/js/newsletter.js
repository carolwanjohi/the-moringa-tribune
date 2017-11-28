// Calls AJAX function

$(document).ready(function(){

    $('form').submit(function(event){

        // Prevent default for the newsletter form to call the news_today function

        event.preventDefault()

        // Target the form
        form = $("form")

        // Create AJAX function
        $.ajax({
            'url':'/ajax/newsletter',
            'type':'POST',
            'data': form.serialize(),
            'dataType': 'json',
            'success':function(data){
                alert(data['success'])
            }
        }) // End of AJAX method

        // Clear form fields
        $('#id_your_name').val('')
        $('#id_email').val('')

    }) // End of submit event

}) // End of document ready function

/*

AJAX function

$.ajax({
    // Same url in URLConf 
    'url': '/url',

    // Type of request
    'type': 'POST/GET',

    // Data attribute : what we are passing to the request
    'data': form.serialize(),

    // Serialize function : converts form values into a JSON that can be passed into the request
    'dataType':'json',

    // Successful AJAX request --> alert the user it was successful

    'success':function(data){
        alert(data['success'])
    }
})

*/ 