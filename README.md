![img_0050](https://user-images.githubusercontent.com/43143675/53450907-62556a80-3a15-11e9-8d53-0ad96dc523bd.jpg)
## ilive
An online marketplaces site dedicated to provide sellers, buyers and tenants an outstanding experince through an easy-to-use and intuitive functionality. 

## UX
Due to the insufficient supply of housing, we are constantly looking for accomodation and this is not an easy task. For this reason, I decided to create a website to make the property search easier with a focus on accessible information on properties and advertisers alike.  

On ilive the ads are split into properties for sale, rent and share. Also, users can view all the properties currently being advertised on the home page
and access the full details of the properties by clicking on them. Once the advertised property has been clicked, the user can see multiple images of the property together with the description of same and details such as full address, number of bathrooms, bedrooms, property type, price, building energy rating, facilities and contact details(owner's name, email and phone number).  
Users can contact the advertiser via email by clicking in the link provided or make a phone call by clicking on the number provided as a link.  

To advertise properties, the user must create an account by entering their names, email, phone number and password. Registered users can access their advertised properties on the My Properties section where they can be found listed, and users can edit them and delete them.


## Build status
Travis has been used for building status of continus integration.

[![Build Status](https://travis-ci.org/Jeanca7/choppingboard.ie.svg?branch=master)](https://travis-ci.org/Jeanca7/choppingboard.ie)

## Code style
I have used standard code style.

## Tech/framework used
<b>Built with</b>
* Django
* Bootstrap 4
* jQuery
* Ajax
* Python
* JavaScript
* CSS3
* HTML5
* PostgreSQL database
* Stripe
* Heroku  

* Adobe Comp (To create mockups)
## Features
Everyone can view recipes including their videos and pictures. However, in order to interact with ChoppingBoard and its users, viewers must register.
The content on ChoppingBoard is created by its users only.

Specific features are as follows:
1. Authentication system (registration, login, logout, password change and password reset)
2. Social authentication (register and login using Facebook, Linkedin and Google+ (please notice that Google+ will come to an end in April 2019)) 
3. Custom user profiles (Users can change their profile information including names, email, avatar, background image, etc.)
4. Generated images tumbnails (using sorl-thumbnail)
5. Pagination (using ajax)
5. follower system (using ajax)
6. like system (using ajax)
7. Views 
8. Users can email cooks from their profile. 


## Installation

You might need to create an account on AWS (Amazon  and generate secret keys to access the static files. You can find information here: (https://docs.aws.amazon.com/general/latest/gr/aws-sec-cred-types.html#access-keys-and-secret-access-keys)   
Additionally, you need to install an SQL databse system to store information. ChoppingBoard uses PostgreSQL.  
ChoppingBoard utilises Stripe for payments, you can create an account here: (https://stripe.com/ie)

To run this project you will need to clone this repository and enter the following command in your console.
```
$ sudo pip3 -r install requirements.txt
```

## Deployment
ShoppingBoard is hosted on Heroku and static files are stored on AWS.  
(https://jeancasedo-choppingboard.herokuapp.com/)

## Mockups
* [desktop:laptop screen mockups - ChoppingBoard.pdf](https://github.com/Jeanca7/choppingboard.ie/files/2911743/desktop.laptop.screen.mockups.-.ChoppingBoard.pdf)  
* [ipad screen mockups - ChoppingBoard.pdf](https://github.com/Jeanca7/choppingboard.ie/files/2911746/ipad.screen.mockups.-.ChoppingBoard.pdf)  
* [mobile phone screen mockups - ChoppingBoard.pdf](https://github.com/Jeanca7/choppingboard.ie/files/2911748/mobile.phone.screen.mockups.-.ChoppingBoard.pdf)

## Tests
Testing was executed manually to ensure the website's responsiveness, funcionality and defensiveness work correnctly.   

* Responsiveness:
The site was tested on a 23.8" monitor and 13.3" MacBook Air, iphone X and ipad Pro. It was also tested on Firefox, Chrome and Safari.

* Functionality:
To ensure features of the site work effectively and on different operating systems.
    * registration
    * Login/logout
    * social authentication(on Facebook, Linkedin and Google+) Social Uthentication works on deployed website only.
    * Uploading files as images and videos.

* Deffensiveness:
    * Only users can login and post a recipe.
    * An unregistered person cannot follow a user.
    * An unregistered person cannot give a like to recipes.
    * Only users can delete and edit their own recipe and not someone else's.
    * Only users can edit their own profile and not someone else's.
    * Users' profiles can only be viewed by other users.

## How to use?
You can register with your email or login with a social media account(Facebook, Linkedin or Google+).  
Alternatively, you can use the username:guest and password:guest777  
ChoppingBoard: (https://jeancasedo-choppingboard.herokuapp.com/)

## Credits
 Django documentation (https://docs.djangoproject.com/en/2.1/)  
 Appreciation for Django authentication. Simple is better than complex (https://simpleisbetterthancomplex.com/)  
 Book Django 2 by Example By Antonio Mele (Publisher:Packt, 2018)

### Media
* Videos were obtained from Pexels.com
* Images obtained from Pexels.com and Google.
* Icons from Fontawesome.com
* Fonts from GoogleFonts.
    
