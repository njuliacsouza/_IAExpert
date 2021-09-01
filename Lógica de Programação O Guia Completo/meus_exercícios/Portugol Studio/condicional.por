programa {
	funcao inicio() {
		real M1, M2, M3, final
		
		escreva("Qual a primeira nota? ")
		leia(M1)
		escreva("Qual a segunda nota? ")
		leia(M2)
		escreva("Qual a terceira nota? ")
		leia(M3)
		
		final = (M1 + M2 + M3)/3
		escreva("\nMédia: ", final)
		
		se (final >= 6)
        {
            escreva("\nParabéns, você foi aprovado!")
        }
        senao
        {
            se (final > 4)
            {
                escreva("\nVocê deve fazer exame!")
            }
            senao
            {
                escreva("\nQue pena, você foi reprovado...")
            }
        }
		
	}
}
