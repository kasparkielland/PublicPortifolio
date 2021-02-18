import javax.swing.*;

public class Deloppgave_1 {
    /**
     * @param args
     */
    public static void main(String[] args){
        // TODO Auto-generated method stub
        String input = JOptionPane.showInputDialog(null, "Skriv et tall");
        int tall = Integer.parseInt(input);
        JOptionPane.showMessageDialog(null,"Du skrev inn tallet " + tall);

    }
}
