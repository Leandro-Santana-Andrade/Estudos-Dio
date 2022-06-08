programa {
	funcao inicio() {
	    
	    inteiro x, y
		escreva("Digite 2 numeros para somatorio do intervalo\n")
		leia(x)
		leia(y)
		
		escreva("Resutado do intervalo: ", somatorio_intervalo(x,y))
		
	}
	
	funcao inteiro somatorio_intervalo(inteiro x, inteiro y){
	    
    	inteiro total, resultado_parcial
    	total = y/2
    	resultado_parcial = x+y
    	
        inteiro resultado = total * resultado_parcial
    
        retorne resultado
	    
	}
    
}
