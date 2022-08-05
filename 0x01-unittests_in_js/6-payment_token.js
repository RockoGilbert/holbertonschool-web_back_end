// The function will take an argument called success

const getPaymentTokenFromAPI = async (success) => {
  if (success) {
    return { data: 'Successful response from the API' };
  }
}

module.exports = getPaymentTokenFromAPI;