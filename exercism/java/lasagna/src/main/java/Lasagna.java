public class Lasagna {

    public int expectedMinutesInOven() {
        return 40;
    }

    public int remainingMinutesInOven(int minutesInTheOven) {
        return expectedMinutesInOven() - minutesInTheOven;
    }

    public int preparationTimeInMinutes(int numberOfLayers) {
        return numberOfLayers * 2;
    }

    public int totalTimeInMinutes(int numberOfLayers, int minutesInTheOven) {
        return preparationTimeInMinutes(numberOfLayers) + minutesInTheOven;
    }
}
