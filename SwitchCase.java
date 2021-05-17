import java.util.Scanner;

public class SwitchCase {
    
    public static void main(String[] args) {
        
        Scanner teclado = new Scanner(System.in);
        System.out.print("Digite a quantidade de pernas: ");
        int pernas = teclado.nextInt();
        String tipo;
        System.out.print("Isso e um(a) ");
        
        switch (pernas) {
            case 1:
                tipo = "Saci";
                break;
            case 2:
                tipo = "Bipede";
                break;
            case 3:
                tipo = "Tripe";
                break;                
            case 4:
                tipo = "Quadrupede";
                break;
            case 6:
                tipo = "Aranha";
                break;
            default:
                tipo = "ET";
            }
            System.out.println(tipo);               

    }
}
