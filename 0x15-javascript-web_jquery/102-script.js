//script that fetches and prints how to say “Hello” depending on the language

$(document).ready(function () {
    $('#btn_translate').click(function () {
	const languageCode = $('#language_code').val();
	$.get(`https://www.fourtonfish.com/hellosalut/hello/${languageCode}`, function (data) {
	    $('#hello').text(data.hello);
	});
    });
});
