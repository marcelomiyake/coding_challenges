export function decodedResistorValue(colors: string[]) {
  const resistance = (getValue(colors[0]) * 10 + getValue(colors[1])) * Math.pow(10, getValue(colors[2]));
  if (resistance >= 1000) {
    return (resistance / 1000).toString() + " kiloohms";
  }
  return resistance.toString() + " ohms";
}

function getValue(color: string): number {
  switch (color) {
    case 'black':
      return 0;
    case 'brown':
      return 1;
    case 'red':
      return 2;
    case 'orange':
      return 3;
    case 'yellow':
      return 4;
    case 'green':
      return 5;
    case 'blue':
      return 6;
    case 'violet':
      return 7;
    case 'grey':
      return 8;
    case 'white':
      return 9;
    default:
      return -1;
  }
}
