/*
 * Created by Kaspar Eikum Kielland on 7/4/2018 for University of Agder
 */

import javax.swing.*;
import java.awt.*;

class GUI extends JFrame {
    JMenuItem open = new JMenuItem("Åpne");
    JMenuItem saveAs = new JMenuItem("Lagre som...");
    JMenuItem save = new JMenuItem("Lagre");
    JMenuItem checkSpelling = new JMenuItem("Stavekontroll");
    JMenuItem turnOffSpelling = new JMenuItem("Skru av stavekontroll");
    JMenuItem addWord = new JMenuItem("Legg til ord");
    JMenuItem showWordlist = new JMenuItem("Vis ordliste");

    JTextPane textPane = new JTextPane();

    GUI(controller c) {
        JFrame frame = new JFrame();
        frame.setLayout(new BorderLayout());
        String title = "T E X T    E D I T O R";
        frame.setTitle(title);
        frame.setSize(600, 600);
        frame.setLocationRelativeTo(null);
        frame.setDefaultCloseOperation(DO_NOTHING_ON_CLOSE);

        JMenuBar menuBar = new JMenuBar();
        JScrollPane scrollPane = new JScrollPane(
                textPane,
                JScrollPane.VERTICAL_SCROLLBAR_AS_NEEDED,
                JScrollPane.HORIZONTAL_SCROLLBAR_AS_NEEDED);
        frame.getContentPane().add(scrollPane);
        JMenu file = new JMenu("Fil");
        JMenu spelling = new JMenu("Stavekontroll");

        menuBar.add(file);
        menuBar.add(spelling);

        checkSpelling.addActionListener(c);
        turnOffSpelling.addActionListener(c);
        addWord.addActionListener(c);
        showWordlist.addActionListener(c);
        open.addActionListener(c);
        saveAs.addActionListener(c);
        save.addActionListener(c);
        textPane.addKeyListener(c);
        frame.addWindowListener(c);

        file.add(open);
        file.add(saveAs);
        file.add(save);
        spelling.add(checkSpelling);
        spelling.add(turnOffSpelling);
        spelling.add(addWord);
        spelling.add(showWordlist);

        textPane.setEditable(true);
        frame.setJMenuBar(menuBar);
        frame.add(scrollPane);
        frame.setVisible(true);
    }
    public int handleClosing(String message, String title){
        return JOptionPane.showOptionDialog(null,
                message,
                title,
                JOptionPane.YES_NO_CANCEL_OPTION,
                JOptionPane.QUESTION_MESSAGE,
                null,
                null,
                null);
    }

    public String inputMessage(String message, String title){
        return JOptionPane.showInputDialog(
                null,
                message,
                title,
                JOptionPane.INFORMATION_MESSAGE);
    }
}


