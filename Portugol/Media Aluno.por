programa {
	funcao inicio() {
		real a, b, c, d
		
		escreva("Informe as notas do aluno_A:\n")
		leia(a)
		leia(b)
		escreva("Informe as notas do aluno_B:\n")
		leia(c)
		leia(d)
		
		escreva("Media Aluno A: ",media_aluno(a,b))
		escreva("\n")
		escreva("Media Aluno B: ",media_aluno(c,d))
	}
	
	funcao real media_aluno(real nota1, real nota2){
	    
	   retorne(nota1 + nota2)/2
	    
	}
	
}
