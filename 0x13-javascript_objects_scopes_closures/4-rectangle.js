#!/usr/bin/node

// this is a class
class Rectangle {
  constructor (w, h) {
    if (w === undefined || h === undefined) return this;
    if (w <= 0 || h <= 0) return this;
    this.width = w;
    this.height = h;
  }

  print () {
    const char = 'X';
    for (let i = 0; i < this.height; i++) {
      console.log(char.repeat(this.width));
    }
  }

  double () {
    this.width *= 2;
    this.height *= 2;
  }

  rotate () {
    [this.width, this.height] = [this.height, this.width];
  }
}

module.exports = Rectangle;
