<a href="https://tartanthom.herokuapp.com/"><img src="static/img/brand.png" style="margin: 0; height: 100px; width: 220px;"></a>

# Tartan Thom

A close friend has recently started a new business and needed a website to showcase her products. Tartan Thom produces a selection of original, hand crafted cards, some of which can be personalised to the recipient and occasion. The product range also extends to cake toppers and bespoke, frameable occasion gifts, providing beautiful and unique keepsakes when something extra special is required!

## Research, Planning and Scope

I worked closely with Nic in the early phase of the project to gather the requirements initially for her website and spent time with her to fully understand the product range and how the business currently operates. She already had a landing page website which directed potential customers to one of her social media channels but needed a much bigger site to showcase her range of products and provide an ordering system allowing customers to purchase directly from her rather than using third party hosting platforms. 

From our discussions, I identified and documented a series of user stories for the project, each of which was assigned a priority within the scope of the overall project, including Must, Should and Could requirements. The Must requirements would be given highest priority for phase one of the implementation, with Should requirements being implemented where timescales and feasibility allowed and Could requirements captured but perhaps not implemented until a later date.

Together we reviewed existing materials which included the Tartan Thom logo and background tartan image, both designed and produced by Nic, and discussed ideas for the design, structure and style options. A catalogue of the existing product images were collated for use on the new site. 

The main sections of content were subdivided into broad categories and formed the basis of the apps identified for development, including but not limited to Products, Profiles, Basket and Checkout. Lucidchart software was used to plan the models for the database, within which the data would be held, and the relationships between each. 

I drafted some initial designs and ideas and then transferred these to Balsamiq Wireframes to showcase the intended structure and functionality of the website. Several colour palettes were generated using Coolors and a selection of Google Fonts were shortlisted for review. 

## UX Design

### User Stories

User stories were developed for the project and written in the format:
“As a <type of user>, I want <some goal> so that <some reason>"

The user stories were grouped by customer type including customer and administrator users. Once all user stories had been drafted, they were reviewed in terms of their priority and assigned a priority of Must, Should or Could depending on their significance in the overall project.

The ‘Must’ requirements were prioritised for development, with ‘Should’ requirements implemented where feasible in the timescales and some ‘Could’ requirements were parked as features to be included for future development of the site.

The full set of user stories can be viewed [here](documentation/TartanThomUserStories.xlsx "Tartan Thom User Stories").

### Wireframes

Wireframes for the project were drafted on the Balsamiq Wireframes application.

The wireframes show the intended structure and design of the various pages to be included in the project on a desktop view. A handful of wireframes were also drafted to show how the responsive design and structure would be implemented on smaller mobile devices, with the stacking of content using Bootstraps container, row and column structure to render appropriate to device width.

The wireframes can be accessed [here](documentation/TartanThom-Wireframes.pdf "Tartan Thom - Wireframes")

## Database Design

The database models were drafted using the online tool Lucidchart. Each model in the database is represented as a table containing all of the fields assigned to that model, along with their field types. The relationships between the database models are presented in the chart in the style of a typical Entity Relationship Model.

The Entity Relationship Model for Tartan Thom can be found [here](documentation/TartanThomERM.pdf "Tartan Thom – Entity Relationship Model")

### Models

Following discussions with the customer regarding the requirements, the database structure was designed by taking all of the individual elements required for the project and determining whether or not there was a requirement to store the data in a database.

An entity relationship model was drafted using an online tool via Lucidchart to map out all of the individual tables required in the database, the type of data they would be holding and the relationship between the different tables using Foreign Key fields.

A full list of the models developed for this project are listed below:

**User**
-	User is a standard User model in Django which captures user data including username, name, email and password fields. Other fields are also available in the User model including permissions and groups however there wasn’t a requirement to capture data for these at this time. 

**Product**
-	The Products model was designed to hold the data relating to each of the Tartan Thom products. This was one of the harder models to define since the products have slight variation between each type. It was agreed though that in order to reduce complexity, a single Product model would be developed that incorporated requirements and attributes for all products in the collection, given the collection is relatively small at this stage. Should the collection be extended significantly in future, it may be necessary to create separate Models to manage the different product types.

**Product Reviews**
-	The Product Reviews model was designed to capture rating and review text for a specified product which can be completed by a registered User upon purchase of a product. The model includes a review_active field to allow the system administrator to control visibility of the review on the Tartan Thom site – the reviews will be active by default upon submit however should any malicious reviews be left, the administrator has the ability to remove where absolutely necessary.

**Order**
-	The Order model captures data relating to an order of products placed by a registered user. A unique order number is generated and the Users name and delivery details are captured. The total fields are calculated from the quantity and price of a product in the OrderItem model and the Order model is updated with these values.

**Order Item**
-	The OrderItem model captures data relating to individual items within an order, including the quantity and item total. The OrderItem model has foreign keys to both Product and Order models.

**Testimonials**
-	The Testimonials model captures testimonial data submitted by a registered user. The model includes a testimonial_active field to allow the system administrator to control visibility of the testimonial on the Tartan Thom site. 

**Bespoke**
-	As many of the products in the range are bespoke items, the site needed a way to capture additional information about the customer / product recipient in order to produce the bespoke items. Similar to the Products model, the Bespoke model could be split into multiple smaller bespoke models capturing information specific to a type of product, however given the small size of the collection, it was decided to keep all model fields optional and to render to the customer only the necessary fields specific to that product type. The bespoke models may be split out in future should the collection grow and there becomes a requirement to do this.

## Features

### Existing Features

**Navigation tabs**
-	The site has a main navigation bar along the top of all pages which gives users immediate access to the Shop, Login, Register and Basket. When users are logged in to the site, the Login and Register navigation links are replaced with a link to their Account which is a dropdown menu and provides further links to My Account or to Logout.
-	A secondary navigation bar has been introduced on the Shop page to allow users to define their search results by one of the defined product types – the options include All Products, Cards, Cake Toppers and Gifts. Clicking on the links filters the products according to the product type selected. 

**Authentication**
-	The Django-allauth package was utilised for the authentication on the project. The allauth package supports multiple authentication schemes including login by username or by e-mail, as well as multiple strategies for account verification. Allauth also has the ability to connect multiple social accounts to a Django user account, which is something I’d like to introduce in the second phase of development.

**Homepage Images**
-	The Tartan Thom homepage displays a preview of products from the collection with button overlays to invite the user to navigate to the Shop. A user can choose to shop all products, or shop by the three distinct types of products if they are looking for something specific. s

**Testimonials**
-	Beneath the products display, a series of testimonials are presented to the user, allowing them to cycle through the active testimonials using the left and right arrow buttons. This quickly highlights to other customer the positive user experiences of Tartan Thom. Testimonials can be submitted by any user of the site but must be made active by the site owner in order to be displayed (see Profile section for further detail).

**Profile**
-	Once a user is logged in to the site, they are able to access the ‘My Account’ link via the Account dropdown nav menu. The My Profile page displays information relating directly to the logged in user including links to:
-	**My Details** – here, users are able to update key information contained in the User model including their First Name, Last Name and Email Address. The user information is displayed and can be updated as necessary. There is also a link to change their password should they wish to do this.
-	**Testimonials** - a link is provided from the profile page to the testimonials page where logged in users can submit a testimonial about their experience of Tartan Thom. The form captures the text for the testimonial as well as a checkbox allowing the user to give permission for their testimonial to be published on the Tartan Thom website. The site owner has access to review the detail from the admin panel and make live should they wish and have appropriate permission.
-	**Order History** - all previous orders are stored in the Order History section within the users profile page. Once logged in, users can view a full list of their order history with Tartan Thom which initially is a summary of information including the order number, date, amount and the name on the order. The order number field is a link which directs the user to an Order Details page revealing full details of the order including itemised product information, images and quantities. From within the Order Details page, a user is given the option beside each of the products to leave a review, which links to the review form (see Reviews below). There is also a link to the Bespoke Form of a product if the product is bespoke.
-	**My Addresses** - see features left to implement
-	**My Payments** - see features left to implement

**Shop**
-	Users can navigate to the Shop via the main navigation link or via the action links inset within the homepage images, choosing all products, or a specific product type. Once on the main Products page, an additional navigation bar is present allowing the user to filter the products on a specific product type. The results will be displayed in rows and columns depending on device size and include the name and price (or sale price) or the product. 
-	The user can click on the product image to navigate to the product details page which provides additional information including a product description and a list of product reviews if available within a tabs section beneath.

**Reviews**
-	To further enhance the user experience, user reviews have been incorporated to help inform other users when selecting a product to purchase. Reviews are displayed on the product page when a user selects a product, within the tabs section underneath the main product content. Users are able to scroll through a series of reviews, displaying star ratings and rating text. Reviews are only able to be submitted by someone who has purchased the selected product, the link to complete a review is available to a user once they have paid for the product, under the Order History section of their Profile page. 

**Modals**
-	**Confirm Delete** - a Bootstrap model has been utilised in order for Users to confirm when they wish to delete an item from their basket. Introducing a two-step process for deleting items from a user’s basket helps to ensure that they don’t do this in error by confirming their intent to delete.

**Footer**

-	**About** - links to about pages in the footer including About Us, Design and Craft, and Philosophy. These pages aim to give the user some background information about Tartan Thom including the design and production process and the ethics that drive Tartan Thom’s brand. 
-	**Contact** - the contact us page renders a contact form enabling users to get in touch with Tartan Thom directly by completing the contact form. Tartan Thom will receive an email with details of the user including their email address, the subject of the email and the main message text of their enquiry. A message will be displayed once submitted, confirming that their enquiry has been submitted. 
-	**Social Media** - users can link to Tartan Thoms social media pages including Facebook, Twitter and Instagram to further enhance their user experience and where they may find additional information about the company including latest products and updates.

**Basket**
-	Tartan Thom utilises sessions to allow the user of the site to store products and quantities in their bag for checkout at a later time, whether or not they are logged in. As products are added to the bag, the user is taken to their bag and the updated total quantity is displayed in a balloon beside the ‘Bag’ nav link. Users can navigate back to the Shopping pages via a link on the bag page.

**Checkout**
-	Checkout functionality has been implemented to allow a logged in user to purchase products from the site. Stripe, an online payment processing API, has been utilised to take payment for orders made on the site. 
-	Tartan Thom retains data on all orders made by a user and displays previous order information in the Order History section of their Account.

### Features left to implement

**Improved filters**
-	Further development of the filters section could be developed to include filtering and sorting on attributes such as price or recently added. It was decided that this functionality was a low priority at this stage as it is a fairly new business with a small range of products, unlike some larger ecommerce stores who have hundreds of products. The likelihood of requiring this extensive filtering is not necessary at this point however is considered as a possible enhancement in future as the business grows. This also includes the need to search for a product so this too may be something to introduce at a later stage. An enhanced filter could be introduced to look at filtering by review rating though this was also deemed suitable as a future enhancement given the low number of products in the range.

**Google Maps**
-	Google Maps functionality was listed as a ‘Could’ requirement on the user stories and so the development of this feature was not prioritised. During the planning phase and after discussions with my customer, it was decided that this feature would be left out due to her current company address being her residential property and issues surrounding her privacy. It has been agreed that this feature may be implemented at some point in the future once the business has moved to a commercial address. 

**Advertising and Marketing**
-	The offer of advertising space to other companies was not considered a priority at this stage of the development process so has been left out at this current time. 

**Social Media Login**
-	Due to time constraints, the implementation of authentication via social media platforms has been postponed however the intention is to introduce this piece of functionality to allow users to login using Facebook. Often with so many other login accounts, users can be reluctant to create another account on a shopping website so allowing authentication via Facebook may help to prevent loss of interest from prospective users.

**Profile**
-	**My Addresses** - the My Addresses section will allow a logged in user to store and update address information linked the their account. The intention being to make the checkout process much quicker by allowing use of stored address information when placing an order.
-	**My Payments** - as above, the My Payments section will allow a logged in user to store and update payment information linked the their account. The intention also being to make the checkout process much quicker by allowing use of stored payment details when purchasing a product. Reviewing all user stories, these requirements were deemed to be low priority and due to time constraints, were not implemented in phase one.

**Products**
-	Further enhancements to the Products model are planned to offer customer a choice of colour options other than what has been designed for the standard product. A colour field has been added to the model with an attribute of blank=False in anticipation but as yet, this product enhancement is not available to customers. The views in the basket will need adapting to incorporate adding the relevant colour and quantity of a product to the shopping bag. This is planned for phase 2. 


### Structure and Flow


### Navigation

Bootstrap has been utilised for the main navigation menu on the site which is responsive, rendering the burger style menu bar on smaller screen sizes. Supplementary navigation has been included on the Products page, providing users with further navigation links to shop by a particular product type.

### Forms

Many of the forms used in the project are Django model forms which allow submission of data directly to the model within the database. I installed a package called Django Crispy Forms which I used to render the majority of forms used within this project. Crispy Forms provides template tags which allow control over the rendering of the form fields in html pages, displaying them neatly to the end user whilst still allowing the Django framework to maintain the same standards, eliminating the need to write custom forms.

### Typography

Google Fonts was used to browse and select the fonts used on the website and two fonts were identified as a requirement for the project. Great Vibes was selected for its close match to the Tartan Thom logo designed by Nic. It is a handwriting style which has been utilised throughout the project, mainly for header content. Open Sans was identified as a perfect pairing to use concurrently with Great Vibes, utilised for the majority of the text content throughout the site, selected for its clarity and readability.

Font sample demonstrating the Great Vibes and Open Sans font pairing:
[here](/documentation/GreatVibes.png “Great Vibes / Open Sans”)

### Colour

**HTML Color Codes** (https://html-color-codes.info/) was used to extract colours used within the existing tartan background 

**Coolors** (https://coolors.co/) was used to generate and experiment with different colour choices and colour combinations. Alongside the neutral grey tones used in the tartan design, I wanted to introduce an accent colour to add a splash of colour to the website yet persisting the natural theme in keeping with Tartan Thom’s eco-friendly philosophy and Desert Sand was chosen for the project.

The final colour selections can be seen below.

**Colour pallet:**
![](/documentation/TartanThomColourPalette.png)

**#F8F9FA - Cultured**

<img src="/documentation/Cultured.png" width="200px" height="100px">

**#E5E5E5 - Platinum**

<img src="/documentation/Platinum.png" width="200px" height="100px">

**#CED6D7 – Light Gray**

<img src="/documentation/LightGray.png" width="200px" height="100px">

**#828285 – Gray Web**

<img src="/documentation/GrayWeb.png" width="200px" height="100px">

**#E6BEAE**

<img src="/documentation/DesertSand.png" width="200px" height="100px">


### Icons

**Font Awesome** has been utilised for the various icons in use throughout the site. Icons have been used for the navigation links including Bag and Shop as well as the boxes on the Profile page under My Account. Font Awesome icons have also been used for the social media icons embedded in the footer including Facebook, Twitter and Instagram which link out to the respective social media pages.

## Technologies Used

-	HTML
-	CSS
-	JQuery
-	Javascript
-	Django Framework
-	Django allauth - https://django-allauth.readthedocs.io/en/latest/overview.html
-	Django Crispy Forms - https://django-crispy-forms.readthedocs.io/en/latest/
-	Stripe
-	Bootstrap – Responsive Grid System, Modal boxes, Forms
-	Google Fonts
-	Font awesome
-	Coolors

## Testing

To test the project I combined two different approaches including the use of Django’s unit tests which use a Python standard library module called unittest and implementing my own user testing framework by drafting test scripts for the various areas of the website which were then conducted on an array of different devices and browsers.

The Django unittest module defines tests using a class-based approach. When running tests, Django searches for all test cases whose name begins with test, builds and runs the tests in the suite – unittest supports test automation including the set-up and teardown of code for tests. Coverage was installed to measure the coverage of unit testing against all lines of code within the project.

The user testing framework was drafted in excel, defining the different areas of the site and the associated actions within that specific app/area. The user-based approach allowed me to test not only that the code worked as expected when performing certain actions, but also that the rendering and visual display of code was appropriate for the type in use to ensure a fully responsive design.

Testing was also conducted throughout the build of the project to ensure that the functionality worked as expected and any issues that cropped up during the build phase were rectified during development. 

### Issues


## Deployment

**GitPod and GitHub**

Code Institute have provided a full workspace template for GitPod which provides extensions and tools for CI students, available in Code Institute’s GitHub repository. Once logged in to GitHub, I created a new repository in my account called tartanthom using the GitPod template and launched GitPod directly from the new repository which replaced the need to initialise a new repository directly in GitPod. 

Code was run locally in GitPod using the command ‘python3 manage.py runserver’

As code was developed in GitPod, changes in the working directory were added regularly to the staging area using the command ‘git add <filename>’ which tells Git to include these updates in the next commit. 

Code was then committed and saved to the local repository using the command ‘git commit -m “commit message here”’ before being pushed to the remote repository in GitHub using the command ‘git push’, transferring the commits from the local to the remote repository.

**SQLite Database**

An SQLite database was provisioned and used during the development and build phase of the project. 

**PostgreSQL Database**

A PostgreSQL database was provisioned in Heroku when the project moved into production. Heroku Postgres is a managed SQL database service provided directly by Heroku. 

**Heroku Deployment**

Deployment to Heroku can be accessed [here](documentation/TartanThom-Deployment.pdf "Tartan Thom - Deployment")


## Credits

### Coding

I adapted the code demonstrated by Brad Traversy for use in my Product Reviews.
https://codepen.io/bradtraversy/pen/GQLRZv

I followed the coding lessons from Code Institute’s full stack frameworks module using this as a foundation and basis on which to build my own ideas for Tartan Thom’s ecommerce website, utilising some of the concepts and code taught throughout the module, in particular the use of Stripe API and checkout functionality.

### Media

**Images** - All images used throughout the site were taken by Tartan Thom’s founder Nicola Thomson.

### Acknowledgements

A huge thank you to my wonderful friend Nicola Thomson for allowing me to take on her website for my final project milestone. It has been an absolute privilege to build this for you and I have thoroughly enjoyed every step of the project design and build phases, albeit a few bumps along the way. I hope this will give her greater visibility in the wider arts and crafts market and be a kick start to a successful business venture. Best of luck!

I’ve had the pleasure of working with my mentor Spencer Barriball, who has been instrumental in his advice and guidance throughout the course, helping me to work through and untangle a few knots along the way and giving me a boost of confidence when all hope was lost. Thank you for your encouragement, perseverance and patience!

Thank you to my family, in particular my parents, who have been incredibly supportive throughout the course and even more so in Covid lockdown whilst trying to juggle work, coursework and home schooling. Thanks for keeping me going through the highs and lows and for the encouragement to get it done, I really couldn’t have achieved this without you.

A final thank you to my gorgeous little boy Alfie, for being patient, kind and understanding towards his Mummy over the last few months and for all the hugs when the going got tough. I promise you my undivided attention from now on, I love you!
