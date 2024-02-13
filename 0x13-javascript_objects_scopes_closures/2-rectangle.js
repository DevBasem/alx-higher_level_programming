#!/usr/bin/node

// this is a class
class Rectangle {
  constructor (w, h) {
    if (w === undefined || h === undefined) return this;
    if (w <= 0 || h <= 0) return this;
    this.width = w;
    this.height = h;
  }
}

module.exports = Rectangle;
