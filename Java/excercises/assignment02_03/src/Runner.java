import javax.swing.*;

public class Runner {
        public static void main(String[] args) {
            Funksjoner f = new Funksjoner();
            int result = 0;
            while (result == 0) {
                //Valutaer
                double[][] valuta = new double[3][3];
                valuta[0][0] = 1; //kr til kr
                valuta[0][1] = 0.12; //kr til euro
                valuta[0][2] = 17; //kr til yen

                valuta[1][0] = 10.12; //euro til kr
                valuta[1][1] = 1; //euro til euro
                valuta[1][2] = 136.03; //euro til yen

                valuta[2][0] = 0.07; //yen til kr
                valuta[2][1] = 0.0074; //yen til euro
                valuta[2][2] = 1; //yen til yen

                String fraValuta = f.fraValuta();
                String tilValuta = f.tilValuta();

                f.egenValuta(fraValuta, tilValuta, valuta);

                String input = JOptionPane.showInputDialog("Hvor mye vil du konvertere?");
                double mengde = Double.parseDouble(input);
                double nyMengde = f.choises(fraValuta, tilValuta, mengde, valuta);
                result = JOptionPane.showOptionDialog(null,
                        mengde + " " + fraValuta + " = " + nyMengde + " " + tilValuta + "\nVil du ta en ny konvertering?",
                        "Fra " + fraValuta + " til " + tilValuta,
                        JOptionPane.YES_NO_OPTION,
                        JOptionPane.QUESTION_MESSAGE,
                        null,
                        null,
                        null);
            }
        }

    }
