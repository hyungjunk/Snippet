// Ternary Operator
var drink = age >= 18 ? 'beer' : 'juice';

// Switch Statement
switch (true){
  case age < 13:
    console.log(firstName + ' is a boy.');
    break;
  case age >= 13 && age < 20:
    console.log(firstName + ' is a teenager.');
    break;
  case age >= 20 && age < 30:
    console.log(firstName + ' is a young man');
    break;
  default:
    console.log('This always run?');
    console.log('No, only when not any condition meets defined above.');
}

// data selector
$('div').data('product-id') // is equivalent to
document.querySelector('div').dataset.productId // Wow!
