import java.util.Scanner;

public class ProgramaIdade {
    
    public static void main(String[] args) {
        Scanner teclado = new Scanner(System.in);
        System.out.print("Digite o ano do seu nascimento: ");
        int nasc = teclado.nextInt();
        int i = 2021-nasc;
        System.out.println("Sua idade e " + i);
        if (i>=18) {
            System.out.print("Maior de idade");
        } else {
            System.out.print("Menor de idade");
        }
        

    
    }
}
