# Iron Fitness

The Iron Fitness is a site that provides men's fitness clothing at a competitive price. User's can browse different styles and see a variety of different sizes in each. User's have the option to buy items quickly through adding their chosen items to their basket and proceeding to the checkout where they pay for the item through an online payment. Users can also save items to a wishlist if they want to browse the store and potentially buy them at another time.

![Welcome Image](http)

## User stories

I have listed my user stories in the following agile tool so that it is easy to see where they fit in my project. I have added tags to them so it is easy to see who they are for and for which part of the site.

[Story Points](https://github.com/sams4566/iron-fitness/projects/1)

### Story points
- Below is a diagram that shows the user stories for the projects timebox and breaks down the number of story points allocated to each:

![Story Points](http)

- User stories were also documented throughout the project using the 'Issues' tab in the github repository. Below is a screenshot of the table used:

![User Stories](http)

## Data Model
### Schema
  - The below database diagram shows the breakdown of my database which helped me to work out the layout of the site and how to structure my python and javascript functions.
  - For the local database I used 'sqlite3' and for the production database I used 'Postgres' on Heroku.
  - Having the Items model as the center of the project allowed the flow to be intuative and helpful for UX.
  - The basket is also similar to a model except that the items in it are delete automatically at the end of the session.

![Schema](https://github.com/sams4566/iron-fitness/tree/main/media/readme/schema.jpg)

### Site layout
- __Wireframe__
  - I researched lots of the different bootstraps themes and looked at many clothing sites such as ASOS and Gymshark to help work out how the site should look.
  - I subsequently created the below wireframe to further solidify my thoughts.

![Wireframe](https://github.com/sams4566/iron-fitness/tree/main/media/readme/wireframe.jpg)

- __Theme__
  - I decided to use the [Shop Homepage](https://startbootstrap.com/template/shop-homepage) theme from Start Bootstraps as it made the navigations of the site easy and was similar to my wireframe.

- __Color Scheme__  
  - I decided to use black, white and grey as the color scheme as they contrast well making it easy for users to see the content.
  - The black navbar and footer reduces the white space and draws the users eyes to the main content.

- __Font__
  - After researching several sites for good font combinations, I found the combination of Oswald and Quattrocento on [Page Cloud](https://www.pagecloud.com/blog/best-google-fonts-pairings). 
  - Oswald was a strong and bold font that I thought would appeal to men and Quattrocento is a thinner font that would look good for large paragraphs.

- __Icons__
  - I used font awesome for some of the icons as they appear as text rather than an image which limits the icon from being altered at different screen sizes.

- __Images__
  - Images are stored in the repository for the localhost and on AWS when deployed on Heroku.

## Features
- __Header and Footer__
  - Both the header and footer are styled to allow users to easily navigate the site and are stuck at the top and bottom of each page.

![Header and Footer](http)

### Future features

## Technologies used

### Languages
  - **HTML** - I used html to create the content and main layout of each page
  - **CSS** - CSS was used to style the html elements and make the site more appealing to users. It was also used to allow the website to respond to different screen sizes.
  - **JavaScript** - I used JavaScript to enhance some of the front end functionality.
  - **Python** - I used python as the main back end language. It was used to write all of the different functions that occur when requested by the user.

### Extentions
  - **Django** - The site was built using the Django full-stack framework where I used many of the built in shortcuts and variables to create the websites backend. Out of the django extentions I used both AllAuth and Coverage. AllAuth was used to confirm authentication with users on the site and Coverage was used to find out how much of the back end code I had automatically tested.
  - **Bootstraps** - I used bootstraps to allow the site to be structured and built quickly. 
  - **jQuery** - jQuery was chosen to allow the javascript code to be implemented easily. 

## Testing

### Bugs

#### Bug 1

#### Bug 2

#### Bug 3

### Automated Testing

The site was tested using the built-in django 'TestCase' library in the items/tests.py file. I ran ##### tests to test the sites basic functionality including testing:
  - Information was successfully entered into the items/models.py data models.
  - Form data couldn't be left empty
  - Items could be added, edited and deleted#########

To run the tests you can type: `python3 manage.py test`

The coverage report for how much of the code I've covered with tests is below:

![Coverage](http)

### Manuel Testing
I tested the site on several occations throughout its development to make sure all the apps and urls were working correctly.

### User Testing

### Security

- **Authentication** - I used Django's AllAuth package to ensure users have to login to make edits to the site.

- **Debug** - When the site is in production on Heroku debug is set to `False` ensuring the user doesn't get information about the certain urls aren't working.

### Validators 

  - HTML
    - [W3C Validator](https://validator.w3.org/)
  - CSS
    - [(Jigsaw) Validator](https://jigsaw.w3.org/css-validator/)
  - JavaScript
    - [JSHint JavaScript Validator](https://jigsaw.w3.org/css-validator/)
  - Python
    - [PEP8 Online](http://pep8online.com/)
  - Accessibility
    - 

![Accessibility](http)

## Development

### Cloning the repository

  - Navigate to the main page of this repository
  - Click on the 'Code dropdown menu to the left of the green 'Gitpod' button.
  - Copy the HTTPS url and then open your own workspace.
  - Go to the terminal of your new workspace and type `git clone` + 'copied url'.
  - To install all of the required modules use `pip3 freeze --local > requirements.txt` in the terminal.
  - Type `python manage.py runserver` to run the site.

### Deployment to Heroku

## Credits

### Content/Tutorials
  - [The Django Documentation](https://docs.djangoproject.com/en/4.0/)
  - Bootstrap Themes - [Shop Homepage](https://startbootstrap.com/template/shop-homepage) and [Shop Item](https://startbootstrap.com/template/shop-item)

### Media
  - [Gymshark](https://uk.gymshark.com/) - for items images and information.

