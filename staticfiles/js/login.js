$(document).ready(function() {
    $('#login-form').submit(function(event) {
        event.preventDefault();
        var form = $(this);
        var formData = form.serialize(); // Сериализация формы
        $.ajax({
            type: 'POST',
            url: '/login/',
            data: formData,
            headers: {
                'X-CSRFToken': getCookie('csrftoken') // Установка CSRF токена в заголовке запроса
            },
            success: function(response) {
                $('#login-result').html('<div class="alert alert-success">' + response.message + '</div>');
                setTimeout(function() {
                    window.location.href = '/empty-page/';
                }, 2000);
            },
            error: function(xhr, errmsg, err) {
                $('#login-result').html('<div class="alert alert-danger">' + xhr.responseJSON.error + '</div>');
            }
        });
    });
});

// Функция для получения CSRF токена из cookie
function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Если нашли cookie с нужным именем, извлекаем его значение
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
