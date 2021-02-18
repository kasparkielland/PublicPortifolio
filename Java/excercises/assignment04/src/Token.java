import java.awt.*;

class Token{
    private int x, y, score;
    private final Snake snake;
    private final BaseGraphic bs = new BaseGraphic();
    private final int height = 500;
    private final int width = 500;


    public Token(Snake s){
        x = (int)(Math.random() * (width - 8));
        y = (int)(Math.random() * (height - 40));
        snake = s;
    }

    public void changePosition(){
        x = (int)(Math.random() * (width - 8));
        y = (int)(Math.random() * (height + 10));

    }

    public int getScore(){
        return score;
    }

    public void draw(Graphics g){
        bs.farge = Color.GREEN;
        bs.bredde = 8;
        bs.hoyde = 8;
        bs.x = x;
        bs.y = y;
        bs.tegnMeg(g);
        g.setColor(Color.WHITE);
        g.drawString("Score: " + getScore(), 20, 50);

    }

    public void snakeCollison(){
        int snakeX = snake.getX() + 2;
        int snakeY = snake.getY() + 2;

        if (snakeX >= x - 1 && snakeX <= x + 9){
            if (snakeY >= y - 1 && snakeY < y + 9){
                changePosition();
                score++;
                snake.setElongate(true);
                System.out.println("Snake spiste eplet");
            }
        }
    }
}
