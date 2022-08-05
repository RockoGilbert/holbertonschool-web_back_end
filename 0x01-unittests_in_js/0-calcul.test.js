const calculateNumber = require('./0-calcul.js');
const assert = require('assert');

describe('calculateNumber', () => {
  it('checks the output', () => {
    assert.equal(calculateNumber(1, 3), 4);
    assert.equal(calculateNumber(1, 3.7), 5);
    assert.equal(calculateNumber(1.2, 3.7), 5);
    assert.equal(calculateNumber(1.5, 3.7), 6);
    assert.equal(calculateNumber(3.7, 1), 5);
    assert.equal(calculateNumber(3.7, 1.2), 5);
  });
  it('negative numbers', () => {
    assert.equal(calculateNumber(-1, 1), 0);
    assert.equal(calculateNumber(1, -1), 0);
    assert.equal(calculateNumber(-1, -1), -2);
  });
});

describe('calculateNumber', () => {
  it('checks the output', () => {
  
    assert.equal(calculateNumber(1, 3), 4);
    assert.equal(calculateNumber(1, 3.7), 5);
    assert.equal(calculateNumber(1.2, 3.7), 5);
    assert.equal(calculateNumber(1.5, 3.7), 6);
    assert.equal(calculateNumber(3.7, 1), 5);
    assert.equal(calculateNumber(3.7, 1.2), 5);
  });
  it('negative numbers', () => {
    assert.equal(calculateNumber(-1, 1), 0);
    assert.equal(calculateNumber(1, -1), 0);
    assert.equal(calculateNumber(-1, -1), -2);
  });
});