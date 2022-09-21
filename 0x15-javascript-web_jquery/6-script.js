const $headerElem = $('header');
const $update_header = $('DIV#update_header');
$update_header.on('click', function () {
  $headerElem.text('New Header!!!');
});
