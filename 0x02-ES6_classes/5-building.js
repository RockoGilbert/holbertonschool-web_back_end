export default class Building {
  constructor(sqft) {
    this._sqft = sqft;

    if (this.constructor !== Building && !this.evacuationWarningMessage) {
      throw new Error(
        // eslint-disable-next-line comma-dangle
        'Class extending Building must override evacuationWarningMessage'
      );
    }
  }

  get sqft() {
    return this._sqft;
  }

  set sqft(val) {
    this._sqft = val;
  }
}
