![Share A Plate](/static/images/site-img.png)

# Share A Plate

View the live site [HERE](https://share-a-plate-bm.herokuapp.com/)

View the GitHub repository [Here](https://github.com/brimurphy/share-a-plate)

View README.md [HERE](https://github.com/brimurphy/share-a-plate/blob/master/README.md)

## Table of Contents

- [Automated Testing](#automated-testing)

- [Manual Testing](#manual-testing)

- [Bugs](#bugs)

- [Future Features](#future-features)

- [Wireframes](#wireframes)

- [Technologies Used](#technologies-used)

- [Testing](#testing)



## Automated Testing
 
### Validation Services

  - [HTML](https://validator.w3.org/)
  Placeholder tag not allowed when the input type is time - Placeholder removed
  All other errors are from Jinja not being reconised in the validator

  - [CSS](https://jigsaw.w3.org/css-validator/)
  No Errors Found

  - [JQuery](https://jshint.com/)
  No Errors found

  - [Python](http://pep8online.com/)
  No Errors found 

### Manual Testing

1. Logo:

If you're logged out, go to a page that is not the welcome.
Try to click on the logo and verify that it leads you to the welcome.
If you're logged in, go to a page that is not the users my recipes page.
Try to click on the logo and verify that it leads you to the welcome page.

2. Navigation Bar Pages:

Hover over the pages and verify that their background changes color individualy.
Try to click on them and verify that you are able to go to the page you selected.
Register and login as Admin and verify that "admin controls" is added to your navigation bar.

3. Add Recipe:

Go to the Add Recipe page.
Try to submit recipe leaving one field empty, recipe won't add
Try to enter wrong format into field and warning prompt should appear with red error line
Try to leave the fields empty and verify that a red line appears, indicating that it's a required field
Try to submit the recipe and verify that a confirmation message appears
Go to your my recipes page or the recipes page and verify that your recipe was added

4. Edit Recipe:

Select one of your recipes
Click on the edit button and verify that it opens a form with correct information and recipe
Change the information in any field
Click on the cancel button and you should return to My Recipes page
Click Update and verify that you should return to My Recipes page
Verify that a confirmation message appears and you can see the new changes
Go to your My Recipe page and verify that your recipe was edited

5. Delete Recipe:

If not logged in you can not access edit/delete recipe
Click on the delete button in full recipe view and verify that it opens a new page to confirm deletion
Click on the delete button and verify that a pop up message confirming deletion
Click no and verify that recipe is not deleted
Go to your My Recipe page and verify that your recipe has been deleted.

6. Admin:

Login as Admin.
Click on "Add Diets" and verify a form should load with one input
Delete user, In admin tab click delete user message should be displayed confirming deletion
Delete recipe, In admin tab click delete recipe message should be displayed confirming deletion
Delete diet, In admin tab click delete diet message should be displayed confirming deletion
Edit diet, In admin tab click edit diet message should be displayed confirming update
Try to add a new recipe and verify that the new category appears when selecting the category in the recipe form.

7. Social Media Icons:

Try to click on any social media icon and verify that it opens in a new tab.

8. Test search function:

Search for Ingredients checked by selecting random ingredients
Search by recipe name checked by selecting random recipe names
To test no results message displayed when trying to search by
other fields, I searched by values in the other fields that weren't
a recipe name or a type of ingredient.
Search by numbers will display No recipe/ingredient msg.
To check recipe only returns recipe or recipe with ingredient, I 
searched by single names and ingredients that would only display
one recipe.
To check if multi results would be displayed I searched common
ingredients that would result in more than one recipe.
To search with no characters will display prompt
that field can't be empty

### Bugs

1. Error when trying to add recipe after update to my_recipes
post method.
**Fix** Add username variable to add_recipe function

2. Method not inputing to db on add or edit forms. Name attribute
missing and causing null value to be returned. 
**Fix** Add name attribute to method input

3. When admin updated user, all key value pairs deleted that
were not available to be updated. Added key value pairs to python 
function but this creates a security risk with the user password 
availale to the admin. 
**Fix**After checking mongo.db docs I changed
my update method to update_one. Values passed back to db were strings.
Add bool() method to push correct type to db. 

4. Admin controls getting added to nav more than once.
No checks in function to see if user was a super user,
incorrect jinja expression used in base.html
therefore admin tab created for every new user.
**Fix** Updated jinja for users loop to if statement for
session variable.

5. Session[is_superuser] causing KeyError: 'is_superuser' for new users
when they try log out. Error being caused by session.pop(is_superuser)
after creating new value pair in the register function. 
**Fix** Removed session.pop(is_superuser) to resolve this error.

6. Welcome text breaks out of welcome-content div at 269px.
This will not be fixed it affects the UI of most mobile screen sizes
fixing causes text to look squashed on bigger mobile screens