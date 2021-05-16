
public class ComparacaoString {
    
    public static void main(String[] args) {
        
        String nome1 = "Daniel";
        String nome2 = new String("Daniel");
        String res = (nome1.equals(nome2))?"igual":"diferente";
        System.out.println(res);
    }
}
