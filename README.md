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

![Schema](https://github.com/sams4566/iron-fitness/blob/main/media/readme/schema.jpg)

### Site layout
- __Wireframe__
  - I researched lots of the different bootstraps themes and looked at many clothing sites such as ASOS and Gymshark to help work out how the site should look.
  - I subsequently created the below wireframe to further solidify my thoughts.

![Wireframe](https://github.com/sams4566/iron-fitness/blob/main/media/readme/wireframe.jpg)

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
  - The header forms a dropdown menu at lower screen sizes to allow users to stop the options from being bunched up.
  - The footer has a link to the companies Facebook page and their privacy policy as it is important that users have easy access to both these links.
  - The header and footer are the same in all pages as they are part of the base.html file.

![Header and Footer](http)

- __Authentication__
  - Users will be able to sign-up, sign-in and sign-out using the below screens.
  - Admins are the only users who are able to add and edit products alongside viewing all of the options in the Django Admin Panel.
  - If users aren't logged in they won't be able to add products to a basket or wishlist alongside leaving a rating or review of a product.
  - I used the built in django.allauth package to impliment these functions.

![Authentication](http)

- __Home page__
  - The home page quickly lets the user know that the page allows users to buy clothing.
  - The newsletter sign-up is on the front page so that it is one of the first things a user thinks about when they enter the page. Having easy access to signing up will increase the number of emails retrieved for marketing.
  - The large view clothing button organicly leads users on to seeing the products available.

![Home page](http)

- __List of products pages__
  - The list of products page lays out the list of products in an organic fashion with the number of products per line reducing on lower screen sizes.
  - Depending on the option choosen by the user in the clothing dropdown menu the products and title displayed will be filtered.

![List of products pages](http)

- __Product Info page__
  - The product info page displays all of the key product information in an effective layout that allows the user to quickly read the key information.
  - The user has the option of giving the product a rating if they are logged by clicking one of the stars alongside leaving a review at the bottom of the page.
  - The user can also add the item with their choosen size to their wishlist or basket.
  - If the user is an Admin they can edit and add products to the system.
  - The list of similar products helps guide the user to other products to increase their interaction with the site.

![Product Info page](http)

- __Add and Edit Products__
  - An Admin has the ability to edit and add products to the site to keep the site up to date.
  - When a user tries to edit a product the information that has previously been entered is prepopulated.
  - A default image is also set in place if a picture isn't added to a product.

![Add and Edit Products](http)

- __Wishlist__
  - The user can add items to a wishlist if they don't want to make a decision about paying for the product straight away. 
  - Items be deleted from the wishlist and their sizes can be edited.
  - User can move items to there basket at any point and an error message appears if the item is already in their basket.

![Wishlist](http)

- __Basket__
  - Users can quickly see the total cost of the items in their basket when they first enter the basket.
  - If there are more than 2 items in the basket a 'More Items' button appears. This prevents the page from being to cramped.
  - Items sizes can be edited and deleted from the basket if the customer changes their mind. 

![Basket](http)

- __Checkout__
  - The checkout form is a generic form that users will be familiar with when paying for products on other sites.
  - User can double check the total cost and size of each item before filling out the form.
  - If the user enters card details that are declined an error message appears to let them know the issue. The user details also aren't deleted meaning they can quickly change their card details and pay for their items.
  - A loading screen appears while their card details are being checked to stop the user from exiting the screen before the payment is complete.

![Checkout](http)

- __Order Confirmation__
  - Once the payment has been completed users are directed to an order confirmation page that displays the key information for their order.
  - The 'Your payment was successful' message also clears up any ambiguaty regarding whether the payment went through.
  - A 'View Orders' button directs the user to all the orders they have made.

![Order Confirmation](http)

- __List of Orders__
  - User can see a list of their order on this page and can click into each to see each orders specific details.

![List of Orders](http)

- __Django Admin Panel__
  - The Django Admin Panel allows site managers to add, edit and delete orders, users, products, categories, ratings and reviews.

![Admin](http)

### Future features

- Add filters for products categories such as filtering by price, recently added and alphabetically.
- Add a search bar so that users can find specific items.
- Allow only users who have bought items to give items reviews and ratings.
- Add a quantity option so user can buy more than one of the same product at a time.
- Produce a breakdown table for users of how many of the star ratings were one star, two star etc.
- Have the home page products be items on sale.

## Marketing



## Technologies used

### Languages
  - **HTML** - I used html to create the content and main layout of each page
  - **CSS** - CSS was used to style the html elements and make the site more appealing to users. It was also used to allow the website to respond to different screen sizes.
  - **JavaScript** - I used JavaScript to enhance some of the front end functionality.
  - **Python** - I used python as the main back end language. It was used to write all of the different functions that occur when requested by the user.

### Extentions
  - **Django** - The site was built using the Django full-stack framework where I used many of the built in shortcuts and variables to create the websites backend. Below are the django extensions used:
    - django-allauth - used to confirm authentication with users on the site
    - django-crispy-forms - used to format the layout of forms
    - django-countries - to provide a list of countries in the checkout form
    - django-storages - used to connect to Amazon S3 for storing media and static files.
    - coverage - used to find out how much of the back end code I had automatically tested
  - **Stripe** - Stripe was the API used to confirm payments
  - **Amazon S3** - Amazon S3 was used to store all the media and static files to be used when the site is deployed on Heroku.
  - **Bootstraps** - I used bootstraps to allow the site to be structured and built quickly. 
  - **jQuery** - jQuery was chosen to allow the javascript code to be implemented easily. 
  - Postgres - I used Postgres as the database for the Heroku deployed website as it is well integrated with Heroku.

## Testing

### Bugs

#### Bug 1
  - The following error was showing when I tried to click on the item info page for any of the items in the 'Base layer' category: `ValueError at /items/5/ - The 'image' attribute has no file associated with it.` The reason for the issue was that an item without a picture was added to base layers and the 'Related Items' section of the item info page didn't have the {% if not product.image %} tags.

#### Bug 2
  - Two of the automated tests I created stopped working after I added the review and rating models. I needed to login the user on both tests to fix the issue as the item_info redirect view required this.

#### Bug 3
 - Users that weren’t super users were able to add and edit items by typing in the correct url. I stopped this by adding `if request.user.is_superuser:` to the start of both the add_item and edit_item functions

### Automated Testing

The site was tested using the built-in django 'TestCase' library in the items/tests.py file. I ran 8 tests to test the sites basic functionality including testing:
  - Information was successfully entered into the items/models.py data models.
  - Form data couldn't be left empty
  - Items could be added, edited and deleted

To run the tests you can type: `python3 manage.py test`

The coverage report for how much of the code I've covered with tests is below:

![Coverage](https://github.com/sams4566/iron-fitness/blob/main/media/readme/coverage.jpg)

### Manuel Testing
I tested the site on several occations throughout its development to make sure all the apps and urls were working correctly. I tested the site on several different browsers such as Google Chrome, Safari and Mozilla Firefox and between a width of 320px to 2000px the site is easily readable on all devices.

#### Check user logged out
- On the navbar, the wishlist is not visible. PASS
- Under account section of the navbar, there is not an option to 'Add Item'
- When the basket is clicked a message directing the user to login to add items to their basket appears. PASS
- On the user info page, adding a rating by clicking one of the stars doesn't change the rating total. PASS
- On the user info page, there is no option to leave a review. PASS
- On the user info page, there is no option to add an item to your wishlist or basket. PASS
- On the user info page, there is no option to edit or delete an item along. PASS

#### Checkout page test
- The checkout page displays all of the items added to the basket. PASS
- The total cost correctly adds all the items in the basket together. PASS
- Clicking the 'Change Basket' button returns the user to the basket page. PASS
- If parts of the checkout form that have an astrik next to it aren't filled out an error appears. PASS
- A loading circle appears when I have filled out the form correctly and pressed submit. PASS
- An error message under the card payment box appears in red if the card was declined. PASS
- The user is directed to an order confirmation page when the payment is confirmed correct. PASS
- Check if an an order is still created when a user exits the payment page before the loading circle has disappeared. PASS

#### Other Manuel tests
Below are a list of some of the other key tests I completed before submitting the project:
- Check admins could add, edit and delete items on the site.
- Ensure users that aren't admins cannot add, edit and delete items from the system through typing the correct url
- Ensure all of the star rating buttons work correctly and modify the rating total correctly
- Make sure the 'More Items' buttons work correctly and don't prevent the user from seeing all their items.
- Ensure admins have access to the Django Admin Panel and can modify orders correctly with the order totals updating correctly if an item is added or deleted.
- Check error messages appear if there is a duplicate item in the wishlist or basket.

### User Testing
For user testing I asked two friends to do a number of manual tests such as adding a star rating, adding items to their basket and paying for them. This helped me realise the site had to have a 'Change Basket' button on the checkout page to make the site more user friendly.

### Security

- **Authentication** - I used Django's AllAuth package to ensure users have to login to make edits to the site. Throughout my code I also made sure that users can only accesss their own orders and details. If the user is an admin they have access to edit all parts of the site including user order and product information.

- **Debug** - When the site is in production on Heroku debug is set to `False` ensuring the user doesn't get information about why certain urls aren't working.

- **Environment Variables** - I stored private infomation in environment variables in both gitpod for when accessing the database locally and in the 'Config Vars' Section in Heroku for when the site is deployed on Heroku. This ensured that any information that could cause the website to be hacked is hidden.

- **Stripe** - Payments are confirmed securely through stripe which only creates an order when stripe returns that the payment was successful. 

### Validators 

  - HTML
    - No errors were returned when passing through the official [W3C Validator](https://validator.w3.org/)
  - CSS
    - No errors were found when passing through the official [(Jigsaw) Validator](https://jigsaw.w3.org/css-validator/)
  - JavaScript
    - No significant issues were found when passing through the [JSHint JavaScript Validator](https://jigsaw.w3.org/css-validator/)
  - Python
    - No errors were returned when passing through [PEP8 Online](http://pep8online.com/)
  - Accessibility
    - The site was tested through Lighthouse in Google Chrome's developer tools and confirmed a high level of accessibility.

![Accessibility](http)

## Development

### Cloning the repository

  - Navigate to the main page of this repository
  - Click on the 'Code' dropdown menu to the left of the green 'Gitpod' button.
  - Copy the 'HTTPS url' and then open your own workspace.
  - Go to the terminal of your new workspace and type `git clone` + 'HTTPS url'.
  - Move all the files within the 'iron_fitness' folder into your route directory and delete the empty 'iron_fitness' folder
  - To install all of the required modules use `pip3 install -r requirements.txt` in the terminal.
  - Type `python manage.py runserver` to run the site.
  - After this you will have to migrate the changes to integrate them to the new database. Add both of the below statements to the terminal:
    - `python3 manage.py makemigrations`
    - `python3 manage.py migrate`
  - To get access to the Django Admin Panel type the below to your terminal and fill in the details:
    - `python3 manage.py createsuperuser` 
  - Finally, add an `env.py` file similar to the below:
```
  import os
  os.environ['DEVELOPMENT'] = 'True'
  os.environ['SECRET_KEY'] = 'enter_secret_key'
  os.environ['STRIPE_PUBLIC_KEY'] = 'enter_stripe_public_key'
  os.environ['STRIPE_SECRET_KEY'] = 'enter_stripe_secret_key'
  os.environ['STRIPE_WEBHOOK_SECRET'] = 'enter_stripe_webhook_secret'`
```

### Setting up Stripe
  - Login to Stripe and sign up for free.
  - To retrieve the stripe STRIPE_PUBLIC_KEY and STRIPE_SECRET_KEY when you first login to stripe if you click on the 'Developers' tab and then click on the 'API Key' tab you will find both of them.
  - To set up a webhook first, click on the 'Webhooks' tab in the 'Developers' tab
  - Click on 'Add Endpoint' and add your 'home page url' + '/checkout/webhook' similar to https://8000-teal-capybara-nch0igqc.ws-eu25.gitpod.io/checkout/webhook/
  - For the 'Events to send' setting, click 'Select all event'
  - Click 'Add Endpoint
  - Retrieve the 'STRIPE_WEBHOOK_SECRET' by clicking 'Reveal' on the 'Signing section' of the webhook dashboard.

### Deployment to Heroku
  - Create a 'Procfile' with the following in it making sure you add in your application name: `web: gunicorn application_name.wsgi:application`
  - Login to Heroku on their website and create a new app.
  - Click on the 'Resources' tab and add 'Heroku Postgres' to the Add-ons section.
  - Navigate to the 'Settings' tab in Heroku and click on the 'Reveal Config Vars' section and add in the below config vars:

|**Environment Variable**|**Value**                                           |
|------------------------|------------------------------------------------    |
| AWS_ACCESS_KEY_ID      | The access key provided by AWS                     |
| AWS_SECRET_ACCESS_KEY  | The secret key provided by AWS                     |
| DATABASE_URL           | Automatically Generated by Postgres                |
| EMAIL_HOST_PASSWORD    | The password for the address that sends out emails |
| EMAIL_HOST_USER        | The email address for sending out emails           |
| SECRET_KEY             | Django secret key                                  |
| STRIPE_PUBLIC_KEY      | Publishable Key provided by Stripe                 |
| STRIPE_SECRET_KEY      | Secret Key provided by Stripe                      |
| STRIPE_WEBHOOK_SECRET  | Webhook Signing Secret provided by Stripe          |
| USE_AWS                | True                                               |
| DISABLE_COLLECTSTATIC  | 1                                                  |

  - Add in the correct 'ALLOWED_HOSTS' urls to settings.py
  - Now login to Heroku in the terminal of your workspace using `heroku login -i`
  - Type `heroku git:remote -a heroku_app_name` into your terminal then `git push heroku main`. This will deploy your app.
  - To migrate the databases to the Heroku Postgres database enter the below statements to your workspace terminal:
    - `heroku run python3 manage.py makemigrations`
    - `heroku run python3 manage.py migrate`

### Set-up Amazon S3
  - Once you're signed into Amazon AWS, navigate to S3 and create a new bucket.
  - In the permissions tab within your bucket add the below to the CORS configuration:

```
[
  {
    "AllowedHeaders": [
      "Authorization"
    ],
    "AllowedMethods": [
      "GET"
    ],
    "AllowedOrigins": [
      "*"
    ],
    "ExposeHeaders": []
  }
]
```
  - Then click on 'Policy generator' under the Bucket Policy Tab and add in the ARN + '/*' (which looks similar to arn:aws:s3:::your-bucket-name/*) to the generated policies 'Resource' section. Then add the generated policy to the 'Bucket Policy Editor'.
  - Now navigate to the AWS app 'IAM' and create a 'Group' making sure you add in your existing S3 Bucket details.
  - Once you have done this, create a 'New Policy' and 'New User' and add them to your 'Group'.
  - After this, go back to the config variables in the Heroku app and delete the 'DISABLE_COLLECTSTATIC' variable.
  - Deploy again to heroku by entering `git push heroku main` in your terminal and you should be fully set up.

## Credits

### Content/Tutorials
  - [The Django Documentation](https://docs.djangoproject.com/en/4.0/)
  - Bootstrap Themes - [Shop Homepage](https://startbootstrap.com/template/shop-homepage) and [Shop Item](https://startbootstrap.com/template/shop-item)

### Media
  - [Gymshark](https://uk.gymshark.com/) - for items images and information.

