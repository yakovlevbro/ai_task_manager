$(document).ready(function() {
    $('#registration-form').submit(function(event) {
        event.preventDefault();
        var form = $(this);
        var formData = form.serializeArray();
        formData.push({name: 'csrfmiddlewaretoken', value: $('input[name=csrfmiddlewaretoken]').val()});
        $.ajax({
            type: 'POST',
            url: '/register/',
            data: formData,
            success: function(response) {
                $('#registration-result').html('<div class="alert alert-success">' + response.message + '</div>');
                setTimeout(function() {
                    window.location.href = '/empty-page/';  // Redirect to empty page after successful registration
                }, 2000);
            },
            error: function(xhr, errmsg, err) {
                $('#registration-result').html('<div class="alert alert-danger">' + xhr.responseJSON.error + '</div>');
            }
        });
    });
});
