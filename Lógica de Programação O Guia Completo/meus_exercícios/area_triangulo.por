programa {
	funcao inicio() {
		real base, altura, area
		
		escreva("Vamos calcular a altura de um triângulo! \n")
		
		escreva("\nQual a base do triângulo? (em metros) ")
		leia(base)
		escreva("\nQual a altura do triângulo? (em metros) ")
		leia(altura)
		
		area = (base * altura)/2
		escreva("\nA área do triângulo é (em m²): ", area)
		
	}
}
