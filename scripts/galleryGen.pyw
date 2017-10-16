#Purpose: to create gallery html pages for hbpac.club in a quick a seamless fashion

import random
import string

def imageRows(n, filepath):
    htmlText = []
    htmlText.append('''\n\t<div class="container-fluid">\n\t\t<div class="row">''')
    count = 0
    for x in range(n, 0, -1):
        count += 1
        htmlText.append('''\n\t\t\t<div class="col-md-3">\n\t\t\t\t<a class="thumbnail" href="''' +filepath)
        htmlText.append(str(x) + '.JPG">')
        htmlText.append('\n\t\t\t\t\t<img src="' + filepath)
        htmlText.append(str(x) + '.JPG">')
        htmlText.append('''</a>\n\t\t\t</div>''')

        if(count==4):
            count = 0
            htmlText.append('\n\t\t</div>\n')
            htmlText.append('\n\t\t<div class="row">')

    htmlText.append('\n\t\t</div>\n\t</div>')




    htmlText = "".join(htmlText)
    return htmlText

def randomLink():
    url  = [] #basically where all the random ints and strings are gonna be
    letter = 'a'
    num = 0
    for x in range(7):
        x = random.randint(0,1)
        if x==0:
           letter = random.choice(string.ascii_letters)
           url.append(letter)
        else:
            num = str(random.randint(0,9))
            url.append(num)

    url.append('.html')

    return ''.join(url)





f = open(randomLink(),'a+')


#Writes the header and stuff
f.write('''<html lang="en">


<head>

<meta name="google-site-verification" content="wpVtv0tfYqiRZGLLweiK_q34qUh5i4MoxHtNh9piVnM" />
<meta http-equiv="X-UA-Compatible" content="IE=edge">
<meta name="viewport" content="width=device-width, initial-scale=1.0">


<title> HBPAC </title>

<!-- Bootstrap -->
<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css" integrity="sha384-BVYiiSIFeK1dGmJRAkycuHAHRg32OmUcww7on3RYdg4Va+PmSTsz/K68vbdEjh4u" crossorigin="anonymous">
<link href="assets/css/bootstrap-responsive.css" rel="stylesheet">

<!-- Fonts -->
<link href="https://fonts.googleapis.com/css?family=Roboto" rel="stylesheet">

<!-- CSS for index -->
<link rel="stylesheet" href="CSS/styles.css">
<link rel="stylesheet" href="css/styles.css"
<link href="css/bootstrap.min.css" rel="stylesheet">

<!-- Javascript -->
<script type="text/javascript" src="javascript.js"></script>
<script src="https://use.fontawesome.com/e2ea768ee0.js"></script>



</head>

<body>

  <!-- Container for viewport -->
<div class="container-fluid">

    <!-- Bar for navigation includes main bar for  {Home, Departments and Contact} -->
    <nav class="navbar navbar-default navbar-fixed" id="z-property" role="navigation">
      <div class="container-fluid">
        <!-- Logo -->
        <div class="navbar-header">
          <button type="button" class="navbar-toggle" data-toggle="collapse" data-target="#mynavbar">
            <span class="sr-only">Toggle navigation</span>
            <span class="icon-bar"></span>
            <span class="icon-bar"></span>
            <span class="icon-bar"></span>
          </button>
          <a class="navbar-brand" href="/index.html">
            <img id="logo" src="images/brand.png" width="4%" height="100%">
          </a>
        </div>

        <!-- Deparments/About/Contacts -->
        <div class="collapse navbar-collapse navbar-right" id="mynavbar">
          <ul class="nav navbar-nav">
            <li><a href="http://www.hbpac.club/departments.html">Meet The Team</a></li>
            <li><a href="http://www.hbpac.club/about.html">About</a></li>
            <li><a href="http://www.hbpac.club/contact.html">Contact</a></li>
          </ul>
        </div>
      </div>
    </nav>''')

n = int(input('Enter amount of images'))
m = input('Enter Filepath of said images')

f.write(imageRows(n, m)) #Making of rows of images

#Fadding the footer
f.write('''<div class="container-fluid">
          <div class="row extendfull footer">
            <div class="col-md-6 col-xs-4">
                <a class"" href="http://www.hbpac.club">
                  <img class="icon" src="images/brand.png"/> </a>
                  <p class="">
                    <small>
                      HBPAC &copy; 2016
                      <br>
                      Proudly Created by: S. Williams
                      <br> <span style="margin-left:9.3em"> J. Jeyaranjan
                      </small>
                    </p>
                  </div>
                  <div class="col-md-6 col-xs-4 text-right spacing">
                    <ul class="list-inline">
                      <li> <a href="https://www.instagram.com/hb_pac/" class="btn btn-lg"><i class="fa fa-instagram fa-2x" aria-hidden="true"></i> </a> </li>
                      <li> <a href="https://www.youtube.com/channel/UCSiYzZbr4e1KwwDMA8F4q7A" class="btn btn-lg"><i class="fa fa-youtube-play fa-2x" aria-hidden="true"></i> </a> </li>
                      <li> <a href="https://www.facebook.com/HBPAC/?ref=aymt_homepage_panel" class="btn btn-lg"><i class="fa fa-facebook fa-2x" aria-hidden="true"></i> </a> </li>
                    </ul>
                    <ul class="list-inline">
                      <li> <a href="http://www.hbpac.club/departments.html"> <p> Departments </p> </a> </li>
                      <li> <a href="http://www.hbpac.club/about.html"> <p> About </p> </a> </li>
                      <li> <a href="http://www.hbpac.club/contact.html"> <p> Business </p> </a> </li>
                    </ul>

                  </div>
                </div>
            </div>''')


f.close()