class SpaceAge {
  static const earth_period = 31557600.0;

  double age({required String planet, required int seconds}) {
    switch (planet) {
      case "Earth":
        return double.parse(
            (seconds / earth_period).toDouble().toStringAsFixed(2));
      case "Venus":
        return double.parse(((seconds / earth_period).toDouble() / 0.6151972)
            .toStringAsFixed(2));
      case "Mercury":
        return double.parse(((seconds / earth_period).toDouble() / 0.2408467)
            .toStringAsFixed(2));
      case "Mars":
        return double.parse(((seconds / earth_period).toDouble() / 1.8808158)
            .toStringAsFixed(2));
      case "Jupiter":
        return double.parse(((seconds / earth_period).toDouble() / 11.862615)
            .toStringAsFixed(2));
      case "Saturn":
        return double.parse(((seconds / earth_period).toDouble() / 29.447498)
            .toStringAsFixed(2));
      case "Uranus":
        return double.parse(((seconds / earth_period).toDouble() / 84.016846)
            .toStringAsFixed(2));
      case "Neptune":
        return double.parse(((seconds / earth_period).toDouble() / 164.79132)
            .toStringAsFixed(2));
      default:
        return 0.0;
    }
  }
}
