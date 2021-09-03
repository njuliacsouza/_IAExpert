programa {
	funcao inicio() {
	    real temp_celsius, temp_fahrenheit
	    
		escreva("Diga a temperatura em Celsius: ")
		leia(temp_celsius)
		temp_fahrenheit = (9*temp_celsius + 160)/5
		escreva("\nA temperatura em Fahrenheit é: ", temp_fahrenheit)
	}
}
