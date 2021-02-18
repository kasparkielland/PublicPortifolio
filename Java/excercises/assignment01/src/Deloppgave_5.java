import javax.swing.*;

public class Deloppgave_5 {
    /**
     * @param args
     */
    public static void main(String[] args){
        // TODO Auto-generated method stub
        int magic_number = (int)(Math.random()*100);
        String input;
        int guessed_number;
        int trials = 0;
        while (true){
            input = JOptionPane.showInputDialog(null, "Gjett tallet mellom 0 og 100");
            guessed_number = Integer.parseInt(input);
            trials++;

            if (magic_number == guessed_number){
                JOptionPane.showMessageDialog(null, "DU GJETTET RIKTIG!!!!" +
                        "\nDu gjettet riktig på forsøk nummer "+ trials);
                break;

            }
            else{
                String hint;
                if (magic_number < guessed_number)
                    hint = "lavere";
                else
                    hint = "høyere";
                JOptionPane.showMessageDialog(null, "Dessverre ikke riktig denne gangen, prøv igjen!" +
                        "\nHINT: Tallet er " + hint + " enn " + guessed_number);

            }

        }

    }
}
