public class Funksjoner {
    public double kronerTilEuro(double kroner){
        double euro = kroner * 0.12;

        return euro;
    }
    public double kronerTilYen(double kroner){
        double yen = kroner * 17;

        return yen;
    }
    /* En evt. løsning på oppgaven
    public double kronerToNewCurrency(double kroner, double valuta){
        double newCurrency = kroner * valuta;

        return newCurrency;
    }*/
}
