function calculateNumber(a, b) {
  if (isNaN(a) || isNaN(b)) throw TypeError("Hey girl");  
  const aRound = Math.round(a);
  const bRound = Math.round(b);

  return aRound + bRound;
}

module.exports = calculateNumber;