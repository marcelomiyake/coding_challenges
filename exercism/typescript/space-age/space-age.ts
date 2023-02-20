export function age(planet: string, seconds: number): number {
  const EARTH_PERIOD = 31557600;

  let orbitalAge = (seconds: number, period: number): number => Number((seconds / EARTH_PERIOD / period).toFixed(2));

  switch (planet) {
    case "earth":
      return orbitalAge(seconds, 1.0);
    case "venus":
      return orbitalAge(seconds, 0.6151972);
    case "mercury":
      return orbitalAge(seconds, 0.2408467);
    case "mars":
      return orbitalAge(seconds, 1.8808158);
    case "jupiter":
      return orbitalAge(seconds, 11.862615);
    case "saturn":
      return orbitalAge(seconds, 29.447498);
    case "uranus":
      return orbitalAge(seconds, 84.016846);
    case "neptune":
      return orbitalAge(seconds, 164.79132);
    default:
      return 0.0;
  }
}
