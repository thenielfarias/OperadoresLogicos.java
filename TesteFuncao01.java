
public class TesteFuncao01 {
    
    /*static void soma(int a, int b) {
        int s = a + b;
        System.out.println("A soma e " + s);
    }
        
    public static void main(String[] args) {
        System.out.println("Initialize");
        soma(5,2);
    }*/

    static int soma(int a, int b) {
        int s = a + b;
        return s;
    }
        
    public static void main(String[] args) {
        System.out.println("Initialize");
        int sm = soma(5,2);
        System.out.println("A soma vale " + sm);
    }        




}
