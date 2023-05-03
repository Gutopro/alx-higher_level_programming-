// script that fetches and prints how to say “Hello” depending on the language

$(document).ready(function () {
    const url = 'https://fourtonfish.com/hellosalut/';
    $('#btn_translate, #language_code').click(() => {
	$.ajax({
	    url: url,
	    type: 'GET',
	    data: { lang: $('#language_code').val() },
	    success: (response) => {
		$('#hello').html(response.hello);
	    },
	    error: () => {
		$('#hello').html('Error');
	    },
	});
    });
});
