#if !defined(SPACE_AGE_H)
#define SPACE_AGE_H

namespace space_age {

    class space_age {

    private:
        double _seconds;

        const double EARTH_YEAR = 31557600;

        const double MERCURY_YEAR = 0.240846 * EARTH_YEAR;

        const double VENUS_YEAR = 0.61519726 * EARTH_YEAR;

        const double MARS_YEAR = 1.8808158 * EARTH_YEAR;

        const double JUPITER_YEAR = 11.862615 * EARTH_YEAR;

        const double SATURN_YEAR = 29.447498 * EARTH_YEAR;

        const double URANUS_YEAR = 84.016846 * EARTH_YEAR;

        const double NEPTUNE_YEAR = 164.79132 * EARTH_YEAR;

    public:
        space_age(long seconds);

        double seconds() const;

        double on_mercury() const;

        double on_venus() const;

        double on_earth() const;

        double on_mars() const;

        double on_jupiter() const;

        double on_saturn() const;

        double on_uranus() const;

        double on_neptune() const;
    };
}  // namespace space_age

#endif // SPACE_AGE_H