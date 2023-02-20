class Lasagna
{
    public int ExpectedMinutesInOven()
    {
        return 40;
    }

    public int RemainingMinutesInOven(int actualMinutesInTheOven)
    {
        return ExpectedMinutesInOven() - actualMinutesInTheOven;
    }

    public int PreparationTimeInMinutes(int numberOfLayers)
    {
        return numberOfLayers * 2;
    }

    public int ElapsedTimeInMinutes(int numberOfLayers, int minutesInTheOven)
    {
        return PreparationTimeInMinutes(numberOfLayers) + minutesInTheOven;
    }
}
