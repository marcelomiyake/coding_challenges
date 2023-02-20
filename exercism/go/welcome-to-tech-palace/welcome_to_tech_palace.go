package techpalace

import (
	"bytes"
	"strings"
)

// WelcomeMessage returns a welcome message for the customer.
func WelcomeMessage(customer string) string {
	var builder bytes.Buffer
	builder.WriteString("Welcome to the Tech Palace, ")
	builder.WriteString(strings.ToUpper(customer))
	return builder.String()
}

// AddBorder adds a border to a welcome message.
func AddBorder(welcomeMsg string, numStarsPerLine int) string {
	var builder bytes.Buffer
	builder.WriteString(strings.Repeat("*", numStarsPerLine))
	builder.WriteString("\n")
	builder.WriteString(welcomeMsg)
	builder.WriteString("\n")
	builder.WriteString(strings.Repeat("*", numStarsPerLine))
	return builder.String()
}

// CleanupMessage cleans up an old marketing message.
func CleanupMessage(oldMsg string) string {
	var newMsg = strings.Replace(oldMsg, "*", "", -1)
	newMsg = strings.Replace(newMsg, "\n", "", -1)
	newMsg = strings.Trim(newMsg, " ")
	return newMsg
}
