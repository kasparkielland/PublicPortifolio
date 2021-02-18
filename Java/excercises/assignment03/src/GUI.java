import java.awt.GridLayout;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.awt.event.KeyListener;
import java.util.Random;

import javax.swing.*;

public class GUI extends JFrame implements ActionListener, KeyListener {

    JMenuBar menuBar = new JMenuBar();
    JMenu file = new JMenu("File");
    JMenu newGame = new JMenu("New game");
    JMenuItem easy = new JMenuItem("Easy");
    JMenuItem medium = new JMenuItem("Medium");
    JMenuItem hard = new JMenuItem("Hard");
    JMenuItem checkGame = new JMenuItem("Check game");
    JMenuItem deleteGame = new JMenuItem("Delete game");

    public JTextField[][] sudukoBrett = new JTextField[9][9];

    public GUI() {
        this.setLayout(new GridLayout(9,9));
        this.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        this.setJMenuBar(menuBar);
        menuBar.add(file);
        file.add(newGame);
        newGame.add(easy);
        newGame.add(medium);
        newGame.add(hard);
        file.add(checkGame);
        file.add(deleteGame);

        checkGame.addActionListener(this);
        deleteGame.addActionListener(this);
        easy.addActionListener(this);
        medium.addActionListener(this);
        hard.addActionListener(this);

        for(int i = 0; i < 9; i++) {
            for(int j = 0; j < 9; j++) {
                sudukoBrett[i][j] = new JTextField();
                sudukoBrett[i][j].addKeyListener(this);
                this.add(sudukoBrett[i][j]);
            }
        }

        this.setTitle("S U D U K O");
        this.setSize(600,600);
        this.setLocationRelativeTo(null);
        this.setVisible(true);
    }

    public void nyttBrett() {
        for(int i = 0; i < 9; i++) {
            for(int j = 0; j < 9; j++) {
                sudukoBrett[i][j].setEditable(true);
                sudukoBrett[i][j].setText("");
            }
        }
    }

    public void genRandom(int vansklighetsgrad) {
        Random rg = new Random();
        int checker;
        for (int i = 0; i < 9; i++) {
            for (int j = 0; j < 9; j++) {
                checker = rg.nextInt(vansklighetsgrad);
                if (checker == 1 && sudukoBrett[i][j].isEditable()) {
                    int rgTall = rg.nextInt(9) + 1;
                    String tall = String.valueOf(rgTall);
                    sudukoBrett[i][j].setText(tall);
                    checkAndValidateRowCol();
                    sudukoBrett[i][j].setEditable(false);
                }
            }
        }
    }

    public boolean checkGame() {
        int checker = 0;
        for (int n = 0; n < 9; n++) {
            for (int j = 0; j < 9; j++) {
                for (int i = j + 1; i < 9; i++) {
                    //Hvis tallet i posisjonen er unikt for hele raden OG hele kolonnen --> øk "checker" med 1
                    if (!(sudukoBrett[n][j].getText().equals(sudukoBrett[n][i].getText())) &&
                        !(sudukoBrett[j][n].getText().equals(sudukoBrett[i][n].getText()))
                            /*!sudukoBrett[n][j].isEditable() && !sudukoBrett[j][n].isEditable()*/) {
                        checker++;
                    }
                }
            }
        }
       return (checker == 41 || checker == 31 || checker == 21);
    }

    public void checkAndValidateRowCol(){
        Random rg = new Random();
        for (int n = 0; n < 9; n++) {
            for (int j = 0; j < 9; j++) {
                for (int i = j+1; i < 9; i++){
                    while (!(sudukoBrett[n][j].getText().equals("")) && sudukoBrett[n][j].getText().equals(sudukoBrett[n][i].getText())) {
                        int rgTall = rg.nextInt(9) + 1;
                        String tall = String.valueOf(rgTall);
                        sudukoBrett[n][j].setText(tall);
                    }
                    while (!(sudukoBrett[j][n].getText().equals("")) && sudukoBrett[j][n].getText().equals(sudukoBrett[i][n].getText())) {
                        int rgTall = rg.nextInt(9) + 1;
                        String tall = String.valueOf(rgTall);
                        sudukoBrett[j][n].setText(tall);
                    }
                }
            }
        }
    }

    @Override
    public void actionPerformed(ActionEvent e) {

        if(e.getSource().equals(easy)) {
            nyttBrett();
            genRandom(2);
        }
        else if(e.getSource().equals(medium)) {
            nyttBrett();
            genRandom(3);
        }
        else if(e.getSource().equals(hard)) {
            nyttBrett();
            genRandom(4);
        }
        else if(e.getSource().equals(deleteGame)) {
            nyttBrett();
        }
        else if(e.getSource().equals(checkGame)){
            if (checkGame()){//checkGame() == 41 || checkGame() == 20){
                JOptionPane.showMessageDialog(null, "Brettet er godjeknt!");
            }
            else
                JOptionPane.showMessageDialog(null, "Brettet er ugyldig!");
        }
    }

    @Override
    public void keyTyped(java.awt.event.KeyEvent e) {
        if (!(e.getKeyChar() >= 49 && e.getKeyChar() <= 57 || e.getKeyChar() == 8))
            e.consume();
    }

    @Override
    public void keyPressed(java.awt.event.KeyEvent e) {
    }

    @Override
    public void keyReleased(java.awt.event.KeyEvent e) {

    }
}