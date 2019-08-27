# GALLERY
###### By **[JOHN ONYANGO](https://github.com/Johnonyango/gallery)**


## Description
[Gallery](https://affluen.herokuapp.com/)application allows users to have a view of different photos based on location and category and search different photos they want.They can also copy link to that photo and view the photo on a window.


## Setup/Installation Requirements
1. Live site at https://affluen.herokuapp.com
2. Copy  and  Paste the link on your prefered browser
3. Install requirements e.g:
_*pip install django==2.2.4 -- to install django _*
_*pip intsall django-bootstrap3._*
4. Run the app on server by command python3.6 manage.py runserver.
5. Click on any photo to copy a link od view its details i.e description and name.
6. Tap the close button or icon to go back to the gallery.
7. To view photos according on their location, tap on the drop down menu in the navbar.

## Specifications
1. Users can view different photos that interest  them.
2. Users can click on a single photo to expand it and also view the details of the photo.
3. Users can search for different photos. (ie. Sports, Food, etc)
4. Users can copy a link to the photo to share with their friends.
5. Users can view photos based on the location they were taken.

## To clone this Repo
1. Run the following command on the terminal: git clone https://github.com/Johnonyango/gallery 
2. cd gallery
3. Open with your preffered text editor

## Activate virtual environment
Activate virtual environment using python3.6 as the default handler

virtualenv -p /usr/bin/python3.6 venv && source venv/bin/activate

## Create the Database
1. Run psql command
2. CREATE DATABASE gallery;
3. \c gallery to connect to your database

##Run initial Migration
python3.6 manage.py makemigrations photos
python3.6 manage.py migrate

# Running Tests
* python3.6 manage.py test

## Run the app
python3.6 manage.py runserver
Open terminal on localhost:8000
copy paste to your preffered browser

# Django Admin
* Username:dejohh
* Password:12345

## Known Bugs 
1. Images showing locally but on heroku app they come blank.

## Technologies & Resources/Tools Used
Technologies used include:
* Python3.6(Django) 
* HTML
* CSS
* Bootstrap
* Postgres Database
* Heroku - for app hosting live
* Git - for app details


## Contact for support:
For more info or assistance(If there is a bug in my code), please contact:
j.yayah7@gmail.com

## MIT License
Copyright (c) 2019 John Onyango

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

Copyright (c) 2019 JOHN ONYANGO
