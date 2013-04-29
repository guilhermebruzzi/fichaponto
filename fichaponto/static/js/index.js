$(document).ready(function(){
    $('#content').on('submit', '#fichaponto-form', function(event){
        var email = $('#email');
        var empresa = $('#empresa');

        if(typeof ga != "undefined"){
            ga('send', 'event', 'Cadastro', 'Cadastro da empresa ' + empresa.val().trim(), 'Email: ' + email.val().trim());
        }

        if (email.val().trim() == "" || empresa.val().trim() == ""){
            $("#erro").removeClass("hidden");
            event.preventDefault();
            return false;
        }
        return true
    });

    $('body').on('click', '#logo-link', function(){
        var currentUrl = window.location.href;
        ga('send', 'event', 'Home', 'Home Logo', currentUrl);
    });

    $('body').on('click', '#envie-email-para', function(){
        var currentUrl = window.location.href;
        ga('send', 'event', 'Email', 'Envie email para', currentUrl);
    });
});
