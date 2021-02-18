import javax.swing.*;

public class Funksjoner {
    public String fraValuta(){
        String[] nedtrekksValg = {"kr", "€", "¥"};
        String fraValuta = (String) JOptionPane.showInputDialog(
                null,
                "Velg valutaen du vil konvertere fra",
                "Velg valuta",
                JOptionPane.QUESTION_MESSAGE,
                null,
                nedtrekksValg,
                nedtrekksValg[0]);
        return fraValuta;
    }
    public String tilValuta(){
        String[] nedtrekksValg = {"kr", "€", "¥"};
        String tilValuta = (String) JOptionPane.showInputDialog(
                null,
                "Velg valutaen du vil konvertere til",
                "Velg valuta",
                JOptionPane.QUESTION_MESSAGE,
                null,
                nedtrekksValg,
                nedtrekksValg[0]);
        return tilValuta;
    }

    public double valutaUtregning(double valuta1, double valuta2) {
        double utregning = valuta1 * valuta2;
        return utregning;
    }

    public double choises(String fraValuta, String tilValuta, double mengde, double valuta[][]){
        double nyMengde = 0;

        if (fraValuta.equals("kr")){
            switch (tilValuta){
                case "kr":
                    nyMengde = valutaUtregning(mengde, valuta[0][0]);
                    break;
                case "€":
                    nyMengde = valutaUtregning(mengde, valuta[0][1]);
                    break;
                case "¥":
                    nyMengde = valutaUtregning(mengde, valuta[0][2]);
                    break;
            }
        }
        else if (fraValuta.equals("€")){
            switch (tilValuta){
                case "kr":
                    nyMengde = valutaUtregning(mengde, valuta[1][0]);
                    break;
                case "€":
                    nyMengde = valutaUtregning(mengde, valuta[1][1]);
                    break;
                case "¥":
                    nyMengde = valutaUtregning(mengde, valuta[1][2]);
                    break;
            }
        }
        else if (fraValuta.equals("¥")){
            switch (tilValuta){
                case "kr":
                    nyMengde = valutaUtregning(mengde, valuta[2][0]);
                    break;
                case "€":
                    nyMengde = valutaUtregning(mengde, valuta[2][1]);
                    break;
                case "¥":
                    nyMengde = valutaUtregning(mengde, valuta[2][2]);
                    break;
            }
        }
        else
            JOptionPane.showMessageDialog(null, "En feil har oppstått!");

        return nyMengde;
    }
    public void egenValuta(String fraValuta, String tilValuta, double valuta[][]) {

        int fraValutaInt = 0;
        if (fraValuta.equals("kr"))
            fraValutaInt = 0;
        else if (fraValuta.equals("€"))
            fraValutaInt = 1;
        else if (fraValuta.equals("¥"))
            fraValutaInt = 2;

        int tilValutaInt = 0;
        if (tilValuta.equals("kr"))
            tilValutaInt = 0;
        else if (tilValuta.equals("€"))
            tilValutaInt = 1;
        else if (tilValuta.equals("¥"))
            tilValutaInt = 2;

        int result = JOptionPane.showOptionDialog(null,
                "Vil du bruke egen valutakurs?",
                "Vil du bruke egen valutakurs?",
                JOptionPane.YES_NO_OPTION,
                JOptionPane.PLAIN_MESSAGE,
                null,
                null,
                null);
        if (result == JOptionPane.YES_OPTION) {
            String input = JOptionPane.showInputDialog("Skriv inn valutakursen fra 1 " + fraValuta + " til " + tilValuta);
            valuta[fraValutaInt][tilValutaInt] = Double.parseDouble(input);
        }
    }
}
