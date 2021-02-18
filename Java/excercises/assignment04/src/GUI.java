import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.awt.event.KeyEvent;
import java.awt.event.KeyListener;
import java.util.TimerTask;
import java.util.Timer;


class GUI extends JFrame implements KeyListener, ActionListener {

    private final int height = 500;
    private final int width = 500;

    private final Graphics gfx;
    private final Snake snake;
    private boolean gameOver;
    private final Token token;


    public GUI() {

        this.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        this.setTitle("S N A K E");
        this.setSize(width, height);
        this.setLocationRelativeTo(null);
        this.addKeyListener(this);
        this.setVisible(true);

        gameOver = false;
        snake = new Snake();
        token = new Token(snake);

        gfx = this.getGraphics();

        view(gfx);
        gameRunner();
    }

    private void backgroundPaint(Graphics g) {
        BaseGraphic bs = new BaseGraphic();
        bs.farge = Color.BLACK;
        bs.bredde = width;
        bs.hoyde = height;
        bs.x = 0;
        bs.y = 0;
        bs.tegnMeg(g);
    }

    private void view(Graphics g) {
        backgroundPaint(g);

        if (!gameOver) {
            snake.draw(g);
            token.draw(g);
        } else {
            backgroundPaint(gfx);
            g.setColor(Color.GREEN);
            g.drawString("Game Over", 20, 50);
            g.drawString("Score: " + token.getScore(), 20, 70);
            g.drawString("Trykk SPACE for å avslutte eller 'R' for å prøve igjenn!", 20, 100);

        }

    }

    private void gameRunner() {
        Timer timer = new Timer();
        TimerTask refresh = new TimerTask() {
            @Override
            public void run() {
                if (!gameOver) {
                    snake.move();
                    checkGameOver();
                    token.snakeCollison();
                    view(gfx);
                }
            }
        };
        Timer tokenTimer = new Timer();
        TimerTask tokenRespawn = new TimerTask() {
            @Override
            public void run() {
                token.changePosition();
            }
        };
        int speed = 40;
        if (token.getScore() >= 5 && token.getScore() < 10) {
            speed = 35;
        } else if ((token.getScore() > 10 && token.getScore() < 15)) {
            speed = 30;
        } else if ((token.getScore() > 15 && token.getScore() < 20)) {
            speed = 20;
        } else if ((token.getScore() > 20 && token.getScore() < 50)) {
            speed = 17;
        } else if ((token.getScore() > 50)) {
            speed = 15;
        }

        timer.scheduleAtFixedRate(refresh, 0, speed);
        tokenTimer.scheduleAtFixedRate(tokenRespawn, 60000, 6000);

    }


    private void checkGameOver() {
        if (snake.getX() < 0 || snake.getX() > width - 10) {
            gameOver = true;
        }
        if (snake.getY() < 0 || snake.getY() > height - 10) {
            gameOver = true;
        }
        if (snake.snakeCollision()) {
            gameOver = true;
        }
    }


    public void keyTyped(KeyEvent e) {

    }

    public void keyPressed(KeyEvent e) {

        if (!snake.isMoving) {
            if (e.getKeyCode() == KeyEvent.VK_UP ||
                    e.getKeyCode() == KeyEvent.VK_DOWN ||
                    e.getKeyCode() == KeyEvent.VK_RIGHT ||
                    e.getKeyCode() == KeyEvent.VK_W ||
                    e.getKeyCode() == KeyEvent.VK_S ||
                    e.getKeyCode() == KeyEvent.VK_D) {
                snake.setIsMoving(true);
            }
        }

        //Up arrow and 'w'
        if (e.getKeyCode() == KeyEvent.VK_UP || e.getKeyCode() == KeyEvent.VK_W) {
            if (snake.getyDir() != 1) {
                System.out.println("Up");
                snake.setYDir(-1);
                snake.setXDir(0);
            }
        }
        //Down arrow and 's'
        if (e.getKeyCode() == KeyEvent.VK_DOWN || e.getKeyCode() == KeyEvent.VK_S) {
            if (snake.getyDir() != -1) {
                System.out.println("Down");
                snake.setYDir(1);
                snake.setXDir(0);
            }

        }
        //Left arrow and 'a'
        if (e.getKeyCode() == KeyEvent.VK_LEFT || e.getKeyCode() == KeyEvent.VK_A) {
            if (snake.getxDir() != 1) {
                System.out.println("Left");
                snake.setYDir(0);
                snake.setXDir(-1);
            }

        }
        //Right arrow and 'd'
        if (e.getKeyCode() == KeyEvent.VK_RIGHT || e.getKeyCode() == KeyEvent.VK_D) {
            if (snake.getxDir() != -1) {
                System.out.println("Right");
                snake.setYDir(0);
                snake.setXDir(1);
            }
        }
        if (e.getKeyCode() == KeyEvent.VK_SPACE && gameOver) {
            System.out.println("Space");
            System.exit(0);
        }
        /*if (e.getKeyCode() == KeyEvent.VK_R && gameOver){
            System.out.println("Restart");
            gameOver = false;
            token.nullScore();
            System.exit(0);
            GUI g = new GUI();
            System.out.println("Kode ferdig");

        }*/


    }

    public void keyReleased(KeyEvent e) {

    }

    public void actionPerformed(ActionEvent e) {

    }
}
