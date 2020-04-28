[![Build Status](https://travis-ci.org/sheldon18/cinebox.svg?branch=master)](https://travis-ci.org/sheldon18/cinebox)

# Cinebox Movies <a name="introduction"></a> 


This website is an e-commerce website built as a part of the Code Institue Full Stack Software Development course.
This milestone-4 project is an online movie store for potential customers to browse and buy 4k Blu-ray discs.
All content is for educational purposes and I request that no real credit card information is submitted into the payment form.




[Cinebox App](https://cinebox-movies.herokuapp.com) </br>
[Cinebox GitHub Repo](https://github.com/sheldon18/cinebox)
</br></br>



-----
## Table of contents
1. [Introduction](#introduction)
2. [Wireframes](#wireframes)
3. [Technologies and External APIs](#techonologies)
4. [UX](#ux)
    1. [Features](#uxfeatures)
    2. [User Stories](#uxstories)
5. [Testing](#testing)
6. [Deployment](#deployment)
    1. [Local Deployment](#localdeploy)
    2. [Heroku Deployment](#herokudeploy)
7. [Credits & Acknowledgements](#credits)
8. [Media](#media)
9. [Disclaimer](#disclaimer)

## Wireframes <a name="wireframes"></a>


<p align="center"><img src="https://user-images.githubusercontent.com/44424348/78755946-1887d380-79ce-11ea-8df7-9addb9928adc.png" /></p>




<a href="#top">Back to top</a>

## Technologies and External APIs <a name="techonologies"></a>

- Project created using __AWS C9__ IDE
- __Balsamiq Wireframes__ tool for wireframes
- __HTML__
- __CSS__
- __JavaScript - JQuery__
- __CDNJS cloudfare__ script tag for executing jQuery
- __Python - Django 1.11.29__
- __Bootstrap__
- __Google APIs__
- __GitHub__ for version control
- __Heroku__ to host the website
- 3rd party free logo creator and editing tools used to create logo
- 3rd party retro font - __Haarlem Deco__
- __Pillow__
- __Travis-CI__
- __SQLite__ for local database
- __Postgres__ database
- __Stripe__ for payment processing
- GitHub issues section to generate links to add wireframe images to README.


<a href="#top">Back to top</a>


## UX <a name="ux"></a>

### Features <a name="uxfeatures"></a>
- Simple and easy-to-use/navigate e-commerce website.
- Manually created logo image links to home page on all webpages.
- 3rd party font used to give a more movie-marquee-like feel to the movie titles. 
- Session stores the users' cart items until browser is closed or purchases are completed.
- Stripe payment integration used for safe payment processing.
- Contact information provided so that user/potential purchaser feels comfortable and safe on an e-commerce website
- Responsive design for any device/layout.
- Smooth and easy-to-follow Sign In, Sign Out, Sign Up and Checkout functionality
- Credit Card information is submitted directly to Stripe, no payment information is stored in the this website's database.
- Never a need to use the Back button to move through the site.
- EmailAPI added to the contact and 'Request a movie' fields.
- For Code Institute Assessors only: please contact me via email if you need me to create an admin access login for testing (if required)

### User Stories <a name="uxstories"></a>

Done? | As a user I want to... 
:---:| ---
✅|be able  to  open this app on any device
✅|be able to  view movies without having the need to sign in
✅|be able to create an account myself 
✅|be able to login
✅|be able to logout
✅|be able to see my profile page
✅| see  the number  of  items that i add to  my cart
✅| see the actual items in my cart 
✅| be able to use the search bar to find movies
✅| be able to contact cinebox if  i cant  find a movie
✅| view  trailers  of the movies on a new tab
✅| be able to purchase mutiple items of the same movie
✅| be able to adjust  quantity of specific items in the cart
✅| be able to  remove items from the cart
✅| be able to process full checkout (delivery  and payment information)
⬜️|be able to add my own movies (Sorry, this feature is not available as this is an e-commerce website for cinebox movies.)



 <a href="#top">Back to top</a>
 
 
## Testing <a name="testing"></a>
 
- __W3C Markup Validation Service__ used to validate code all HTML pages  by direct input.
- __W3C CSS Validation Service__ used to validate CSS code by direct input.
- __Chrome dev tools__ and __Mozilla inspect element tool__ used for testing HTML and CSS.
- __JSHint__ used to validate CSS code by direct input.
- All Python code conforms to __PEP8__ style guide.
- Browser __console log__ used for testing layout, responsiveness and user actions.
- Tested webhook between GitHub and Heroku.
- Auto-deploy tested
- __Travis-CI__ use to test Continuous Integration. Removed/Updated numerous AWS C9 auto installed apps from requirements.txt file to get Travis to pass.

[![Build Status](https://travis-ci.org/sheldon18/cinebox.svg?branch=master)](https://travis-ci.org/sheldon18/cinebox)


<a href="#top">Back to top</a>

## Deployment <a name="deployment"></a>

### Local Deployment <a name="localdeploy"></a>

Used __AWS C9__ IDE for this project. Click [here](https://github.com/sheldon18/cinebox) for GitHub repository.

- Using AWS C9 I had to create below alias in the .bashrc file as compared to .bash_alias file (as shown in tutorial videos).
   <br> alias run="python3 manage.py runserver $IP:$C9_PORT"
- 'sudo-pip3-installed' all required packages via terminal interface.
- 'python3 manage.py makemigrations' and 'python3 manage.py migrate' done at the end of adding each app.
- SQLite3 database used for local deployment.
- .env.py file created to store all sensitive variables securely.
- .gitignore added to restrict security sensitive files being uploaded to GitHub.
- Ran project on local Django server: [http://127.0.0.1:8080/](http://127.0.0.1:8080/)
- Django Admin superuser created to access admin panel and to add items.
- AWS S3 Bucket used to host static file and media files with public permissions.

### Heroku Deployment <a name="herokudeploy"></a>

- Heroku app link added to Allowed Hosts in settings.py file
- pip3 freeze --local > requirements.txt to add installed packages to requirements.txt file
- Procfile (web: gunicorn cinebox.wsgi:application) added to project
- DEBUG set to False
- To deploy this page to Heroku, the following was done:
1. Created repo in GitHub
2. Pushed to GitHub from AWS C9
3. Created [Cinebox App](https://cinebox-movies.herokuapp.com) in Heroku
4. Postgres database added in Heroku Add-Ons section.
5. Required Config Vars added:
    - AWS_ACCESS_KEY_ID
    - AWS_SECRET_ACCESS_KEY
    - DATABASE_URL
    - DISABLE_COLLECTSTATIC (set to 1)
    - SECRET_KEY
    - STRIPE_PUBLISHABLE
    - STRIPE_SECRET
6. App connected to GitHub Repo in Heroku deploy settings.
7. Deploy Branch set to __Master__
8. Enabled Automatic deploys so that all GitHub pushes are auto-deployed to Heroku


<a href="#top">Back to top</a>

### Credits & Acknowledgements <a name="credits"></a>

- Code Institute Video Tutorials for milestone project guidance
- tackoverflow for burger button input.
- W3schools to add main logo image.
- password_reset_email.html added using information and help from my previous mini project.
- All code has been self-written without use of any Git Pull requests (personal or otherwise).
- README image uploads were using links created on GitHub Issues section.
- 3rd party 'haarlem_deco' free font added using helping code from w3schools to add .otf files.
- Tutor Support assistance was used for referencing static files in base.html.
- Big thanks to Michael and rest of Tutor Support team for their patience and assitance in all of my projects.

 
 
 
#### Media <a name="media"></a>

- Apple devices mockup [image](https://user-images.githubusercontent.com/44424348/78756100-55ec6100-79ce-11ea-9969-cd07127840bc.JPG) created using Multi Device Website Mockup Generator. 
- All images are non-watermarked imsages that have been sourced from IMDB and Google Images
- All trailer links are youtube trailer links for the respective movie.

#### Disclaimer <a name="disclaimer"></a>

The content of this app is for educational and milestone project purposes only.

<a href="#top">Back to top</a>