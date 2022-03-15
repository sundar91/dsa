const reverse = (str) => {

  if(!str || str.length < 2 || typeof str !== 'string')
    return 'bad string';

  let charArray = [];
  let len = str.length - 1;
  for(let i = len; i >= 0; i--){
    charArray.push(str[i]);
  }
  return charArray.join('');
}

console.log(reverse('sundar'));