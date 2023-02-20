export class Triangle {

  sides: number[];

  constructor(...sides: number[]) {
    this.sides = sides;
  }

  get isEquilateral() {
    return this.sides[0] > 0 && this.sides[0] == this.sides[1] && this.sides[1] == this.sides[2];
  }

  get isIsosceles() {
    return this.sides[0] < this.sides[1] + this.sides[2]
      && this.sides[1] < this.sides[2] + this.sides[0]
      && this.sides[2] < this.sides[0] + this.sides[1]
      && (this.sides[0] == this.sides[1] || this.sides[1] == this.sides[2] || this.sides[2] == this.sides[0]);
  }

  get isScalene() {
    return this.sides[0] < this.sides[1] + this.sides[2]
      && this.sides[1] < this.sides[2] + this.sides[0]
      && this.sides[2] < this.sides[0] + this.sides[1]
      && this.sides[0] != this.sides[1] && this.sides[1] != this.sides[2] && this.sides[2] != this.sides[0];
  }
}
