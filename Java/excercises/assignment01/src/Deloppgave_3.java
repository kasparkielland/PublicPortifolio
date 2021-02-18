import javax.swing.*;

public class Deloppgave_3 {
    /**
     * @param args
     */
    public static void main(String[] args){
        // TODO Auto-generated method stub
        int magic_number = (int)(Math.random()*100);
        String input;
        int guessed_number;
        while (true){
            input = JOptionPane.showInputDialog(null, "Gjett tallet mellom 0 og 100");
            guessed_number = Integer.parseInt(input);

            if (magic_number == guessed_number){
                JOptionPane.showMessageDialog(null, "DU GJETTET RIKTIG!!");
                break;
            }
            else
                JOptionPane.showMessageDialog(null, "Dessverre ikke riktig denne gangen, prøv igjen!");

        }

    }
}
