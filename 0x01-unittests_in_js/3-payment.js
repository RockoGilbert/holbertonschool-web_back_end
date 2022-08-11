// Utils payment module
const Utils = require('./utils');

const sendPaymentRequestToApi = (totalAmount, totalShipping) => {
  const total = Utils.calculateNumber("sum", totalAmount, totalShipping);
  console.log(`The total is: ${total}`);
};

module.exports = sendPaymentRequestToApi;
