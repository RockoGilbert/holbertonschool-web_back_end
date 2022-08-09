// Creates a function named calculateNumber. It should accepts two arguments (number) a and b
// The function should round a and b and return the sum of it

const calculateNumber = (a, b) => {
  if (isNaN(a) || isNaN(b)) throw new TypeError("Argument is not a number");
  return Math.round(a) + Math.round(b);
};

module.exports = calculateNumber;