import java.awt.*;

class BaseGraphic {
    //Farge
    public Color farge;
    //Størrelse
    public int bredde;
    public int hoyde;

    //Posisjon
    public int x;
    public int y;

    public void tegnMeg(Graphics g) {
        g.setColor(this.farge);
        g.fillRect(this.x, this.y, this.bredde, this.hoyde);
    }


}
