import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import twitter4j.*;
import twitter4j.conf.ConfigurationBuilder;


public class GUI extends JFrame implements ActionListener{
    private String emneknagg = "#dat113";
    private JTextArea tekst = new JTextArea();
    private JTextField teksstfelt = new JTextField();

    GUI() {
        final int height = 800;
        final int width = 1000;

        this.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        this.setTitle("T W I T T E R");
        this.setSize(width, height);
        this.setLocationRelativeTo(null);
        this.setVisible(true);


        this.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        this.setLayout(new BoxLayout(this.getContentPane(), BoxLayout.Y_AXIS));

        JLabel tweets = new JLabel("Eksisterende tweets");
        JLabel sporsmaal = new JLabel("Skriv ditt spørsmål");

        JButton sendSporsmaal = new JButton("Send inn spørsmål");
        sendSporsmaal.addActionListener(this);

        JButton byttEmneknagg = new JButton("Bytt #emneknagg");
        byttEmneknagg.addActionListener(this);


        teksstfelt.setMaximumSize((new Dimension(Integer.MAX_VALUE, teksstfelt.getPreferredSize().height)));

        getTweets();

        this.add(tweets);
        tekst.setEditable(false);
        this.add(tekst);
        this.add(sporsmaal);
        this.add(teksstfelt);

        this.add(sendSporsmaal);
        this.add(byttEmneknagg);
        this.setVisible(true);

    }

    private void getTweets(){
        tekst.setText("");

        ConfigurationBuilder cb = new ConfigurationBuilder();
        cb.setOAuthConsumerKey("saJmmLLlOlZFXP7Kz1kvKPtAo");
        cb.setOAuthConsumerSecret("8g7LpU6Gz5DP9IeOt0WGKRcL9IuMdhooKD9W2Hy2zMvNboiuxp");
        cb.setOAuthAccessToken("963340503990374401-SrbciHsmEobIH2tqDIkA4Cap5bneelo");
        cb.setOAuthAccessTokenSecret("nVOjU0OlmzKkbtGyetOdooQuiVSIy0Lrk97kfo3Q7Yazp");
        TwitterFactory tf = new TwitterFactory(cb.build());
        Twitter twitter = tf.getInstance();

        Query q = new Query(emneknagg);
        GeoLocation geo = new GeoLocation(58.3405000,8.5934300);
        q.setGeoCode(geo,100.0, Query.KILOMETERS);
        try {
            QueryResult result = twitter.search(q);
            for(Status tweet:result.getTweets()){
                tekst.setText(tekst.getText() + tweet.getUser().getName() + ":\n" + tweet.getText() + "\n\n");
            }
        } catch (TwitterException e) {
            e.printStackTrace();
        }

    }

    public void actionPerformed(ActionEvent e) {
        if (e.getActionCommand().equals("Send inn spørsmål")) {
            ConfigurationBuilder cb = new ConfigurationBuilder();
            cb.setOAuthConsumerKey("saJmmLLlOlZFXP7Kz1kvKPtAo");
            cb.setOAuthConsumerSecret("8g7LpU6Gz5DP9IeOt0WGKRcL9IuMdhooKD9W2Hy2zMvNboiuxp");
            cb.setOAuthAccessToken("963340503990374401-SrbciHsmEobIH2tqDIkA4Cap5bneelo");
            cb.setOAuthAccessTokenSecret("nVOjU0OlmzKkbtGyetOdooQuiVSIy0Lrk97kfo3Q7Yazp");
            TwitterFactory tf = new TwitterFactory(cb.build());
            Twitter twitter = tf.getInstance();

            String tweet = teksstfelt.getText();
            try {
                twitter.updateStatus(tweet);
            } catch (TwitterException e1) {
                e1.printStackTrace();
            }
            teksstfelt.setText("");
        }
        else if (e.getActionCommand().equals("Bytt #emneknagg")){
            emneknagg = ('#' + JOptionPane.showInputDialog("Fyll inn ny emneknagg, ikke sett '#' foran emnet!"));
            getTweets();
        }
    }
}