import javax.swing.*;

public class Runner {
    public static void main(String[] args) {
        Funksjoner f = new Funksjoner();


        Object[] valutaValg = new String[] { "kr → €", "kr → ¥", "Avbryt"};

        JPanel panel = new JPanel();
        panel.add(new JLabel("Oppgi antall kroner"));
        JTextField textField = new JTextField(8);
        panel.add(textField);

        int result = JOptionPane.showOptionDialog(null, panel, "Oppgi antall kroner",
                JOptionPane.YES_NO_CANCEL_OPTION, JOptionPane.PLAIN_MESSAGE, null,
                valutaValg, valutaValg[2]);

        String input;
        double kroner;
        if (result == JOptionPane.YES_OPTION){
            input = textField.getText();
            kroner = Double.parseDouble(input);
            double euro = f.kronerTilEuro(kroner);
            JOptionPane.showMessageDialog(null, kroner + " kr = " + euro + " €");

        }
        else if (result == JOptionPane.NO_OPTION){
            input = textField.getText();
            kroner = Double.parseDouble(input);
            double yen = f.kronerTilYen(kroner);
            JOptionPane.showMessageDialog(null, kroner + " kr = " + yen + " ¥");
        }

        /*//Valutakurser til bruk i metoden kronerToNewCurrency(kroner, valuta);
        double euroV = 0.12;
        double yenV = 17;
        //Evt. løsning slik at bruker får alt i én dialogboks
        //JOptionPane.showMessageDialog(null, kroner + " kr = " + euro + " €\n" + kroner + " kr = " + yen + " ¥");
        */
    }
}
