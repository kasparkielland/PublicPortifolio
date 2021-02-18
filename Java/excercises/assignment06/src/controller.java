/*
 * Created by Kaspar Eikum Kielland on 7/4/2018 for University of Agder
 */

import javax.swing.*;
import java.awt.*;
import java.awt.event.*;


public class controller implements ActionListener, WindowListener, KeyListener {
    private GUI myView;
    private dataHandler myModel;
    private Boolean change = true;
    private Boolean multipleWindows = false;


    private controller() {
        this.myView = new GUI(this);
        myView.setName("frame0");
        this.myModel = new dataHandler();
    }

    public static void main(String[] args) {
        new controller();
    }

    public void actionPerformed(ActionEvent e) {
        if (e.getSource().equals(myView.saveAs)) {
            myModel.saveFileAs(myView, myView.textPane);
        } else if (e.getSource().equals(myView.save)) {
            if (myModel.filename.equals(""))
                myModel.saveFileAs(myView, myView.textPane);

            else
                myModel.saveFile(myView.textPane);
        } else if (e.getSource().equals(myView.open)) {
            myModel.openFile(myView.textPane);
        }
        if (e.getSource().equals(myView.checkSpelling)) {
            myModel.checkSpelling(myView.textPane);
        } else if (e.getSource().equals(myView.turnOffSpelling)) {
            myModel.turnOffSpelling(myView.textPane);
        } else if (e.getSource().equals(myView.addWord)) {
            String newWord = myView.inputMessage(
                    "Skriv inn ordet du vil legge til i ordlisten",
                    "Legg til ord i ordlisten");
            myModel.addWordToWordlist(newWord);
        } else if (e.getSource().equals(myView.showWordlist)) {
            GUI newMyView = new GUI(this);
            newMyView.setName("frame1");
            myModel.printWordlist(newMyView.textPane);
            multipleWindows = true;
        }
    }

    public void keyPressed(KeyEvent e) {
        change = false;
    }


    public void windowClosing(WindowEvent e) {
        Window currentWindow = e.getWindow();

        if (change)
            currentWindow.dispose();
        else {
            int result = myView.handleClosing(
                    "Du har ikke lagret endringene!\nLagre nå?",
                    "Endringer vil gå tapt");
            switch (result) {
                case JOptionPane.YES_OPTION:
                    myModel.saveFile(myView.textPane);
                    currentWindow.dispose();
                    if (!multipleWindows)
                        System.exit(0);
                    multipleWindows = false;
                case JOptionPane.NO_OPTION:
                    currentWindow.dispose();
                    if (!multipleWindows)
                        System.exit(0);
                    multipleWindows = false;
                case JOptionPane.CANCEL_OPTION:
                    break;
            }
        }
    }


    //Unused listeners
    public void windowOpened(WindowEvent e) {

    }

    public void windowClosed(WindowEvent e) {

    }

    public void windowIconified(WindowEvent e) {

    }

    public void windowDeiconified(WindowEvent e) {

    }

    public void windowActivated(WindowEvent e) {

    }

    public void windowDeactivated(WindowEvent e) {

    }

    public void keyTyped(KeyEvent e) {
    }

    public void keyReleased(KeyEvent e) {

    }
}
