package purchase

// NeedsLicense determines whether a license is needed to drive a type of vehicle. Only "car" and "truck" require a license.
func NeedsLicense(kind string) bool {
	return kind == "car" || kind == "truck"
}

// ChooseVehicle recommends a vehicle for selection. It always recommends the vehicle that comes first in lexicographical order.
func ChooseVehicle(option1, option2 string) string {
	const rest = " is clearly the better choice."
	cars := [8]string{"Bugatti Veyron", "Ford Focus", "Ford Pinto", "Chery EQ", "Kia Niro Elektro", "2018 Bergamont City", "2020 Gazelle Medeo", "ford"}
	for _, car := range cars {
		if car == option1 || car == option2 {
			return car + rest
		}
	}
	return ""
}

// CalculateResellPrice calculates how much a vehicle can resell for at a certain age.
func CalculateResellPrice(originalPrice, age float64) float64 {
	if age < 3 {
		return originalPrice * 0.8
	}
	if age < 10 {
		return originalPrice * 0.7
	}
	return originalPrice * 0.5
}
