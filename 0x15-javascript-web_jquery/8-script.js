// script that fetches and lists the title for all movies by using this URL: https://swapi-api.alx-tools.com/api/films/?format=json

$(document).ready(function() {
    $.getJSON('https://swapi-api.alx-tools.com/api/films/?format=json', function(data) {
	$.each(data.results, function(index, movie) {
	    $('#list_movies').append('<li>' + movie.title + '</li>');
	});
    });
});
