![Share A Plate](/static/images/site-img.png)

# Share A Plate

View the live site [HERE](https://share-a-plate-bm.herokuapp.com/)

View the GitHub repository [Here](https://github.com/brimurphy/share-a-plate)

View TESTING.md [HERE](https://github.com/brimurphy/share-a-plate/blob/master/TESTING.md)

## About

This website is an online community shared cookbook. A place were food lovers of all levels can interact by sharing their own recipes
and by finding other users recipes. Users can build their own cookbook with their own custom recipes and other users recipes to keep
in one handy location.

## Table of Contents

1. [User Experience](#ux)

- [User Stories](#user-stories)

- [Design](#design)

- [Features](#features)

- [Future Features](#future-features)

- [Wireframes](#wireframes)

- [Technologies Used](#technologies-used)

- [Testing](#testing)

2. [Deployment](#deployment)

- [Steps for Cloning Locally](#steps-for-cloning-locally)

- [Deploying to Heroku](#deploying-to-heroku)

3. [Credits](#credits)

- [Content](#content)

- [Media](#media)

- [Acknowledgements](#acknowledgements)

## User Experience (UX)

### User Stories

  * First Time User Stories

    - As a user, I want to navigate easily through the site
    - As a user, I want to be able to search for recipes using specific keywords or ingredient(s)
    - As a user, I want to register if I do not have an account
    - As a user, I want to be able to log into my account
    - As a user, I want a responsive design on all screen sizes

  * Returning User Stories

    - As a registered user, I want easy access to the members log in page
    - As a registered user, I want to view my recipes and recipes from other members
    - As a registered user, I want to be able to create new recipes
    - As a registered user, I want to be able to edit my recipes and delete them if required
    - As a registered user, I don't want other users able to edit or delete my recipes

  * Admin User Stories

    - As an admin, I want to remove recipes that contain inappropriate language or images
    - As an admin, I want to remove users who repeatedly break the site rules
    - As an admin, I want to be able to create other admins
    - As an admin, I want to add, edit or delete diet categories

## Design 

  ### Colour Scheme

  To choose the colour scheme for the project I read some articles on colour and it's use in food,
  to get a better understanding of the relationship of colours and food. The main information I 
  gathered from these articles was to avoid dark colder colours. That is why I've tried to use bright
  shades of colours, not too bright to affect readability but a shade brighter than I would normally use.

  If you would like to read the articles referred to you can find them below:

  [Palermo Cafe](https://palermocafe.com/colors-make-hungry/)

  [Jenn David Design](https://jenndavid.com/colors-that-influence-food-sales-infographic/)

  [Ashley Anastasia Howell](https://medium.com/@ashley_howell/understanding-colour-psychology-for-restaurants-brands-dbb7ffbcecae)

  ![My Colour Palette](/static/images/color-palette.png)

  I have used [Coolors](https://coolors.co/) to help generate my Colour Palette

  ### Typography

  I have used [Inknut Antiqua](https://fonts.google.com/specimen/Inknut+Antiqua?query=Inknut+Antiqua) for the Headings and Nav links
  and [Rubik](https://fonts.google.com/specimen/Rubik?sidebar.open=true) for the content of the project. I really think these fonts 
  work well together

  ### Wireframes

  I've created the wireframes for this project using Balsamiq Wireframes
  To view the wireframes of this project click [HERE](https://github.com/brimurphy/share-a-plate/tree/master/static/images/wireframes)

  ### Original Sketches

  If you wish to see the original paper sketches of the project click [HERE](https://github.com/brimurphy/share-a-plate/tree/master/static/images/sketches)

## Features

  ### Existing Features

    * Responsive design

      - This website is designed with mobile first design to ensure users experience is seamless on all devices

    * Register form for new users

    * Sign in form for existing users

    * Log Out functionality

    * User page with custom recipes 

    * Easy navigation on all devices

    * Search function to find recipes quickly by entering a recipe name or ingredient

    * User can delete their recipes

    * Defensive programming for deleting recipes

    * Tips displayed on forms to help user fill out correctly

    * Messages displayed when a user Registers for the first time, Logs In, Logs Out, Adds, Edits or deletes a recipe

    * Admin control to delete users, create admins, delete recipes and add, edit or delete diets 

    * Once In the “Recipes” page the user can browse, search and click on the available recipes to open a more detailed card of the recipe

    * The user can view their own recipes by going to their "My Recipes" page

    * User can only edit or delete their own recipes

  ### Future Features

    * Add 'favourite' recipes page, were a collection of users favourite recipes can be found

    * Add option for user to delete their profile

    * Extend search criteria to include more options, like diet and cooking time

    * Add users the option to add recipe images from their files as well as URL's

    * Add a review or comments feature so users can offer advice and give kudos for recipes they enjoyed

    * Limit the amount of recipes are viewable on a page to reduce scrolling by implementing a pagination feature to display 6 recipes at a time

    * Add the option to share recipes to users social media accounts

    * Option for user to flag or report recipes for inappropriate language or images

    * Add functionality to an admin so they can be able to answer any queries a user might have through email

## Technologies Used

  * Languages 

    - [HTML5](https://developer.mozilla.org/en-US/docs/Web/HTML)
    - [CSS3](https://developer.mozilla.org/en-US/docs/Web/CSS)
    - [JavaScript](https://developer.mozilla.org/en-US/docs/Web/JavaScript)
    - [Python](https://www.python.org/)

  * Frontend

    - [Materialize](https://materializecss.com/)
    - [Font Awesome](https://fontawesome.com/v4.7.0/icons/) 
    - [Material Design Icons](https://material.io/resources/icons/?style=baseline)
    - [Favicon](https://favicon.io/)
    - [JQuery](https://jquery.com/download/)
    - [Google Fonts](https://fonts.google.com/)
    
  * Backend

    - [Flask](https://flask.palletsprojects.com/en/1.1.x/)
    - [PyMongo](https://pymongo.readthedocs.io/en/stable/)
    - [Werkzueg](https://werkzeug.palletsprojects.com/en/1.0.x/)
    - [Jinja2](https://jinja.palletsprojects.com/en/2.11.x/)
    - [MongoDB](https://www.mongodb.com/)

  * Other

    - [GitHub](https://github.com/)
    - [Heroku](https://heroku.com/)
    - [Gitpod](https://gitpod.io/)
    - [Balsamiq](https://balsamiq.com/)
    - [RandomKeygen](https://randomkeygen.com/)
    - [Coolors](https://coolors.co/)
    - [Paint 3D](https://www.microsoft.com/en-us/p/paint-3d/9nblggh5fv99?activetab=pivot:overviewtab)
    - [Remove BG](https://www.remove.bg/)
    - [Am I Responsive](http://ami.responsivedesign.is/)
    


## Testing

View TESTING.md [HERE](https://github.com/brimurphy/share-a-plate/blob/master/TESTING.md)
  
## Deployment

#### Requirements

  * [Python3](https://www.python.org/downloads/)
  * [PIP](https://pypi.org/project/pip/) For installing packages in Python
  * [Git](https://git-scm.com/downloads) For version control
  * An IDE of your choice - I have used [gitpod](https://gitpod.io/)
  * [Heroku](https://devcenter.heroku.com/)
  * [MongoDB](https://www.mongodb.com/)

### Steps for Cloning Locally

  1. Go to the project repository [Share A Plate](https://github.com/brimurphy/share-a-plate)

  2. Open Git and select clone from the repository tab. Enter source location [Share A Plate](https://github.com/brimurphy/share-a-plate) and
     the location you wish to store the files and press the clone button

  3. Open your IDE and navigate to the directory where you stored the cloned files

  4. Install requirements from requirements.txt file by entering
     `pip3 install -r requirements.txt` in the terminal

  5. Activate your virtual environment by `py -m venv virtual` into the terminal

  6. Create an environment file `env.py` to store environment variables. Add environment variables as shown:
  ```
os.environ.setdefault("IP", "0.0.0.0")
os.environ.setdefault("PORT", "5000")
os.environ.setdefault("SECRET_KEY", "ADD_YOUR_SECRET_KEY")
os.environ.setdefault("MONGO_URI", "YOUR_MONGODB_URI")
os.environ.setdefault("MONGO_DBNAME", "YOUR_MONGO_DBNAME")```

  * Remember to update your **Secret  Key**, **Database Name** and **Database URI**

  7. Add `env.py` to a `.gitignore` file so sensitive data will not be pushed to GIT

  8. You should now be able to run the program by entering `python3 app.py` into the terminal

### Deploying to Heroku

  1. Login to [Heroku](https://dashboard.heroku.com/)

  2. Go to `Create new App` from `New` tab

  3. Go to settings

  4. Click on `Reveal Config Vars` to add environment variables to match env.py file

  5. Click on `Deploy` tab and set to automatically deploy from GitHub by entering the repository name [Share A Plate](https://github.com/brimurphy/share-a-plate)

  6. Click on connect

  7. In your IDE create the requirements.txt file to contain all dependencies

  ` pip3 freeze --local > requirements.txt`

  8. Create the Procfile

  `echo web: python app.py > Procfile`

  9. Make sure all files have been pushed to GitHub repository 

  10. In Heroku in the `Deploy` tab scroll down to `Manual deploy` and click `Deploy Branch`

  11. When Heroku is finished building the app you can press the `View` button to view your deployed app

## Credits

### Content

I have used [Eat Your Books](https://www.eatyourbooks.com/) welcome message 
*Join a community of cookbook lovers & discover that Eat Your Books is a great way to make better use of your own collection*
As the base of my own welcome message and built on it. 

The original content for my footer is from [My Foodbook](https://myfoodbook.com.au/), again I have altered the content to better tie in with my website

The recipes I have used in my db are from [BBC Good Food](https://www.bbcgoodfood.com/recipes)
  - [Ultimate quiche](https://www.bbcgoodfood.com/recipes/ultimate-quiche-lorraine)
  - [Quick chicken hummus bowl](https://www.bbcgoodfood.com/recipes/quick-chicken-hummus-bowl)
  - [Chilli con carne recipe](https://www.bbcgoodfood.com/recipes/chilli-con-carne-recipe)
  - [Vegan sausage rolls](https://www.bbcgoodfood.com/recipes/vegan-sausage-rolls)
  - [Vegan chilli](https://www.bbcgoodfood.com/recipes/vegan-chilli)
  - [Vegan scones](https://www.bbcgoodfood.com/recipes/vegan-scones)
  - [Coconut & kale fish curry](https://www.bbcgoodfood.com/recipes/coconut-kale-fish-curry)

### Media 

The sites logo is a design by [Jaylyn Breaux](https://www.behance.net/JBDesignWorks) and can be found on [Behance](https://www.behance.net/gallery/67910949/Share-A-Plate-App-Icon-Designs).
I have edited the colours to link in with my colour pallette using [Paint 3D](https://www.microsoft.com/en-us/p/paint-3d/9nblggh5fv99?activetab=pivot:overviewtab)

The hero-image I found on [https://www.pnas.org/content/116/37/18152](https://www.pnas.org/content/116/37/18152) and downloaded it from the Download figure button.
The creater of the image is by Olga Klochanko and this picture and more of her work can be found at [Shutterstock](https://www.shutterstock.com/g/klochanko)

The 'Plate clipart broken' image used on the 404.html page can be found on [Web Stock Review](https://webstockreview.net/pict/getfirst)

### Acknowledgements

For information to help implement :first-of-type selector and :first-child I read this article on [CSS-Tricks](https://css-tricks.com/almanac/selectors/f/first-of-type/#:~:text=The%20%3Afirst%2Dof%2Dtype,with%20parent%20and%20sibling%20content.)
The article is by Sara Cope and you can check out more of her articles [here]([Sara Cope](https://css-tricks.com/author/saracope/))

To implement the use of CSS Counter I read [W3 Schools](https://www.w3schools.com/css/css_counters.asp) and [MDN Web Docs](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_Lists_and_Counters/Using_CSS_counters) tutorials and explanation on using the CSS Variable

To create the back button on the full_recipe and 404 pages I followed Niel McEwen jquery events in jquery tutorials in the Interactive Frontend Development module of [Code Institute's](https://codeinstitute.net/full-stack-software-development-diploma/) Full Stack Software Development course
I also used [W3 Schools](https://www.w3schools.com/js/js_window_history.asp) tutorial on these buttons.

For help handling the 404 error in Flask [Geeks for Geeks](https://www.geeksforgeeks.org/python-404-error-handling-in-flask/)

To help with implementing the /admin_page checks to allow admins access to higher rights I have been tutored by *Shane Murphy*
He helped me understand the use of the session variable. His tutoring helped me set the is_superuser check to allow users with admin privaleges access to the admin page
He also helped me with creating the split and strip function to display information correctly when editing a recipe.

To seperate the list for recipes and methods when displaying to the screen I used this method I found on [Kite](https://www.kite.com/python/answers/how-to-make-a-list-into-a-comma-separated-string-in-python)

To tutor *Tim Nelson* for his Mini Project `Task Manager` tutorial and *Matt Rudge* for his mini Project `Thorin & Company` which I followed to ensure the setup and functionality worked correctly

Thanks to my mentor *Jonathan Munz* for putting up with me and pushing me to be better

Thanks to my family and friends for their help testing and pointing out my typos