// Package weather provides forecast functions.
package weather

// CurrentCondition represents current condition.
var CurrentCondition string

// CurrentLocation represents current location.
var CurrentLocation string

// Forecast returns forecast for specific location.
func Forecast(city, condition string) string {
	CurrentLocation, CurrentCondition = city, condition
	return CurrentLocation + " - current weather condition: " + CurrentCondition
}
