# -----Statement of Authorship----------------------------------------#
#
#  This is an individual assessment item.  By submitting this
#  code I agree that it represents my own work.  I am aware of
#  the University rule that a student must not act in a manner
#  which constitutes academic dishonesty as stated and explained
#  in QUT's Manual of Policies and Procedures, Section C/5.3
#  "Academic Integrity" and Section E/2.1 "Student Code of Conduct".
#
#    Student no: n10588281
#    Student name: Kaspar Kielland
#
#  NB: Files submitted without a completed copy of this statement
#  will not be marked.  Submitted files will be subjected to
#  software plagiarism analysis using the MoSS system
#  (http://theory.stanford.edu/~aiken/moss/).
#
# --------------------------------------------------------------------#


# -----Assignment Description-----------------------------------------#
#
#  News Feed Aggregator
#
#  In this assignment you will combine your knowledge of HTMl/XML
#  mark-up languages with your skills in Python scripting, pattern
#  matching, and Graphical User Interface design to produce a useful
#  application that allows the user to aggregate RSS news feeds.
#  See the instruction sheet accompanying this file for full details.
#
# --------------------------------------------------------------------#


# -----Imported Functions---------------------------------------------#
#
# Below are various import statements for helpful functions.  You
# should be able to complete this assignment using these
# functions only.  Note that not all of these functions are
# needed to successfully complete this assignment.
#
# NB: You may NOT use any Python modules that need to be downloaded
# and installed separately, such as "Beautiful Soup" or "Pillow".
# Only modules that are part of a standard Python 3 installation may
# be used. 

# The function for opening a web document given its URL.
# (You WILL need to use this function in your solution,
# either directly or via our "download" function.)

# Functions for finding all occurrences of a pattern
# defined via a regular expression, as well as
# the "multiline" and "dotall" flags.  (You do NOT need to
# use these functions in your solution, because the problem
# can be solved with the string "find" function, but it will
# be difficult to produce a concise and robust solution
# without using regular expressions.)
from re import findall
# Import the standard SQLite functions (just in case they're
# needed one day).
from sqlite3 import *
# Import the standard Tkinter functions. (You WILL need to use
# these functions in your solution.  You may import other widgets
# from the Tkinter module provided they are ones that come bundled
# with a standard Python 3 implementation and don't have to
# be downloaded and installed separately.)
from time import time
from tkinter import *

# Import a special Tkinter widget we used in our demo
# solution.  (You do NOT need to use this particular widget
# in your solution.  You may import other such widgets from the
# Tkinter module provided they are ones that come bundled
# with a standard Python 3 implementation and don't have to
# be downloaded and installed separately.)
from tkinter.ttk import Progressbar


#
# --------------------------------------------------------------------#


# -----------------------------------------------------------
#
# A function to download and save a web document. If the
# attempted download fails, an error message is written to
# the shell window and the special value None is returned.
#
# Parameters:
# * url - The address of the web page you want to download.
# * target_filename - Name of the file to be saved (if any).
# * filename_extension - Extension for the target file, usually
#      "html" for an HTML document or "xhtml" for an XML
#      document or RSS Feed.
# * save_file - A file is saved only if this is True. WARNING:
#      The function will silently overwrite the target file
#      if it already exists!
# * char_set - The character set used by the web page, which is
#      usually Unicode UTF-8, although some web pages use other
#      character sets.
# * lying - If True the Python function will hide its identity
#      from the web server. This can be used to prevent the
#      server from blocking access to Python programs. However
#      we do NOT encourage using this option as it is both
#      unreliable and unethical!
# * got_the_message - Set this to True once you've absorbed the
#      message about Internet ethics.
#


def download(url='http://www.wikipedia.org/',
             target_filename='download',
             filename_extension='xhtml',
             save_file=True,
             char_set='UTF-8',
             lying=False,
             got_the_message=False):
    # Import the function for opening online documents and
    # the class for creating requests
    from urllib.request import urlopen, Request

    # Import an exception raised when a web server denies access
    # to a document
    from urllib.error import HTTPError

    # Open the web document for reading
    try:
        if lying:
            # Pretend to be something other than a Python
            # script (NOT RECOMMENDED!)
            request = Request(url)
            request.add_header('User-Agent', 'Mozilla/5.0')
            if not got_the_message:
                print("Warning - Request does not reveal client's true identity.")
                print("          This is both unreliable and unethical!")
                print("          Proceed at your own risk!\n")
        else:
            # Behave ethically
            request = url
        web_page = urlopen(request)
    except ValueError:
        print("Download error - Cannot find document at URL '" + url + "'\n")
        return None
    except HTTPError:
        print("Download error - Access denied to document at URL '" + url + "'\n")
        return None
    except Exception as message:
        print("Download error - Something went wrong when trying to download " + \
              "the document at URL '" + url + "'")
        print("Error message was:", message, "\n")
        return None

    # Read the contents as a character string
    try:
        web_page_contents = web_page.read().decode(char_set)
    except UnicodeDecodeError:
        print("Download error - Unable to decode document from URL '" + \
              url + "' as '" + char_set + "' characters\n")
        return None
    except Exception as message:
        print("Download error - Something went wrong when trying to decode " + \
              "the document from URL '" + url + "'")
        print("Error message was:", message, "\n")
        return None

    # Optionally write the contents to a local text file
    # (overwriting the file if it already exists!)
    if save_file:
        try:
            text_file = open(target_filename + '.' + filename_extension,
                             'w', encoding=char_set)
            text_file.write(web_page_contents)
            text_file.close()
        except Exception as message:
            print("Download error - Unable to write to file '" + \
                  target_filename + "'")
            print("Error message was:", message, "\n")

    # Return the downloaded document to the caller
    return web_page_contents


#
# --------------------------------------------------------------------#


# -----Student's Solution---------------------------------------------#
#
# Put your solution at the end of this file.
#

# Modules to be used later on (NOT a necessity - just extra feature)
from os import getcwd
from webbrowser import open_new_tab
from time import sleep

# <editor-fold desc="Model section">
# Program name
program_name = 'World News'

# Name of the exported news file. To simplify marking, your program
# should produce its results using this file name.
news_file_name =  'news.html'

# Link to image used in html
news_file_main_image = 'https://ya-webdesign.com/images250_/cowboy-svg-welcome-1.png'

# HTML templates, with blanks marked by asterisks
html_template = """
<!DOCTYPE html>
<html>

  <head>

    <meta charset = 'UTF-8'>
  
  </head>

<title>***MAINTITLE***</title>
<style>
        body    {background-color:BEIGE; 
                margin: 0;
                font-family:'Helvetica';
                }
                
        p       {margin-left:5%; 
                margin-right:5%;
                text-align:justify;
                font-family:'Helvetica';
                }
                
        h1      {margin-left:10%; 
                margin-right:10%;
                text-align:center; 
                color:DARKSLATEGRAY;
                font-family:'Helvetica';
                font-size:70px;
                }
                
        h2      {margin-left:10%; 
                margin-right:10%;
                text-align:center; 
                color:DARKSLATEGRAY;
                font-family:'Helvetica';
                }
                
        ol      {width:auto;
                text-align:center;
                font-family:'Helvetica';
                }
        
        hr      {border: 15px solid;
                color: TOMATO;
                text-align:center;
                }
                
        ul      {width:auto;
                display:inline-block;
                line-height:100%;
                }
                
        img     {border: TOMATO 4px ridge;
                marginleft:"10%";
                marginright:"10%";
                width:80%; 
                align:"middle";
                }
                
        

  * {
   box-sizing: border-box; 
  }
  #main {
    display: flex;
    min-height: calc(100vh - 40vh);
  }
  #main > article {
    flex: 1;
  }
  #main > aside {
    flex: 0 0 10vw;
    background: TOMATO;
  }
  header, footer, article, aside {
    padding: 1em;
  }
  footer {
    color:DARKSLATEGRAY;
    face=verdana,arial,sans-serif;
    font-size=25px;
    background: TOMATO;
    text-align:center;
    height: 25vh;
  }
  header {
    color:DARKSLATEGRAY;
    face=verdana,arial,sans-serif;
    font-size=25px;
    background: TOMATO;
    text-align:center;
    height: 50vh;
  }
</style>
<body>
  <header><h1>***MAINTITLE***</h1>
  <img style="border: NONE; width:34%; align:'left'" src="***MAINIMAGE***" alt="Image with the text 'head lines today">
  </header>
  <div id="main">
    <aside></aside>
    <article>***ARTICLE***</article>
    <aside></aside>
  </div>
  <footer><h2>Sources</h2>
    <ul>
        ***SOURCES***
    </ul>
  </footer>
</body>
</html>
"""
article_html_template = '''
        <h2>***TITLE***</h2>
      
        <p style="text-align:center;">
        <img src="***IMAGE***" alt="Image from ***PUBLISHER*** for the article with title '***TITLE***'">
        </p>

        <p>***TEXT***</p>
      
        <p><a href="***HYPERLINK***"><em>Read more</em></a></p>

        <p style="text-align:right">***PUBLISHER*** — ***DATEANDTIME***</p>
        
        <hr>
'''
sources_html_footer_template = '''
<li><a href="***SOURCELINK***">***SOURCE***</a></li>
'''
# informatonal strings (TODO: should be in .txt files and be read in from file)
about_message = '''Welcome to World News's news aggregator!

Statement of Authorship:

This is an individual assessment item.  By submitting this code I agree that it represents my own work.  I am aware 
of the University rule that a student must not act in a manner which constitutes academic dishonesty as stated and 
explained in QUT's Manual of Policies and Procedures, Section C/5.3 "Academic Integrity" and Section E/2.1 "Student 
Code of Conduct". 

    Student no: n10588281
    Student name: Kaspar Kielland

NB: Files submitted without a completed copy of this statement will not be marked.  Submitted files will be 
subjected to software plagiarism analysis using the MoSS system (http://theory.stanford.edu/~aiken/moss/). 

Assignment Description

News Feed Aggregator

In this assignment you will combine your knowledge of HTMl/XML mark-up languages with your skills in Python 
scripting, pattern matching, and Graphical User Interface design to produce a useful application that allows the 
user to aggregate RSS news feeds.
'''
instruction_message = ''' Welcome to World News's news aggregator!


This program are designed to help keeping you updated 
on news from your favorite news sources.*

How to use the main dashboard:
1. Select the number of stories from the designated 
   sources that you would like to know more about\n
2. Choose your preferences:
   2.1 'Generate html'
        Generates a html with the selected number 
        of stories from the designated news sources. 
        NB! Will only generate if one or more 
            stories are chosen\n
   2.2 'Open html after export'
        Opens html file in new tab on default browser.
        This option are only available after you 
        choose to 'Generate html'\n
   2.3 'Save stories to data base'
        Saves information from selected stories to the 
        database in the following format
            ['headline', 'link to story' (online), 'time and date']\n
3. Press the button on the right to preview your selected 
   number of stories from the designated news sources 
   along with any chosen preferences

How to use the menu bar:
'File' --> 'Open html' : Open html in default browser
         --> 'Save selections' : Save to data base
         --> 'Exit' : Exit program

'Edit' --> 'Appearance'
                    --> 'Dark mode' : Dark theme colors
                    --> 'Light mode' : Light theme colors
         --> 'Edit sources' : Change news sources*
         --> 'Copy' : Copy content of text box**
         --> 'Clear all fields' : Wipe information from all fields

* In this current version (ver. 1.0) you will not be able to change news sources 
** For this to work copy_to_clipboard() function on line 986 needs to import 'clipboard' module and code needs to be 
uncommented. See function for more detail. '''
# Full file path to data base file
db_file = getcwd() + '/news_log.db'

# List that hold important information for each source as well as attrbutes for their label/spinbox
news_source_widget_preferences = [
    # [publisher, url, status, date, row (for label/spinbox), column (for label/spinbox)]
    ['SBS News', 'http://www.sbs.com.au/news/rss/Section/Top+Stories', True, '19. Oct. 2019', 0, 0],  # Online
    ['Channel 9', 'https://www.9news.com.au/rss', True, '19. Oct. 2019', 1, 0],  # Online
    ['CNN News', 'http://rss.cnn.com/rss/cnn_topstories.rss', False, '19. Oct. 2019', 2, 0],  # Static
    ['NBC News', 'http://feeds.nbcnews.com/feeds/topstories', False, '18. Oct. 2019', 3, 0]  # Static
]


# </editor-fold>

# <editor-fold desc="Controller section">
def on_preview_button_clicked():
    """
    Main function to execute whle program (on preview button click)
    NOTE: bar() functon are called whn progress bar should be updated
    """
    # Disable button
    widgets[7][0].configure(state=DISABLED)
    bar(5)
    # Calls the function get_story_information with the function number_of_stories as parameter
    story_information = get_story_information(number_of_stories())
    bar(30)
    display_requested_articles(story_information)
    bar(30)
    if open_html_var.get():
        open_html_in_browser()
        bar(10)
    if save_selections_var.get():
        save_to_db()
        bar(10)
    # Make progress bar be completed
    bar(100 - progress_var)
    # Reset progress bar
    bar(0, 0.5, True)
    # Enable button
    widgets[7][0].configure(state=NORMAL)


def open_html_in_browser():
    """
    Defines filename and sends to open_new_tab function (from webbrowser module)
    """
    # Change path to reflect file location
    filename = 'file:///' + getcwd() + '/' + news_file_name
    # Open file with 'filename' in new tab on default browser (opens in new window if tab is not available)
    open_new_tab(filename)


def save_to_db():
    """
    Calls data base related functions if we have stories to commit
    """
    story_information = get_story_information(number_of_stories())
    if story_information:
        connection = create_connection(db_file)
        delete_all_stories(connection)
        commit_story(connection, story_information)
        if connection:
            connection.close()


# function to establish a database connection to an SQLite database specified by the database file.
def create_connection(file):
    """
    create a database connection to the SQLite database specified by file
    :param  file: database file
    :return: Connection object or None
    """
    connection = None
    try:
        connection = connect(file)
    except Error as e:
        print("Connection error: %s" % e)
    except Exception as e:
        print("Could not establish connection to file '%s''\nError message: %s" % file % e)
    finally:
        return connection


def commit_story(connection, stories):
    """
    Create a new project into the projects table
    NOTE! Insted of
    :parameter connection: Connection object
    :parameter stories: Full list of stories from the chosen news providers
    """
    sql = ''' INSERT INTO selected_stories(headline,news_feed,publication_date)
          VALUES(?,?,?) '''
    try:
        cur = connection.cursor()
        for story in stories:
            for requested_stories in range(story[0]):
                story_information = story[3][requested_stories], story[1], story[7][
                    requested_stories]
                cur.execute(sql, story_information)
        connection.commit()
    except Error as e:
        print("Database error: %s" % e)
    except Exception as e:
        print("Exception in commit: %s" % e)


def delete_all_stories(connection):
    """
    Delete all rows in the tasks table
    :param connection: Connection to the SQLite database
    :return:
    """
    sql = 'DELETE FROM selected_stories'
    try:
        cur = connection.cursor()
        cur.execute(sql)
        connection.commit()
    except Error as e:
        print("Database error: %s" % e)
    except Exception as e:
        print("Exception in commit: %s" % e)


def number_of_stories():
    """
    Gets the number of stories requested from each of the news sources
    :return: List of tuples containing information* about the stories that are selected
            *Information includes:
                            1. Number of stories requested
                            2. Name of news provider
                            3. Link to news providers RSS feed
                            4. Whether or not the news source should be an "Online" accessed source
    """
    # Define list to hold stories requested by user
    requested_articles = []
    try:
        # For every news source
        for news_source in news_source_widget_preferences:
            # get the index of the current news source
            index = news_source_widget_preferences.index(news_source)
            # get user input by utilizing index found above
            stories = int(widgets[5][index].get())
            # combine relevant infomation
            news_source_information = (stories, news_source[0], news_source[1], news_source[2])
            # add tuple to list
            requested_articles.append(news_source_information)
    except IndexError as e:
        print('Index error: %s' % e)
    except ValueError as e:
        print('Values are not correct!\nValue error: %s' % e)
    except Exception as e:
        print("Failed to gather number of stories requested\nError message: %s" % e)
    finally:
        return requested_articles


def get_story_information(news_providers):
    """
    Function description:
    For every selected provider the function
                            1; gets the content from the xml file (either from archived or web)
                            2; extracts tags and content in each story using RegEx
                            3; extracts content from tags using RegEx
                            4; cleans up content for some known characters
                            5; returns result
    :param news_providers: List of tuples containing information about the stories that are selected
    :return: Extended list of tuples with detailed information*
            *Information includes:
                            1. Number of stories requested
                            2. Name of news provider
                            3. Link to news providers RSS feed
                            4. Title of stories
                            5. Image links
                            6. Body/Description text for the story
                            7. Link to story (online)
                            8. Time and date stamp
    """
    # Defines list to hold all information from every story and news provider
    complete_information = []
    # Go through all news providers
    for provider in news_providers:
        # Sets list variables with understandebale name
        stories_requested = provider[0]
        this_news_provider = provider[1]
        news_feed = provider[2]
        is_online = provider[3]
        # Only do the following if user wants info from the current provider
        if stories_requested != 0:
            # Define variable to hold content
            content = ''
            # Set the full path name (uses os module)
            file_path = getcwd() + '/news/' + this_news_provider
            # If current news provider is an online based, then download using complementary download-function
            if is_online:
                content = download(news_feed, target_filename=file_path, save_file=False, filename_extension='xml')
            # otherwise try to read from archive
            else:
                try:
                    # Read the xml code from archived file
                    # The 'with - as' statement will open the file and ensures the file is closed when the block is left
                    with open(file_path + '.xml', 'r', encoding='UTF-8') as news_file:
                        content = news_file.read()
                except IOError as e:
                    print('Error with reading from file\nError message: %s' % e)

            # RegEx explenation: Capture everything inbetween 'item' opening and closing tag
            stories = gather_information(r'<item.*?>([\s\S]+?)</item>', content, 'top-level stories')
            # If stories contain anything then continue gather information
            if len(stories) != 0:
                # RegEx explenation: See right ->
                titles = gather_information(r'<title.*?>'  # expresseion should start with this opening tag
                                            r'(?:[\s\S])*?'  # then 0 or more whitespace or non-whitespace characters
                                            r'(?:<!\[CDATA\[)?'  # then a CDATA tag
                                            r'(.+?)'  # THIS PART CAPTURES WHAT WE WANT
                                            r'(?:\]\]>)??'  # until two closing squere brackets occurs
                                            r'</title>',  # then the expression should end with this closing tag
                                            str(stories), 'titles')
                texts = gather_information(r'<description.*?>'  # expresseion should start with this opening tag
                                           r'[\s\S]*?'  # then 0 or more whitespace or non-whitespace characters
                                           r'<!\[CDATA\['  # then a CDATA tag
                                           r'(?:<p>)??'  # then there may or may not be a paragraph tag
                                           r'([^><\]]+)'  # CAPTURES THIS PART until we meet one of these '><]'
                                           r'[\s\S]*?'  # then 0 or more whitespace or non-whitespace characters
                                           r'</description>',  # then the expression should end with this closing tag
                                           str(stories), 'texts')
                # If we're not able to find any texts from the above RegExp, then we try another that will
                if not texts:
                    # RegEx explenation: See right ->
                    texts = gather_information(r'<description.*?>'  # expresseion should start with this opening tag
                                               r'(?:\s*?)'  # then zero or more whitespace characters
                                               r'(.+?)'  # CAPTURES THIS PART
                                               r'(?:\s*?)'  # then zero or more whitespace characters
                                               r'</description>',
                                               # then the expression should end with this closing tag
                                               str(stories), 'texts')
                # Gather information using these simple RegExp
                hyperlinks = gather_information(r'<link.*?>[\s\S]*?(.+?)</link>', str(stories), 'hyperlinks')
                timestamps = gather_information(r'<pubDate.*?>(.+?)</pubDate>', str(stories), 'timestamps')
                # Define a list to hold images
                images = []
                # for every item (means everything inbetween item opening and closing tag
                for item in stories:
                    # RegEx explenation: See right ->
                    image = findall(r'<media:content'  # expresseion should start with this opening tag
                                    r'(?:[\s\S])*?'  # then 0 or more whitespace or non-whitespace characters
                                    r'url="([^">]+)"'  # CAPTURE everything inbeteen 'url="' and '"' as long as there 
                                    # is none of these '">'
                                    r'|$',  # sorround with single quotation marks
                                    str(item))[0]  # only take care of the first finding
                    if not image:
                        image = findall(r'(?:<img'  # expresseion should start with this unclosed opening tag
                                        r'[\s\S]*?[^">]+'  # then zero ore more [non-]whitespaces, but if we see one 
                                        # or more of these '">' we have gone to far
                                        r'src="([^" >]+)")'  # CAPTURE whats between 'src="' and '"' as long as 
                                        # there's none of these '" >' (NB! notice the space) 
                                        r'|$',  # sorround with single quotation marks
                                        str(item))[0]  # only take care of the first finding
                    # Append to image list
                    images.append(image)

                # Clean strings (see function for more info)
                titles = clean_up(titles)
                texts = clean_up(texts)

                # To be used when 'Edit' functionality are implemented
                # if news_source_widget_preferences[2]:
                #     news_source_widget_preferences[3] = findall(r'(\d{2} [a-zA-Z]{3} \d{4})', str(timestamps))[0]

                # Put everything in one tuple
                article_information = stories_requested, this_news_provider, news_feed, titles, images, texts, \
                                      hyperlinks, timestamps

                # TODO: Slice off un-needed information. See inspiration below (not functional)
                # for information in article_information[3:]:
                #     information = information[:stories_requested]
                #
                # article_information = [information[:stories_requested] for information in article_information[3:]]

                # Append information to list
                complete_information.append(article_information)
    return complete_information


def gather_information(regex, source, to_find):
    """
    Uses findall and specified regex to locate and gather wanted information
    :param regex: A custom regular expression used to capture wanted information
    :param source: From where the information should be gathered from
    :param to_find: What are we currently looking for (i.e. titles, texts, timestamps, etc.)
                    To be used in exception-handling
    :return: A list containing wanted information (if found)
    """
    items = []
    try:
        items = findall(regex, source)
    except Exception as e:
        print("Could not gather %s from file\nError message: %s" % to_find % e)
    finally:
        return items


def clean_up(items):
    """
    Cleans up items (a parameter) by replacing known string with corresponding symbol (or other)
    :param items: A list with strings to be cleaned
    :return: A clean list of strings
    """
    try:
        items = [item.replace('&#038;', '&') \
                     .replace('&#39;', '\'') \
                     .replace('&#039;', '\'') \
                     .replace('&rsquo;', '"') \
                     .replace('&lsquo;', '"') \
                     .replace('\\', '') \
                 for item in items]
    except Exception as e:
        print('Failed to execute replace command in clean_up function.\nError message: %s' % e)
    finally:
        return items


def display_requested_articles(news_source):
    """
    This function creates the message to be displayed for each story (that is selected) and display message in text box
    :param news_source: A list with information* from each selected news source
        *Information should includes:
                        1. Number of stories requested
                        2. Name of news provider
                        3. Link to news providers RSS feed
                        4. Title of stories
                        5. Image links
                        6. Body/Description text for the story
                        7. Link to story (online)
                        8. Time and date stamp
    """
    # Makes text box writable and accessible
    output_text.configure(state=NORMAL, cursor='arrow')
    output_frame.configure(text='Selected stories')

    # Empties text box
    output_text.delete(1.0, END)

    # Defines local variables
    complete_sources_html = ''
    complete_article_html = ''

    for article_information in news_source:
        # Re-defines names from list (easier to use)
        selected_stories = []
        publisher = []
        news_feed = []
        titles = []
        images = []
        texts = []
        hyperlinks = []
        time_stamps = []
        try:
            selected_stories = article_information[0]
            publisher = article_information[1]
            news_feed = article_information[2]
            titles = article_information[3]
            images = article_information[4]
            texts = article_information[5]
            hyperlinks = article_information[6]
            time_stamps = article_information[7]
        except IndexError as e:
            print('Failed to access information in list due to index error\nError message: %s' % e)
        except Exception as e:
            print('Failed to re-define names for input list in display_requested_articles function\n'
                  'Error message: %s' % e)

        try:
            for story_no in range(selected_stories):
                try:
                    # Get the single item from list for this story
                    title = titles[story_no]
                    image = images[story_no]
                    text = texts[story_no]
                    hyperlink = hyperlinks[story_no]
                    date_and_time = time_stamps[story_no]
                except IndexError as e:
                    print('Failed to access information in list due to index error\nError message: %s' % e)
                else:
                    # Construct message for this story
                    message_to_be_displayed = '"' + title + '" [' + publisher + ' – ' + date_and_time + ']\n\n'
                    # Print constructed message to text box
                    output_text.insert(END, message_to_be_displayed)
                    # Creates html code for all selected stories (only if user wants html to be generated)
                    if generate_html_var.get():
                        complete_article_html += generate_article_html(title, image, text, hyperlink, publisher,
                                                                       date_and_time)
                    # Update progress bar
                    bar(abs(50 - progress_var) / (selected_stories * 10))
        except ValueError as e:
            print('Incorrect value\nError message: %s' % e)
        except TypeError as e:
            print('Incorrect type\nError message: %s' % e)
        except Exception as e:
            print('Failed to create story message and output to text box\nError message: %s' % e)

        # Update progress bar
        bar(abs(progress_var) / (selected_stories * 5))

        # Creates html code for footer (only if user wants html to be generated)
        if generate_html_var.get():
            complete_sources_html += generate_source_footer_html(news_feed, publisher)

    # Sets text box to display appropriate message if no stories are selected
    if output_text.compare('end - 1 char', '==', '1.0'):
        output_text.insert(END, 'No stories selected')
    # Execute below code if > 0 stories are selected and user want to generate html
    elif generate_html_var.get():
        # Remove redundant <hr>-tag
        complete_article_html = complete_article_html[:-5]
        generate_news_html(complete_article_html, complete_sources_html)
    # Disables text box
    output_text.configure(state=DISABLED, cursor='arrow')


def generate_article_html(title, image, text, hyperlink, publisher, time_stamp):
    """
    Generates html-code for article part of the html document by replacing template with story info
    :param title: Title of the story
    :param image: Image of the story
    :param text: Description text of the story
    :param hyperlink: Hyperlink to the online story
    :param publisher: Publisher/News-source of the story
    :param time_stamp: Time and date for when the story was published
    :return: html-code for "this" story
    """
    # Make local copy of template
    article_html_code = article_html_template
    try:
        # Replace the "blanks"/(***HERE***) in the HTML template with current story info
        article_html_code = article_html_code.replace('***TITLE***', title)
        article_html_code = article_html_code.replace('***IMAGE***', image)
        article_html_code = article_html_code.replace('***TEXT***', text)
        article_html_code = article_html_code.replace('***HYPERLINK***', hyperlink)
        article_html_code = article_html_code.replace('***PUBLISHER***', publisher)
        article_html_code = article_html_code.replace('***DATEANDTIME***', time_stamp)
    except Exception as e:
        print('Failed to execute replace command in generate_article_html function.\nError message: %s' % e)
    finally:
        return article_html_code


def generate_source_footer_html(sourcelink, source):
    # Make local copy of template
    source_html_code = sources_html_footer_template
    try:
        # Replace the "blanks"/(***HERE***) in the HTML template with current source info
        source_html_code = source_html_code.replace('***SOURCELINK***', sourcelink)
        source_html_code = source_html_code.replace('***SOURCE***', source)
    except Exception as e:
        print('Failed to execute replace command in generate_source_footer_html function.\nError message: %s' % e)
    finally:
        return source_html_code


def generate_news_html(complete_article_html, complete_sources_html):
    # Make local copy of template
    html_code = html_template
    try:
        # Replace the "blanks"/(***HERE***) in the main HTML template with html info
        html_code = html_code.replace('***MAINTITLE***', program_name)
        html_code = html_code.replace('***MAINIMAGE***', news_file_main_image)
        html_code = html_code.replace('***ARTICLE***', complete_article_html)
        html_code = html_code.replace('***SOURCES***', complete_sources_html)
    except Exception as e:
        print('Failed to execute replace command in generate_news_html function.\nError message: %s' % e)
    else:
        try:
            # Write the HTML code to a Unicode text file
            # The 'with - as' statement will open the file and ensures the file is closed when the block is left
            with open(news_file_name, 'w', encoding='UTF-8') as html_file:
                html_file.write(html_code)
        except IOError as e:
            print('Error with writing to file\nError message: %s' % e)


def bar(value=0, time=.05, reset=False):
    """
    Updates the progressbar
    :param value: How much should the progressbar increase
    :param time: How long should the machine sleep for (only for aesthetics as this is a single-thread program(?))
    :param reset: Boolian; should the progressbar reset to 0
    """
    # Increase the value of the progress bar
    progress['value'] += value
    # Update window so it will dispay the progress
    master_window.update_idletasks()
    # Make thread sleep (only for aesthetic)
    sleep(time)
    # Reset back to zero and update again
    if reset:
        progress['value'] = 0
        master_window.update_idletasks()


def on_chk_clicked():
    if generate_html_var.get():
        widgets[6][1].configure(state=NORMAL)
        if open_html_var.get() and not save_selections_var.get():
            preview_button.configure(text='Preview stories,\nGenerate html and\nOpen in browser')
        elif not open_html_var.get() and save_selections_var.get():
            preview_button.configure(text='Preview stories,\nGenerate html and\nSave selections')
        elif open_html_var.get() and save_selections_var.get():
            preview_button.configure(text='Preview stories,\nGenerate html,\nOpen in browser and\nSave selections')
        else:
            preview_button.configure(text='Preview stories and\nGenerate html')
    else:
        widgets[6][1].deselect()
        widgets[6][1].configure(state=DISABLED)
        if save_selections_var.get():
            preview_button.configure(text='Preview stories and\nSave selections')
        else:
            preview_button.configure(text='Preview stories')


def change_theme(is_dark):
    global text_color
    global background

    temp_holder = background
    background = text_color
    text_color = temp_holder

    bg_color_change_widgets = [widgets[0], widgets[1], widgets[2], widgets[3], widgets[4], widgets[5], widgets[6],
                               widgets[8],
                               widgets[10]]
    fg_color_change_widgets = [widgets[1], widgets[2], widgets[3], widgets[5], widgets[6], widgets[7],
                               widgets[8], widgets[10]]
    try:
        for widget in bg_color_change_widgets:
            for item in widget:
                item.configure(background=background)
        for widget in fg_color_change_widgets:
            for item in widget:
                item.configure(foreground=text_color)
        for item in widgets[6]:
            item.configure(selectcolor=background)
        for item in widgets[5]:
            item.configure(readonlybackground=background, buttonbackground=background)
        for item in widgets[4]:
            if news_source_widget_preferences[widgets[4].index(item)][2]:
                item.configure(foreground=text_color)
    except Exception as e:
        print('Failed to update widget with new colors\nError message: %s' % e)
        temp_holder = background
        background = text_color
        text_color = temp_holder

        for widget in bg_color_change_widgets:
            for item in widget:
                item.configure(background=background)
        for widget in fg_color_change_widgets:
            for item in widget:
                item.configure(foreground=text_color)
        for item in widgets[6]:
            item.configure(selectcolor=background)
        for item in widgets[5]:
            item.configure(readonlybackground=background, buttonbackground=background)
        for item in widgets[4]:
            if news_source_widget_preferences[widgets[4].index(item)][2]:
                item.configure(foreground=text_color)
    else:
        if is_dark:
            appearance_submenu.entryconfigure(0, state=DISABLED)
            appearance_submenu.entryconfigure(1, state=NORMAL)
        else:
            appearance_submenu.entryconfigure(0, state=NORMAL)
            appearance_submenu.entryconfigure(1, state=DISABLED)
        # Shows the user that the above code has been executed
        bar(100, 0.7, True)


def hello():
    print("hello!")


def copy_to_clipboard():
    """
    Copies text in text box to clipboard
    Requires module clipboard to be imported
        On windows: py -m pip install clipboard
        ________OR  python -m pip install clipboard
        On macOS:   pip install clipboard
    """
    # import clipboard
    # output_text.configure(state=NORMAL)
    # # Sets clipboard content to be string from text box except last two newline characters
    # clipboard.copy(output_text.get("1.0", 'end - 3 char'))
    # output_text.configure(state=DISABLED)
    # Shows the user that the above code has been executed
    bar(100, 0.7, True)


def clear_all():
    try:
        for spinbox in widgets[5]:
            spinbox.configure(state=NORMAL)
            spinbox.delete(0, 10)
            spinbox.insert(INSERT, 0)
            spinbox.configure(state='readonly')
        for chk_box in widgets[6]:
            chk_box.deselect()
        widgets[10][0].configure(state=NORMAL)
        widgets[10][0].delete(1.0, END)
        widgets[10][0].configure(state=DISABLED)
    except Exception as e:
        print('Failed to clear fields\nError message: %s' % e)
    else:
        # Shows the user that the above code has been executed
        bar(100, 0.7, True)


def open_html_menu_cmd():
    open_html_in_browser()
    # Shows the user that the above code has been executed
    bar(100, 0.7, True)


def save_db_menu_cmd():
    save_to_db()
    # Shows the user that the above code has been executed
    bar(100, 0.7, True)


def display_message(title, message):
    widgets[8][0].configure(text=title)
    widgets[10][0].configure(state=NORMAL)
    widgets[10][0].delete(1.0, END)
    widgets[10][0].insert(END, message)
    widgets[10][0].configure(state=DISABLED)
    # Shows the user that the above code has been executed
    bar(100, 0.7, True)


# </editor-fold>

# <editor-fold desc="View section">
# Define color and text constants
background = 'BEIGE'
text_color = 'DARKSLATEGRAY'
contrast_color = 'TOMATO'
header_1 = ('Helvetica, 28')
header_2 = ('Helvetica, 22')
header_3 = ('Helvetica, 18')
body = ('Helvetica, 14')
footer = ('Helvetica, 12')

# List to hold all widgets
widgets = []

# Creating window
master_window = Tk()
# Sets window background color
master_window['bg'] = background

# Define window size and position
width = (master_window.winfo_screenwidth()) * (9 / 20)
height = (master_window.winfo_screenheight()) * (17 / 20)
pos_x = (master_window.winfo_screenwidth()) / 2 - width / 2
pos_y = 10

# Sets window size and position
master_window.wm_geometry("%dx%d+%d+%d" % (width, height, pos_x, pos_y))

# Set grid weight to master_window for column and row so window will resize more nicely
for row_no in range(6):
    Grid.rowconfigure(master_window, row_no, weight=1)
for col_no in range(3):
    Grid.columnconfigure(master_window, col_no, weight=1)

# Window title
master_window.title(program_name)
# Widgets will get focus whenever mouse pointer moves over it
master_window.tk_focusFollowsMouse()

# Add to widget list [0]
widgets.append([master_window])

# Create the title label
title_label = Label(master_window,
                    text='Welcome to ' + program_name, font=header_1,
                    fg=text_color, bg=background)
# Positions the label at top-center
title_label.grid(row=0, column=0, columnspan=3, sticky=W + E + N + S)
# Add to widget list [1]
widgets.append([title_label])

# Create the program icon and display it through a label
feed_image = PhotoImage(file='RSS_Globe-256x256.png')
feed_logo = Label(master_window, image=feed_image, bg=background)
# Positions the program icon at right upper corner
feed_logo.grid(row=1, column=1, columnspan=2, rowspan=2, sticky=W + E + N + S, padx=5, pady=5)
# Add to widget list [2]
widgets.append([feed_logo])

# Create frame to hold news sources and spinboxes
news_src_frame = LabelFrame(master_window,
                            text='Choose your stories', font=header_3,
                            bg=background, bd=5, fg=text_color,
                            padx=5, pady=2, labelanchor=N + W,
                            relief=SOLID)
# Positions the frame at left upper corner
news_src_frame.grid(row=1, column=0, padx=20, pady=10, sticky=W + E + N + S)
# Add to widget list [3]
widgets.append([news_src_frame])

# list to hold all labels
labels = []
# For every source we need a label
for news_source_label in news_source_widget_preferences:
    # if source is set as online
    if news_source_label[2]:
        # then set the text and color to be displayed accordingly
        label_text = news_source_label[0] + '\n' + 'Online'
        color = text_color
    # otherwise set text and color to be displayed as archived
    else:
        label_text = 'Archived - ' + news_source_label[0] + '\nLast update: ' + news_source_label[3]
        color = contrast_color
    # Build label
    new_label = Label(news_src_frame,
                      text=label_text, font=body, fg=color, justify=RIGHT,
                      anchor=E, bg=background)
    # Make row and column inside LabelFrame resizable as well
    Grid.rowconfigure(news_src_frame, news_source_label[4], weight=1)
    Grid.columnconfigure(news_src_frame, news_source_label[5], weight=1)
    # Position label
    new_label.grid(row=news_source_label[4], column=news_source_label[5], columnspan=2, pady=10, sticky=W + E + N + S)
    # Add to list
    labels.append(new_label)
# Add to widget list [4]
widgets.append(labels)

# list to hold spinboxes
spinboxes = []
# For every source we need a spinbox
for news_source_spinbox in news_source_widget_preferences:
    # Build spinboxes
    new_spinbox = Spinbox(news_src_frame,
                          font=header_3,
                          width=2, justify=CENTER, buttonuprelief=SOLID,
                          from_=0, to=10, highlightthickness=0, readonlybackground=background, state='readonly',
                          bg=background, buttonbackground=background, fg=text_color)
    # position all spinboxes
    new_spinbox.grid(row=news_source_spinbox[4], column=news_source_spinbox[5] + 2, pady=10, sticky=E)
    # Add to spinbox list
    spinboxes.append(new_spinbox)
# Add to widget list [5]
widgets.append(spinboxes)

generate_html_var = IntVar()
open_html_var = IntVar()
save_selections_var = IntVar()

check_button_preferences = [
    ['Generate html', generate_html_var, 2, 0, NORMAL],
    ['Open in browser', open_html_var, 3, 0, DISABLED],
    ['Save selections', save_selections_var, 4, 0, NORMAL]
]
check_buttons = []
for chk_btn in check_button_preferences:
    new_chk_btn = Checkbutton(master_window,
                              text=chk_btn[0], font=footer,
                              fg=text_color, bg=background, selectcolor=background, state=chk_btn[4],
                              command=on_chk_clicked, variable=chk_btn[1])
    new_chk_btn.grid(row=chk_btn[2], column=chk_btn[3], columnspan=2, padx=20, sticky=W)
    check_buttons.append(new_chk_btn)
# Add to widget list [6]
widgets.append(check_buttons)

preview_button = Button(master_window,
                        text='Preview stories', font=header_3,
                        command=on_preview_button_clicked,
                        activeforeground=contrast_color, activebackground=text_color,
                        bg=contrast_color, fg=text_color, highlightbackground=contrast_color)
preview_button.grid(row=2, column=1, columnspan=2, rowspan=3, padx=20, sticky=W + E + N + S)
# Add to widget list [7]
widgets.append([preview_button])

output_frame = LabelFrame(master_window,
                          text='Selected stories', font=header_3,
                          bg=background, bd=5, fg=text_color,
                          padx=5, pady=2, labelanchor=NW,
                          relief=SOLID)
output_frame.grid(row=5, column=0, columnspan=3, padx=20, pady=10, sticky=W + E + N + S)
# Add to widget list [8]
widgets.append([output_frame])

# Vertical (y) Scroll Bar
yscrollbar = Scrollbar(output_frame)
yscrollbar.pack(side=RIGHT, fill=Y)
output_text = Text(output_frame,
                   font=body, wrap=WORD,
                   bg=background, fg=text_color,
                   width=45, height=15,
                   yscrollcommand=yscrollbar.set)
output_text.configure(state=DISABLED, cursor='arrow')
yscrollbar.config(command=output_text.yview)
# Add to widget list [9]
widgets.append([yscrollbar])
output_text.pack(padx=10, pady=0, fill=BOTH, expand=TRUE)
# Add to widget list [10]
widgets.append([output_text])

progress_var = 0
progress = Progressbar(master_window, orient=HORIZONTAL, length=100, mode='determinate', variable=progress_var)
progress.grid(row=6, column=0, columnspan=3, padx=20, pady=10, sticky=W + E + N + S)
# Add to widget list [11]
widgets.append([progress])
# Adds a menubar to the program
menubar = Menu(master_window)

# create a pulldown menu, and add it to the menu bar
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="Open html", command=open_html_menu_cmd)
filemenu.add_command(label="Save selections", command=save_db_menu_cmd)
filemenu.add_separator()
filemenu.add_command(label="Exit", command=master_window.quit)
menubar.add_cascade(label="File", menu=filemenu)

# create more pulldown menus
editmenu = Menu(menubar, tearoff=0)
appearance_submenu = Menu(editmenu, tearoff=0)
appearance_submenu.add_command(label="Dark mode", command=lambda: change_theme(True))
appearance_submenu.add_command(label="Light mode", command=lambda: change_theme(False), state=DISABLED)
editmenu.add_cascade(label='Appearance', menu=appearance_submenu)
editmenu.add_command(label="Edit sources", command=hello)
editmenu.add_command(label="Copy", command=copy_to_clipboard)
editmenu.add_command(label="Clear all fields", command=clear_all)
menubar.add_cascade(label="Edit", menu=editmenu)

helpmenu = Menu(menubar, tearoff=0)
helpmenu.add_command(label="About", command=lambda: display_message('About', about_message))
helpmenu.add_command(label="Instructions", command=lambda: display_message('Instructons', instruction_message))
menubar.add_cascade(label="Help", menu=helpmenu)

# display the menu
master_window.config(menu=menubar)

# Restricting window to change it's size
master_window.resizable(0, 1)
# </editor-fold>

# Start the event loop
master_window.mainloop()
