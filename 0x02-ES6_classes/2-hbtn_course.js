export default class HolbertonCourse {
  constructor(name, length, students) {
    if (typeof name !== 'string') throw TypeError('Name must be a string');
    if (typeof length !== 'number') throw TypeError('Length must be a number');
    const isBad = students.some((student) => typeof student !== 'string');
    if (!Array.isArray(students) && isBad) {
      throw TypeError('Students must be an array of strings');
    }

    this._name = name;
    this._length = length;
    this._students = students;
  }

  get name() {
    return this._name;
  }

  set name(val) {
    if (typeof val === 'string') this._name = val;
    else throw TypeError('Name must be a string');
  }

  get length() {
    return this._length;
  }

  set length(val) {
    if (typeof val === 'number') this._length = val;
    else throw TypeError('Length must be a number');
  }

  get students() {
    return this._students;
  }

  set students(arr) {
    const isGood = arr.every((student) => typeof student === 'string');
    if (Array.isArray(arr) && isGood) this._students = arr;
    else throw TypeError('Students must be an array of strings');
  }
}
