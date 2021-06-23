$(document).ready(function(){
    $('#id_website').change(function(){
        $('#id_type').children('option').each(function() {$(this).remove()});

        if (!$(this).val()) {
            return;
        }

        $.ajax({
            url: "/services/service-type/",
            data: {"website": $(this).val()},
            success: function(data) {
                data.forEach(service_type => $('#id_type').append(
                    new Option(service_type.name + ' (' + service_type.price + '₽)', service_type.id)
                ));
            }
        });
    });

    $('form').change(function() {
        website = $('#id_website').val();
        type = $('#id_type').val();
        specialist = $('#id_specialist').val();
        count = $('#id_count').val();
        promo_code = $('#id_promo_code').val();
        if (!!website & !!type.length & !!specialist & !!count) {
            $.ajax({
                type: 'GET',
                url: '/services/api/result_sum/',
                data: {'website': website, 'type': type, 'specialist': specialist, 'count': count, 'promo_code': promo_code},
                success: function(data) {
                    $('.itog').remove();
                    $('.label_itog').append('<span class="itog">'+data+' ₽</span>');
                }
            });
        }
    });
});
