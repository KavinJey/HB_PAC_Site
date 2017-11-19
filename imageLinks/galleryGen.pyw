#Purpose: to create gallery html pages for hbpac.club in a quick a seamless fashion

import random
import string
import os

def imageRows(n, filepath):
    htmlText = []
    htmlText.append('''\n\t<div class="container-fluid">\n\t\t<div class="row">''')
    count = 0
    for x in range(n, 0, -1):
        count += 1
        htmlText.append('''\n\t\t\t<div class="col-md-3">\n\t\t\t\t<a class="thumbnail" href="''' +filepath)
        htmlText.append(str(x) + '.jpg">')
        htmlText.append('\n\t\t\t\t\t<img src="' + filepath)
        htmlText.append(str(x) + '.jpg">')
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


def fileRename(filepath):
    path = filepath
    files = os.listdir(path)
    i = 1

    for file in files:
        os.rename(os.path.join(path, file), os.path.join(path, str(i) + '.jpg'))
        i = i + 1




f = open(randomLink(),'a+')


#Writes the header and stuff
f.write('''<html lang="en">


<head>

  <meta name="google-site-verification" content="wpVtv0tfYqiRZGLLweiK_q34qUh5i4MoxHtNh9piVnM" />
  <meta name="viewport" content="user-scalable=no, width=device-width, initial-scale=1.0" />
  <meta name="apple-mobile-web-app-capable" content="yes" />


  <title> HBPAC </title>

  <!-- Bootstrap -->
  <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css" integrity="sha384-BVYiiSIFeK1dGmJRAkycuHAHRg32OmUcww7on3RYdg4Va+PmSTsz/K68vbdEjh4u" crossorigin="anonymous">

  <!-- Fonts -->
  <link href="https://fonts.googleapis.com/css?family=Arvo|Bree+Serif|Roboto" rel="stylesheet">

  <!-- CSS for index -->

  <link rel="stylesheet" href="/../css/styles.css">

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
            <img id="logo" src="../images/brand.png">
          </a>
        </div>

        <!-- Deparments/About/Contacts -->
        <div class="collapse navbar-collapse navbar-right" id="mynavbar">
          <ul class="nav navbar-nav">
            <li><a href="/departments.html">Meet The Team</a></li>
            <li><a href="#">Departments</a></li>
            <li><a href="/contact.html">Contact</a></li>
          </ul>
        </div>
      </div>
    </nav> <!-- End of Nav -->''')

n = int(input('Enter amount of images\n'))
m = input('Enter folder name of said images\n')

m = "../imageLinks/images/" + m + "/"

fileRename(m)
f.write(imageRows(n, m)) #Making of rows of images

#Fadding the footer
f.write('''
    <!-- Footer -->
    <div class="container-fluid">
      <div class="row extendfull footer">

        <div class="col-sm-12 col-md-12">

          <div style="margin: 2%;" class="row">
            <div  class="col-sm-4 col-md-4">
              <img class="img-responsive" src="/images/brand.png" width="30%" height="auto">
              <h4 style=""> Stay Connected </h4>
            </div>
            <div style="" class="col-sm-12 col-md-3 col-md-offset-5 pull-right">
              <a href="https://twitter.com/hb_pac"> <i style="color: #FFF;" class="fa fa-twitter fa-4x" aria-hidden="true"></i> </a>
              <a href="https://www.youtube.com/channel/UCSiYzZbr4e1KwwDMA8F4q7A"> <i style="color: #FFF;" class="fa fa-youtube fa-4x" aria-hidden="true"></i> </a>
              <a href="https://www.instagram.com/hb_pac/"> <i style="color: #FFF;" class="fa fa-instagram fa-4x" aria-hidden="true"></i> </a>
              <a href="https://www.facebook.com/HBPAC/"> <i style="color: #FFF; " class="fa fa-facebook fa-4x" aria-hidden="true"></i> </a>
            </div>
          </div>


        <div class="row">
          <div class="col-sm-12 col-md-12 " style="text-align: center;">
            <p> <small> HBPAC 2015-2017&copy; <small> </p>
            </div>
          </div>
        </div>
      </div>
      </div>

    </div><!-- End of Footer -->

  </div><!-- End of Body Container -->


      <!-- jQuery Version 1.11.1 -->
      <script src="js/jquery.js"></script>

      <!-- jQuery -->
      <script src="js/jquery.js"></script>

      <!-- Bootstrap Core JavaScript -->
      <script src="js/bootstrap.min.js"></script>

      <!-- Scrolling Nav JavaScript -->
      <script src="js/jquery.easing.min.js"></script>
      <script src="js/scrolling-nav.js"></script>



    </body>

    </html>''')


f.close()
