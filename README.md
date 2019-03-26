![IMG_1195](https://user-images.githubusercontent.com/43143675/54995861-b2e1c880-4fbf-11e9-854b-57db2f46ff75.jpg)
## ilive
An online marketplaces site dedicated to provide sellers, buyers and tenants an outstanding experince through an easy-to-use and intuitive functionality. 

## UX
Due to the insufficient supply of housing, we are constantly looking for accomodation and this is not an easy task. For this reason, I decided to create a website to make the property search easier with a focus on accessible information on properties and advertisers alike.  

On ilive the ads are split into properties for sale, rent and share. Additionally, There is a search form on the home page to facilitate the property search according to the user needs. When users enter the name of the city, select the type of property (house, apartment or site) and the motive for the search (buy, rent or share), 
a list of matching properties are displayed together with a string of text on top of the page indicating the number of ads currently advertised with the values entered and selected in the search form.  
Furthermore, users can view all the properties currently being advertised on the home page
and access the full details of the properties by clicking on them. Once the advertised property has been clicked, the user can see multiple images of the property together with the description of same and details such as full address, number of bathrooms, bedrooms, property type, price, building energy rating, facilities and contact details(owner's name, email and phone number).  
Users can contact the advertiser via email by clicking on the link provided or make a phone call by clicking on the number provided as a link.  

To advertise properties, the user must create an account by entering their names, email, phone number and password. Registered users can access their advertised properties on the My Properties section where they can be found listed, and users can edit them and delete them.
When the ad has been edited or deleted the user is redirected to the home page and a message will appear under the navbar confirming the removal or edition. The messages feature is also available when a user registers and logs in. 

## Mockups
* [ilive_tablet_mockups.pdf](https://github.com/Jeanca7/iLive/files/3009348/ilive_tablet_mockups.pdf)
* [ilive_desktop_mockups.pdf](https://github.com/Jeanca7/iLive/files/3009344/ilive_desktop_mockups.pdf)
* [mobile phone screen mockups - ChoppingBoard.pdf](https://github.com/Jeanca7/choppingboard.ie/files/2911748/mobile.phone.screen.mockups.-.ChoppingBoard.pdf)  
* [additional wireframes.pdf](https://github.com/Jeanca7/iLive/files/3009352/additional.wireframes.pdf)

## Code style
I have used standard code style.

## Tech/framework used
<b>Built with</b>
* Flask
* Bootstrap 4
* Python
* JavaScript
* CSS3
* HTML5
* Jinja2
* MongoDB NoSQL database
* Heroku  
* Adobe Comp (To create mockups)  

## Features
Every user can see all the properties being advertised and their content including images and contact details. If a user wants to advertise must register to access the property form. The content on ilive is created by the registered users only.

Specific features are as follows:
1. Authentication system (registration, login and logout) 
2. Form validation
2. Creation of property advertising
3. Edition of property
4. Deletion of property
5. Search form to filter properties (use of regular expressions($regex) and the find method in MongoDB database) 
6. Property description(carousel of images and property features)

## Installation
To run this project you will need to clone this repository and enter the following command in your console.
```
$ sudo pip3 -r install requirements.txt
```
Please note that I used basic Unix in the terminal so the commands may differ from your software operating system.  
Furthermore, You might need to create an account on mLab to store your data as it is a database server for MongoDB; you can find information here: (https://mlab.com/welcome/)  
 
## Deployment
ilive is hosted on Heroku.  
(http://jeansedo-ilive.herokuapp.com/)


## Tests
Testing was executed manually to ensure the website's responsiveness, funcionality and defensiveness work correctly.   

* Responsiveness:
The site was tested on a 23.8" monitor and 13.3" MacBook Air, iphone X and ipad Pro. It was also tested on Firefox, Chrome and Safari.

* Functionality:
To ensure features of the site work effectively and on different operating systems.
    * Registration.
    * Login/logout.
    * Uploading files such as images.
    * Creation of property ads and correctly saved in the database.
    * Edition and deletion of ads from the database.
    * Successful search by using regular expressions together with case insensitivity.
    * Query doccuments from collections by using a logical AND conjuction for the search form. 

* Deffensiveness:
    * Only registered users can login.
    * An unregistered person cannot advertise a property.
    * Only registered users can delete and edit their own properties and not someone else's.

## How to use?
You can register with your email, names and phone number.  
Alternatively, you can use the username:guest@gmail.com and password:guest777  
ilive: (http://jeansedo-ilive.herokuapp.com/)

## Credits
 MongoDB documentation (https://docs.mongodb.com/)  
 Flask doccumentation (http://flask.pocoo.org/docs/1.0/)  
 Appreciation for Flask authentication. Book Flask Web Development, Developing web applications with Python By Miguel Grinberg (Publisher:O'Reilly, 2018)
 
### Media
* Images obtained from Pexels.com and Google.
* Icons from Fontawesome.com
    
