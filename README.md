# Iron Fitness

Iron Fitness is a site that provides men's fitness clothing at a competitive price. Users can browse different styles and see a variety of different sizes in each product. Users have the option to buy items quickly through adding their chosen items to their basket and proceeding to the checkout where they pay for the item online. Users can also save items to a wishlist if they want to browse the store and potentially buy them at another time. The site is user friendly and has some of the best styles on the market which will appeal to the target market of young adult men. The link to the site can be found at [Iron Fitness](https://iron-fitness1.herokuapp.com/)

![Welcome Image](https://github.com/sams4566/iron-fitness/blob/main/media/readme/welcome-image.jpg)

## E-commerce Business Model

![Business Model](https://github.com/sams4566/iron-fitness/blob/main/media/readme/business-model.jpg)

__B2C__ - The customer's will primarily be young adult men who are looking for clothes to work out in. These customers usually make the choice to buy on their own and are impulse buyers.

- Features to add: 
  - Login/logout
  - List of orders made by the user

- Potential Database (image below):
  - User

__Products__ - The customers will buy base-layers, hoodies & jackets, joggers, shorts, tank-tops & stringers and t-shirts & tops.

- Features:
  - List of items
  - Filter results
  - Similar items
  - Wishlist

- Potential Databases (image below):
  - Category
  - Item
  - Rating
  - Review
  - Wishlist

__Single Payment__ - Customers will pay online using a credit or debit card. The single payment method works for businesses that sell products or one-time services, making this ideal for 'Iron Fitness'.

- Features:
  - Easy payment system
  - Basket for items

- Potential Databases (image below):
  - Basket
  - Orders

Potential Databases:
![Potential Database](https://github.com/sams4566/iron-fitness/blob/main/media/readme/potential-databases.jpg)

## User stories

### Iterations
I have listed my user stories in five iterations within the projects tab in this repository so that it is easy to see where they fit in my project. I have added the tags 'Must Have', 'Should Have' and 'Could Have' to each of the user stories to understand which is a higher priority.

- [Authentication Iteration](https://github.com/sams4566/iron-fitness/projects/1)
- [Items Iteration](https://github.com/sams4566/iron-fitness/projects/2)
- [Basket & Wishlist Iteration](https://github.com/sams4566/iron-fitness/projects/3)
- [Checkout Iteration](https://github.com/sams4566/iron-fitness/projects/4)
- [Administration Iteration](https://github.com/sams4566/iron-fitness/projects/5)

### Story points
- Below is a diagram that shows the user stories for the Items Iteration and breaks down the number of story points allocated to each:

![Story Points](https://github.com/sams4566/iron-fitness/blob/main/media/readme/story-points.jpg)

## Data Model
### Schema
  - The below database diagram shows the breakdown of my database which helped me to work out the layout of the site and how to structure my python and javascript functions.
  - For the local database I used 'sqlite3' and for the production database I used 'Postgres' on Heroku.
  - Having the Items model as the centre of the project allowed the flow to be intuitive and helpful for UX.
  - The basket is also similar to a model except that the items in it are deleted automatically at the end of the session.

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
  - Images are stored in the repository for the localhost and on Amazon S3 when deployed on Heroku.

## Features
- __Header and Footer__
  - Both the header and footer are styled to allow users to easily navigate the site and are stuck at the top and bottom of each page.
  - The header forms a dropdown menu at lower screen sizes to stop the options from being bunched up.
  - The footer has a link to the companies Facebook page and privacy policy as it is important that users have easy access to both these links.
  - The header and footer are the same in all pages as they are part of the base.html file.

![Header and Footer](https://github.com/sams4566/iron-fitness/blob/main/media/readme/header-footer.jpg)

- __Authentication__
  - Users will be able to sign-up, sign-in and sign-out using the below screens.
  - Admins are the only users who are able to add and edit products alongside viewing all of the options in the Django Admin Panel.
  - If users aren't logged in they won't be able to add products to a basket or wishlist alongside leaving a rating or review on a product.
  - I used the built in django.allauth package to implement these functions.

![Authentication](https://github.com/sams4566/iron-fitness/blob/main/media/readme/authentication.jpg)

- __Home page__
  - The home page quickly lets the user know that the page allows users to buy clothing.
  - The newsletter sign-up is on the front page so that it is one of the first things a user thinks about when they enter the page. Having easy access to signing up will increase the number of emails retrieved for marketing.
  - The large 'View clothing' button organically leads users on to seeing the products available.

![Home page](https://github.com/sams4566/iron-fitness/blob/main/media/readme/home.jpg)

- __List of products pages__
  - The list of products page lays out the list of products in an organic fashion with the number of products per line reducing on lower screen sizes.
  - Depending on the option chosen by the user in the clothing dropdown menu the products and title displayed will be filtered.

![All products](https://github.com/sams4566/iron-fitness/blob/main/media/readme/all-products.jpg)

- __Product Info page__
  - The product info page displays all of the key product information in an effective layout that allows the user to quickly read the key information.
  - The user has the option of giving the product a rating if they are logged in by clicking one of the stars alongside leaving a review at the bottom of the page.
  - The user can also add the item with their chosen size to their wishlist or basket.
  - If the user is an Admin they can edit and add products to the system.
  - The list of similar products helps guide the user to other products to increase their interaction with the site.

![Product Info 1](https://github.com/sams4566/iron-fitness/blob/main/media/readme/product-info1.jpg)
---
![Product Info 2](https://github.com/sams4566/iron-fitness/blob/main/media/readme/product-info2.jpg)

- __Add and Edit Products__
  - An Admin has the ability to edit and add products to the site to keep the site up to date.
  - When an Admin tries to edit a product, the information that has previously been entered is prepopulated.
  - A default image is also set in place if a picture isn't added to a product.

![Edit Product](https://github.com/sams4566/iron-fitness/blob/main/media/readme/edit-product.jpg)

- __Wishlist__
  - The user can add items to a wishlist if they don't want to make a decision about paying for the product straight away. 
  - Items can be deleted from the wishlist and their sizes can be edited.
  - Users can move items to their basket at any point and an error message appears if the item is already in their basket.

![Wishlist](https://github.com/sams4566/iron-fitness/blob/main/media/readme/wishlist.jpg)

- __Basket__
  - Users can quickly see the total cost of the items in their basket when they first enter their basket.
  - If there are more than 2 items in the basket a 'More Items' button appears. This prevents the page from being to cramped.
  - Items sizes can be edited and deleted from the basket if the customer changes their mind. 

![Basket](https://github.com/sams4566/iron-fitness/blob/main/media/readme/basket.jpg)

- __Checkout__
  - The checkout form is a generic online shopping form that users will likely be familiar with.
  - Users can double check the total cost and size of each item before filling out the form.
  - If the user enters card details that are declined an error message appears to let them know the issue. The form details also aren't deleted meaning the user can quickly change their card details and pay for their items.
  - A loading screen appears while their card details are being checked to stop the user from exiting the screen before the payment is complete.

![Checkout](https://github.com/sams4566/iron-fitness/blob/main/media/readme/checkout.jpg)

- __Order Confirmation__
  - Once the payment has been completed users are directed to an order confirmation page that displays the key information for their order.
  - The 'Your payment was successful' message also clears up any ambiguity regarding whether the payment went through.
  - A 'View Orders' button directs the user to all the orders they have made.

![Order Confirmation](https://github.com/sams4566/iron-fitness/blob/main/media/readme/order-confirmation.jpg)

- __List of Orders__
  - Users can see a list of their orders on this page and can click into each one to see its specific details.

![List of Orders](https://github.com/sams4566/iron-fitness/blob/main/media/readme/orders.jpg)

- __Django Admin Panel__
  - The Django Admin Panel allows site managers to add, edit and delete orders, users, products, categories, ratings and reviews.

![Admin](https://github.com/sams4566/iron-fitness/blob/main/media/readme/admin.jpg)

### Future features

- Add additional filtering of products such as filtering by price, recently added and alphabetically.
- Add a search bar so that users can find specific items.
- Allow only users who have bought items to give items reviews and ratings.
- Add a quantity option so users can buy more than one of the same product at a time.
- Produce a breakdown table for users of how many of the star ratings were one star, two star etc.
- Have the first products a customer see be items on sale.

## Marketing
- I created a Facebook page to help generate business for the site and to spread the word (Pictures below).
- Using organic social media will be a key way in developing the business. I aim to have a presence on other social media sites such as Twitter, Instagram and LinkedIn as these are the main social media channels young adult men would use.
- Using paid social media will also be a key target as focussing on advertising to users who have already visited the site will increase revenue. This can cost a significant amount but long term will produce good results.
- Email marketing will be a key part in increasing website traffic as using sites like MailChimp to collect emails can be relatively inexpensive. The newsletter sign-up is the first stage of retrieving emails.
- Using paid adverts such as Google ads will not initially be a priority due to the cost but will be in the future.

  - [Facebook 1](https://github.com/sams4566/iron-fitness/blob/main/media/readme/facebook1.jpg)
  - [Facebook 2](https://github.com/sams4566/iron-fitness/blob/main/media/readme/facebook2.jpg)
  - [Facebook 3](https://github.com/sams4566/iron-fitness/blob/main/media/readme/facebook3.jpg)
  - [MailChimp](https://github.com/sams4566/iron-fitness/blob/main/media/readme/mailchimp.jpg)

## Technologies used

### Languages
  - **HTML** - I used html to create the content and main layout of each page
  - **CSS** - CSS was used to style the html elements and make the site more appealing to users. It was also used to allow the website to respond to different screen sizes.
  - **JavaScript** - I used JavaScript to enhance some of the front end functionality.
  - **Python** - I used python as the main back end language. It was used to write all of the different functions that occur when requested by the user.

### Extensions
  - **Django** - The site was built using the Django full-stack framework where I used many of the built in shortcuts and variables to create the websites backend. Below are the django extensions used:
    - **django-allauth** - used to confirm authentication with users on the site
    - **django-crispy-forms** - used to format the layout of forms
    - **django-countries** - to provide a list of countries in the checkout form
    - **django-storages** - used to connect to Amazon S3 for storing media and static files.
    - **coverage** - used to find out how much of the back end code I had automatically tested
  - **Stripe** - Stripe was the API used to confirm payments
  - **Amazon S3** - Amazon S3 was used to store all the media and static files to be used when the site is deployed on Heroku.
  - **Bootstraps** - I used bootstraps to allow the site to be structured and built quickly. 
  - **jQuery** - jQuery was chosen to allow the javascript code to be implemented easily. 
  - **Postgres** - I used Postgres as the database for the Heroku deployed website as it is well integrated with Heroku.

## Testing

### Bugs

#### Bug 1
  - The following error was showing when I tried to click on the product info page for any of the items in the 'Base layer' category: `ValueError at /items/5/ - The 'image' attribute has no file associated with it.` The reason for the issue was that an item without a picture was added to base layers and the 'Related Items' section of the item info page didn't have the {% if not product.image %} tags.

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

The coverage report for how much of the code in the items app I've covered with tests is below:

![Coverage](https://github.com/sams4566/iron-fitness/blob/main/media/readme/coverage.jpg)

### Manuel Testing
I tested the site on several occasions throughout its development to make sure all the apps and urls were working correctly. I tested the site on several different browsers such as Google Chrome, Safari and Mozilla Firefox and between a width of 320px to 2000px the site is easily readable on all devices.

#### Check user logged out tests
- On the navbar, the wishlist is not visible. PASS
- Under account section of the navbar, there is not an option to 'Add Item'. PASS
- When the basket is clicked a message directing the user to login to add items to their basket appears. PASS
- On the user info page, adding a rating by clicking one of the stars doesn't change the rating total. PASS
- On the user info page, there is no option to leave a review. PASS
- On the user info page, there is no option to add an item to your wishlist or basket. PASS
- On the user info page, there is no option to edit or delete an item. PASS

#### Checkout page tests
- The checkout page displays all of the items added to the basket. PASS
- The total cost correctly adds all the items in the basket together. PASS
- Clicking the 'Change Basket' button returns the user to the basket page. PASS
- If parts of the checkout form that have an asterisk next to it aren't filled out an error appears. PASS
- A loading circle appears when I have filled out the form correctly and pressed submit. PASS
- An error message under the card payment box appears in red if the card was declined. PASS
- The user is directed to an order confirmation page when the payment is confirmed correct. PASS
- An order is still created when a user exits the payment page before the loading circle has disappeared. PASS

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

- **Authentication** - I used Django's AllAuth package to ensure users have to login to make edits to the site. Throughout my code I also made sure that users can only access their own orders and details. If the user is an admin they have access to edit all parts of the site including deleting users if necessary.

- **Debug** - When the site is in production on Heroku debug is set to `False` ensuring the user doesn't get information about why certain urls aren't working.

- **Environment Variables** - I stored private information in environment variables in both gitpod for when accessing the database locally and in the 'Config Vars' Section in Heroku for when the site is deployed on Heroku. This ensured that any information that could cause the website to be hacked is hidden.

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

![Accessibility](https://github.com/sams4566/iron-fitness/blob/main/media/readme/accessibility.jpg)

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
  - To retrieve the stripe STRIPE_PUBLIC_KEY and STRIPE_SECRET_KEY, when you first login to stripe if you click on the 'Developers' tab and then click on the 'API Key' tab you will find both of them.
  - To set up a webhook, first click on the 'Webhooks' tab in the 'Developers' tab
  - Click on 'Add Endpoint' and add your 'home page url' + '/checkout/webhook' similar to https://8000-ich0igsc.ws-eu25.gitpod.io/checkout/webhook/
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
  - Click on 'Policy generator' under the Bucket Policy Tab and add in the ARN + `/*` (which looks similar to `arn:aws:s3:::your-bucket-name/*`) to the generated policies 'Resource' section. Then add the generated policy to the 'Bucket Policy Editor'.
  - Now navigate to the AWS app 'IAM' and create a 'Group' making sure you add in your existing S3 Bucket details.
  - Once you have done this, create a 'New Policy' and 'New User' and add them to your 'Group'.
  - After this, go back to the config variables in the Heroku app and delete the 'DISABLE_COLLECTSTATIC' variable.
  - Deploy again to heroku by entering `git push heroku main` in your terminal and you should be fully set up.

## Credits

### Content/Tutorials
  - [The Django Documentation](https://docs.djangoproject.com/en/4.0/)
  - Bootstrap Themes - [Shop Homepage](https://startbootstrap.com/template/shop-homepage) and [Shop Item](https://startbootstrap.com/template/shop-item)
  - [Stripe Documentation](https://stripe.com/docs)
  - [Amazon S3 Documentation](https://docs.aws.amazon.com/s3/index.html)

### Media
  - [Gymshark](https://uk.gymshark.com/) - for product images and information.
  - [Home page background photo](https://www.bbc.co.uk/news/business-45246999)
  - [Deadlift Photo](https://mirafit.co.uk/blog/types-of-deadlifts/)
  - [No image available photo](https://www.trendsetter.com/xtr541g74-d.html)

