import java.util.Scanner;

public class CalculadoraImposto {
    
    public static void main(String[] args) {
        Scanner teclado = new Scanner(System.in);
        System.out.print("Digite o preço na America: ");
        float america = teclado.nextFloat();
        System.out.print("O preço na America com imposto e: " + (america+(america/100*10)) + "\n");
        System.out.print("Digite o preço na Europa: ");
        float europa = teclado.nextFloat();
        System.out.print("O preço na Europa com imposto e: " + (europa+(europa/100*15)) + "\n");
        System.out.print("Digite o preço na Asia: ");
        float asia = teclado.nextFloat();
        System.out.print("O preço na Asia com imposto e: " + (asia+(asia/100*20)) + "\n");
        System.out.print("A soma de todos os preços e: " + (america+europa+asia));

    }
}
