// script that adds a <li> element to a list when the user clicks on the tag DIV#add_item:

$(document).ready(function () {
    $('#add_item').click(function () {
	$('.my_list').append('<li>Item</li>');
    });
});
