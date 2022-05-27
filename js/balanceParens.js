balanceParens = (str) =>
{
  // array for indices of right parens unmatched with left parens	
  let loneRight = [];	
  // array for indices of right parens, matched or not	
  let stack = [];	
  for (let i = 0; i < str.length; i++) {	
    // if left paren, push index to stack	
    if (str[i] === '(') {	
      stack.push(i);	
    } else if (str[i] === ')') {	
      // if unmatched right paren, push index to array	
      if (stack.length === 0) {	
        loneRight.push(i);	
        // otherwise, remove corresponding left paren	
      } else {	
        stack.pop();	
      }	
    }	
  }	
  str = str.split('');	
  // concat to create array of unmatched left and right parens	
  loneRight = loneRight.concat(stack);	
  // iterate and replace unmatched left and right parens with ''	
  for (let i = 0; i < loneRight.length; i++) {	
    str[loneRight[i]] = '';	
  }	
  // join array into string and return	
  return str.join('');
}

//console.log(balanceParens(")(())("))

module.exports = { balanceParens }