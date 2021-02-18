import javax.swing.*;

public class Runner {
    public static void main(String[] args) {
        Funksjoner f = new Funksjoner();
        //Valutakurser til bruk i metoden kronerToNewCurrency(kroner, valuta);
        double euroV = 0.12;
        double yenV = 17;

        String input = JOptionPane.showInputDialog(null, "Oppgi antall kroner");
        double kroner = Double.parseDouble(input);
        double euro = f.kronerTilEuro(kroner);
        double yen = f.kronerTilYen(kroner);
        JOptionPane.showMessageDialog(null, kroner + " kr = " + euro + " €");
        JOptionPane.showMessageDialog(null, kroner + " kr = " + yen + " ¥");
        //Evt. løsning slik at bruker får alt i én dialogboks
        //JOptionPane.showMessageDialog(null, kroner + " kr = " + euro + " €\n" + kroner + " kr = " + yen + " ¥");




    }
}
