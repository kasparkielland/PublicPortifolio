import java.awt.*;
import java.util.ArrayList;
import java.util.List;

class Snake extends BaseGraphic {
    private final List<Point> snakePoints;
    private int xDir;
    private int yDir;
    boolean isMoving;
    private boolean elongate;
    private final BaseGraphic bs = new BaseGraphic();


    public Snake(){
        snakePoints = new ArrayList<>();
        xDir = 0;
        yDir = 0;
        isMoving = false;
        elongate = false;
        int STARTY = 150;
        int STARTX = 150;
        snakePoints.add(new Point(STARTX, STARTY));

        int STARTSIZE = 10;
        for (int i = 1; i < STARTSIZE; i++){
            snakePoints.add(new Point(STARTX - i * 4, STARTY));
        }
    }

    public void draw(Graphics g){
        bs.farge = Color.WHITE;
        bs.bredde = 4;
        bs.hoyde = 4;

        for (Point p : snakePoints){
            bs.x = p.getX();
            bs.y = p.getY();
            bs.tegnMeg(g);
        }
    }

    public void move(){
        if (isMoving) {
            Point temp = snakePoints.get(0);
            Point last = snakePoints.get(snakePoints.size() - 1);
            Point newStart = new Point(temp.getX() + xDir * 4, temp.getY() + yDir * 4);
            for (int i = snakePoints.size() - 1; i >= 1; i--) {
                snakePoints.set(i, snakePoints.get(i - 1));
            }
            snakePoints.set(0, newStart);
            if (elongate){
                snakePoints.add(last);
                elongate = false;
            }
        }
    }

    public boolean snakeCollision(){
        int x = this.getX();
        int y = this.getY();
        for (int i = 1; i < snakePoints.size(); i++){
            if (snakePoints.get(i).getX() == x && snakePoints.get(i).getY() == y)
                return true;
        }
        return false;
    }

    public void setIsMoving(boolean b){
        isMoving = b;
    }

    public int getxDir(){
        return xDir;
    }

    public int getyDir(){
        return yDir;
    }

    public void setXDir(int x){
        xDir = x;
    }

    public void setYDir(int y){
        yDir = y;
    }

    public int getX(){
        return snakePoints.get(0).getX();
    }

    public int getY(){
        return snakePoints.get(0).getY();
    }

    public void setElongate( boolean b){
        elongate = b;
    }


}