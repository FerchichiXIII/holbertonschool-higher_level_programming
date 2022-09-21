const $headerElem = $('header');
const $DIVred_header = $('DIV#red_header');
$DIVred_header.on('click', function () {
  $headerElem.addClass('red');
});
