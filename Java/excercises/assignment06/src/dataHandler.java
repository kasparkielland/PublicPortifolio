/*
 * Created by Kaspar Eikum Kielland on 7/4/2018 for University of Agder
 */

import javax.swing.*;
import javax.swing.text.AttributeSet;
import javax.swing.text.SimpleAttributeSet;
import javax.swing.text.StyleConstants;
import javax.swing.text.StyleContext;
import java.awt.*;
import java.io.*;
import java.util.ArrayList;
import java.util.Scanner;

public class dataHandler{
    private JFileChooser fc = new JFileChooser();
    private ArrayList<String> wordListArr = new ArrayList<>();
    public String filename = "";
    private String filepath = "";
    private File file = null;

    dataHandler() {
        importWordlist();
    }

    private void importWordlist(){
        file = new File("/Users/kaspar/OneDrive - Universitetet i Agder/Semester 2/DAT-113/kaspak16/DAT113/assignments/assignment06/src/wordlist/ordliste.txt");
        Scanner s = null;
        try {
            s = new Scanner(file);
        } catch (FileNotFoundException e) {
            e.printStackTrace();
        }
        while (s != null && s.hasNext()) {
            wordListArr.add(s.next());
        }
        if (s != null) {
            s.close();
        }

    }

    public void printWordlist(JTextPane tp){
        importWordlist();
        StringBuilder wordlist = new StringBuilder();
        /*for (String word : wordListArr){
            wordlist.append(word).append("\n");
        }*/
        for (int i = wordListArr.size()-5; i < wordListArr.size(); i++){
            wordlist.append(wordListArr.get(i));
            wordlist.append("\n");
        }
        tp.setText(wordlist.toString());
    }

    public void checkSpelling(JTextPane tp) {
        importWordlist();
        String[] words = tp.getText().split("[ !.,]");
        tp.setText("");
        for (String word : words) {
            int j;
            if (dataHandler.isInteger(word)) {
                appendToPane(tp, word + " ", Color.GREEN);
            }
            else {
                for (j = 0; j < wordListArr.size(); j++) {
                    if (word.equals(wordListArr.get(j))) {
                        appendToPane(tp, word + " ", Color.GREEN);
                        break;
                    }
                }
                if (j == wordListArr.size()) {
                    appendToPane(tp, word + " ", Color.RED);
                }
            }
        }
        appendToPane(tp, "", Color.BLACK);
    }

    public void turnOffSpelling(JTextPane tp) {
        String[] words = tp.getText().split("[ !.,]");
        tp.setText("");
        for (String word : words) {
            appendToPane(tp, word + " ", Color.BLACK);
        }
    }

    public void addWordToWordlist(String newWord) {
        importWordlist();
        wordListArr.add(newWord);
        try(FileWriter fw = new FileWriter("/Users/kaspar/OneDrive - Universitetet i Agder/Semester 2/DAT-113/kaspak16/DAT113/assignments/assignment06/src/wordlist/ordliste.txt", true);
            BufferedWriter bw = new BufferedWriter(fw);
            PrintWriter out = new PrintWriter(bw)) {
            out.println(newWord);

            //Files.write(Paths.get("/Users/kaspar/kaspak16/DAT113/assignments/assignment06/src/wordlist/ordliste.txt"), newWord.getBytes(), StandardOpenOption.APPEND);
        } catch (IOException e) {
            e.printStackTrace();
            System.out.println("Error when saving word to wordlist.txt");
        }
        importWordlist();

    }

    private void appendToPane(JTextPane tp, String text, Color color) {
        StyleContext sc = StyleContext.getDefaultStyleContext();
        AttributeSet attr = sc.addAttribute(SimpleAttributeSet.EMPTY, StyleConstants.Foreground, color);

        int len = tp.getDocument().getLength();
        tp.setCaretPosition(len);
        tp.setCharacterAttributes(attr, false);
        tp.replaceSelection(text);
    }

    private static boolean isInteger(String s) {
        try {
            Integer.parseInt(s);
        } catch(NumberFormatException e) {
            return false;
        }
        return true;
    }

    public void saveFileAs(Component c, JTextPane tp) {
        fc.setFileSelectionMode(JFileChooser.FILES_ONLY);
        int returnVal = fc.showSaveDialog(c);
        if (returnVal == JFileChooser.APPROVE_OPTION) {
            file = fc.getSelectedFile();
            filename = file.getName();
            filepath = file.getPath();
        } else if (returnVal == JFileChooser.CANCEL_OPTION) {
            System.out.println("Canceled save");
            return;
        }
        saveFile(tp);
    }

    public void saveFile(JTextPane tp){
        try(FileWriter writer = new FileWriter(filepath + ".txt");
            BufferedWriter bwr = new BufferedWriter(writer)){

            bwr.write(tp.getText());
            bwr.close();

            writer.close();
        } catch (IOException e) {
            e.printStackTrace();
            System.out.println("Error");

        }
    }

    public void openFile(JTextPane tp){
        int returnValue = fc.showOpenDialog(null);
        if (returnValue == JFileChooser.APPROVE_OPTION) {
            file = fc.getSelectedFile();
            filename = file.getName();
            filepath = file.getPath();
            try {
                FileReader reader = new FileReader(filepath);
                BufferedReader br = new BufferedReader(reader);
                tp.read(br, null);
                br.close();

            } catch (Exception ex) {
                System.out.println("Error");
            }
        }
        else if (returnValue == JFileChooser.CANCEL_OPTION){
            System.out.println("Canceled open");
        }
    }
}
