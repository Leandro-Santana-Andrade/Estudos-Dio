#include <stdio.h>
#include <stdlib.h>

/*Calculadora com menu para escolha de operação*/

float num1, num2, resultado;

void soma(){

    printf("-------SOMA------\n");
    printf("Digite o primeiro numero: \n");
    scanf("%f", &num1);
    printf("Digite o segundo numero: \n");
    scanf("%f", &num2);

    resultado = num1 + num2;
    printf("Resultado: %.2f\n\n", resultado);
    printf("-----------------fim-----------------\n\n");
    system('pause');
    //system("clear");
    menu();

}

void subtracao(){

    printf("------SUBTRAÇÃO--------\n");
    printf("Digite o primeiro numero: \n");
    scanf("%f", &num1);
    printf("Digite o segundo numero: \n");
    scanf("%f", &num2);

    resultado = num1 - num2;
    printf("Resultado: %.2f\n\n", resultado);
    printf("-----------------fim-----------------\n\n");
    system('pause');
    //system("clear");
    menu(); 

}

void multiplicacao(){

    printf("-----MULTIPLICAÇÃO------.\n");
    printf("Digite o primeiro numero: \n");
    scanf("%f", &num1);
    printf("Digite o segundo numero: \n");
    scanf("%f", &num2);

    resultado = num1 * num2;
    printf("Resultado: %.2f\n\n", resultado);
    printf("-----------------fim-----------------\n\n");
    system('pause');
    //system("clear");
    menu();

}

void divisao(){

    printf("-------DIVISÃO-------.\n");
    printf("Digite o primeiro numero: \n");
    scanf("%f", &num1);
    printf("Digite o segundo numero: \n");
    scanf("%f", &num2);

    resultado = num1 / num2;
    printf("Resultado: %.2f\n\n", resultado);
    printf("-----------------fim-----------------\n\n");
    system('pause');
    //system("clear");
    menu();
}

void sair(){

system("exit");
printf("Fechando aplicativo, aguarde...\n");

}

menu(){

int opcao;

    printf("Escolha o operação:\n");
    printf("1 - Soma\n");
    printf("2 - Subtracao\n");
    printf("3 - Multiplicação\n");
    printf("4 - Divisao\n");
    printf("5 - Sair\n");
    printf("\nInforme o numero: ");
    scanf("%d", &opcao);

switch (opcao)
    {
    case 1: soma();
        break;
    case 2: subtracao();
        break;
    case 3: multiplicacao();
        break;
    case 4: divisao();
        break;
    case 5: sair();
        break;
    default: printf("\nOpção invalida\n\n");
        menu();
        break;
    }

}

int main(){
    
    menu();
    return 0;
}