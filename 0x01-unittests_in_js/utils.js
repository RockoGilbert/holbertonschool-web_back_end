// Utils module!

const Utils = {
  calculateNumber(type, a, b) {
    const whichType = type.toLowerCase();
    if (isNaN(a) || isNaN(b)) throw new TypeError('Arguments must be numbers');

    switch (whichType) {
      case 'sum':
        // console.log(typeof("sum"), Math.round(a) + Math.round(b));
        return Math.round(a) + Math.round(b);
      case 'subtract':
        return Math.round(a) - Math.round(b);
      case 'divide':
        // console.log(typeof(type), Math.round(a) / Math.round(b));
        if (Math.round(b) === 0) return 'Error';
        return Math.round(a) / Math.round(b);
      default:
        throw new TypeError('Arguments must be SUM, SUBTRACT or DIVIDE');
    }
  }
};
// console.log(Utils.calculateNumber('DIVIDE', 4, 0));
// console.log(Utils.calculateNumber('DIVIDE', 4, 36) );
module.exports = Utils;
