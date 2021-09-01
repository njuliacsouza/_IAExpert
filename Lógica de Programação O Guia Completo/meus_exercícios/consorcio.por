programa {
	funcao inicio() {
		real n_prestacoes, prestacoes_pagas, valor_prestacao, total_pago, saldo_devedor
		
		escreva("Vamos ver como está sua dívida no consórcio! \n")
		
		escreva("\nQuantas prestações são no total? ")
		leia(n_prestacoes)
		escreva("\nQuantas prestações já foram pagas? ")
		leia(prestacoes_pagas)
		escreva("\nQual o valor de cada prestação? R$")
		leia(valor_prestacao)
		
		total_pago = prestacoes_pagas * valor_prestacao
		saldo_devedor = (n_prestacoes * valor_prestacao) - total_pago
		
		escreva("\nVocê já pagou R$", total_pago)
		escreva("\nSeu saldo devedor é R$", saldo_devedor)
	}
}
