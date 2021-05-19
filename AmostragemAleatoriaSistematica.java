
/**
 * Um lojista adquiriu 1000 lâmpadas, mas não tem tempo para testar todas. Suponha que ele queira testar 2% delas por 
 * amostragem aleatória sistemática e queira iniciar pela 26ª lâmpada. Dessa maneira, qual será a última lâmpada a ser testada?
 */

public class AmostragemAleatoriaSistematica {
    
    public static void main(String[] args) {    
        int totlampadas =1000;
        int amostra =(totlampadas/100*2);
        int salto =(totlampadas/amostra);    
        for(int l=26; l<=totlampadas; l+=salto) {
            System.out.println(l);   
        }            
    }
}
