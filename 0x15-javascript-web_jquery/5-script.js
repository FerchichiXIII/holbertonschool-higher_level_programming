const $list_elem = $('ul.my_list');
const $add_item_elem = $('div#add_item');
$add_item_elem.on('click', () => {
	$list_elem.append('<li>Item</li>');
	});
