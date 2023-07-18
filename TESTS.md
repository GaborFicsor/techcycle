# TechCycle -- TESTS.md

[Back to README.md]()

[GitHub repository of this project]()

[Deployed website on Heroku]()

<hr>

## CONTENTS

* [AUTOMATED TESTING](#automated-testing)
  * [W3C Markup Validator](#w3c-markup-validator)
  * [W3C CSS Validator](#w3c-css-validator)
  * [JSHint JavaScript Validator](#jshint-validator)
  * [CI Python Linter](#code-institutes-python-linter)
  * [Lighthouse Extension](#accessibility)

* [MANUAL TESTING](#manual-testing)
  * [Testing User Stories](#testing-user-stories)
  * [Full Testing](#full-testing)
  * [Testing Responsiveness](#testing-responsiveness)
  * [Manual Testing of the features](#manual-testing-of-the-features)
  * [Navbar Responsiveness](#navbar-responsiveness)
  * [Navbar as Visitor](#navbar-as-visitor)
  * [Navbar as User](#navbar-as-logged-in-user)
  * [Navbar as Admin](#navbar-as-admin)
  * [Home page responsiveness](#home-page-responsiveness)
  * [Home page as Visitor](#home-page-as-visitor)
  * [Home page as User](#home-page-as-logged-in-user-and-superuser)
  * [Footer](#footer)
  * [Recipe Filter responsiveness](#recipe-filter-responsiveness)
  * [Recipe Filter elements](#recipe-filter-elements)
  * [+add your own hyperlink](#add-your-own-hyperlink)
  * [Recipe cards' responsiveness](#recipe-cards-responsiveness)
  * [Recipe cards elements](#recipe-cards-elements)
  * [Pagination's responsiveness](#paginations-responsiveness)
  * [Pagination elements](#pagination-elements)
  * [Recipe Detail Page's responsiveness](#recipe-detail-pages-responsiveness)
  * [Recipe Detail Page elements](#recipe-detail-page-elements)
  * [Comment section responsiveness](#comments-section-responsiveness)
  * [Comment section elements](#comment-section-elements)
  * [My Stuff Page's responsiveness](#my-stuff-pages-responsiveness)
  * [My Stuff Page's elements](#my-stuff-page-elements)
     * [My Stuff Page with entries](#if-there-are-entries-in-the-my-stuff-my-recipes-and-my-saved-recipes-tables)
  * [Authorization Pages testing](#authorization-pages-testing)
     * [Register page](#register-page)
     * [Login page](#login-page)
     * [Logout page](#logout-page)
  * [Error 404 Page](#error-404-page)
  * [Forms](#forms)
     * [Recipe Form and Recipe editing form](#recipe-form-and-recipe-editing-form)
     * [Comment Form](#comment-form)
     * [Deletion page](#deletion-page)
  * [Alert Messages](#alert-messages)
  * [Admin Panel](#admin-panel)

* [BUGS](#bugs)
  * [Solved Bugs](#solved-bugs)

---

## AUTOMATED TESTING

For automated testing the following external validators were used:
* [W3C Markup Validation](https://validator.w3.org/)
* [W3C Jigsaw](https://jigsaw.w3.org/css-validator/)
* [JSHint](https://jshint.com/)
* [CI Python Linter](https://pep8ci.herokuapp.com/)

###  W3C Markup Validator

<hr>

The deployed project's address was passed for checking, and the result returned with no errors or warnings

![image of the w3c markup validator's result]()

### W3C CSS Validator

<hr>

CSS validation was done by direct input and the result returned with no errors or warnings

![image of the w3c css validator's result]()

### JSHint Validator

<hr>

JSHint Validator was used to validate JavaScript code written in jQuery framework

 * Bootstrap variable is defined within the project and the function is working as expected

![image of jshint javascript validator's result]()

### Code Institute's Python Linter

<hr>

* Validating Python code was carried out by manually pasting the code from each Python file manually written for this project
* No errors were returned 

<details>
  <summary>filters.py linter result</summary>

![image of filters's python linter result](static/images/filters_linter.png)

</details>

<details>
  <summary>forms.py linter result</summary>

![image of forms's python linter result](static/images/forms_linter.png)

</details>

<details>
  <summary>urls.py linter result</summary>

![image of urls's python linter result](static/images/urls_linter.png)

</details>

<details>
  <summary>models.py linter result</summary>

![image of models's python linter result](static/images/models_linter.png)

</details>

<details>
  <summary>views.py linter result</summary>

![image of views's python linter result](static/images/views_linter.png)

</details>

<details>
  <summary>settings.py linter result</summary>

![image of settings's python linter result](static/images/settings_linter.png)

</details>

<details>
  <summary>app.py linter result</summary>

![image of app's python linter result](static/images/app_linter.png)

</details>

<details>
  <summary>admin.py linter result</summary>

![image of admin's python linter result](static/images/admin_linter.png)

</details>

## Accessibility

<hr>

* With keeping accessibility in mind, I provided aria-label texts to hyperlinks and buttons. Also, an alt-description for each image is present throughout the website.

* I tried using colours that are visually appealing while also maintaining a good contrast so that every text is easily readable

* The current page the user is viewing is reflected in the navigation bar by highlighting

![image of the lighthouse extension's report](static/images/ligthhouse_report.png)

## MANUAL TESTING

### Testing User Stories

<hr>

`First Time Visitors`

| Goals | How are they achieved? |
| :--- | :--- |
| I want to have an immediate understanding of the website's purpose | Steezy Spatula is a recipe sharing website. Upon arriving at the landing page the first thing the user sees is the logo with a slogan that says 'Cooking made less overwhelming'. There is also a short description of how someone can make sure this website is the right place for them. Further down the bottom of the page, there is also a short description about who this project is dedicated to, so I think the website has a clear message.
| I want the site to be responsive on the device I am using | The overall design and the logo were developed with responsiveness in mind. |
| I want the site to be easy to navigate. | Buttons are presented throughout the website with simple and clear labels that tell the user what they can expect after clicking them. The current page viewed is also reflected in the navigation bar with highlighting  |

`Registered Users`

|  Goals | How are they achieved? |
| :--- | :--- |
| I want to be able to register on the website to gain access to the full experience provided by the application. | Users can navigate to the page where they can register easily from the home page in 2 ways. There is a green call to action button in the header section of the landing page, and there is also a Register tab on the navigation tab which is present throughout every other page on the website if the user is not logged in. If a user wants to register to the website they need to fill out the register form, they have to choose a name and a password. The password has to be entered twice in 2 different fields for security reasons. Users can register with their email however, at this stage, it is optional and not required to gain access to the website's full features.  |
| I want to be able to create and share my recipe | Registered users can share their recipes and upload them to the database after filling out the recipe form. This form can be found in multiple places throughout the website's pages. The easiest way to do this is to navigate to the 'Recipes' tab in the navigation bar, where they are directed to the recipes page where all recipes are listed. Here they can find a hyperlink to the form that says '+add your own'. Users can also find this form after navigating to the 'My Stuff' tab where they are presented with 2 empty sections. On the left-hand side the first section that reads 'my recipes+' will hold all the recipes the current user has submitted. the '+' sign is a hyperlink to the recipe form. Furthermore, if the section is empty, meaning there are no entries made by the user yet, a sentence will tell the user that it "Looks like you haven't added anything just yet! Share your recipes with us here". The word 'here' is also a hyperlink to the recipe form. |
| I want to have the ability to edit the recipes I have created if needed. | Registered users can edit their own recipes at any time, with the use of an editing form, which is a prepopulated form with the recipe's information. Users can edit any field of their recipe and submit their changes. The editing form can be reached from the 'My Stuff' tab's 'my recipes+' section after a recipe has been created. The editing form can also be reached after navigating to the recipe's detailed page. In both places, a clickable pencil icon tells the users that editing is possible. |
| I want to have the ability to delete the recipes I have created if needed. | Registered users can delete their own recipes. To achieve this, a trash-can icon is placed next to the pencil icon for every recipe the user has created. Clicking the trash-can icon will take the user to a page where they need to confirm their intentions to delete the recipe. |
| I want to have the ability to view other users' shared recipes. | Visitors and also registered users can view any recipe's detailed page under the 'Recipes' tab, where each recipe is presented with a clickable card that takes the user to the recipe's detailed page. |
| I want to have the ability to save and 'unsave' the recipes I like, to access them faster and easier anytime. | Registered users can save a recipe to populate a list under the 'My Stuff' tab's 'my saved recipes'. This list is easily accessible and will hold every recipe that the user decides to save. Saving and 'unsaving' a recipe can be done by clicking a flag icon on a recipe's detailed page. 'Unsaving' can also be done in the 'my saved recipes' table after any recipe has been saved and displayed there. |
| I want to have the ability to engage in conversations regarding a recipe. | Registered users can comment under any recipe's comment section with the use of a comment form. Users can also edit and delete their comments with the pencil icon and trash-can icon respectively |
| I want to be able to view my recipes in one place to manage them faster and easier. | As mentioned above, registered users are provided with the 'My Stuff' page that gives them easy and convenient access to a list of their own and saved recipes. |
| I want to be reinforced by the actions I undertake during my time on the website. | Registered users are alerted after every action performed on the website, including authorization. |
| I want to search and filter recipes to cater for my own needs. | Visitors and also registered users can search recipes with keywords, or filter by difficulty, type and vegan recipes. These filters can also be combined to achieve the best result possible. |

### Testing responsiveness

<hr>

 * Responsiveness of the page was tested manually using Google Chrome developer tools
   * The website is confirmed to be responsive on every screen size without any distortion
   * Images do not stretch or distort in smaller screen sizes
   * Texts remain readable on every screen size


### Manual Testing of the features  

<hr>

<br>

#### Navbar responsiveness

<hr>

 * consistent throughout every page
 * smaller screen sizes will result in a hamburger dropdown menu of navbar tabs
 * currently viewed page is reflected by highlighting 

<br>

#### Navbar as Visitor

|  Element | Expected outcome | Testing performed | Pass |
| :--- | :--- | :--- | :--- |
| Title | indicate link | hover | Pass|
| Title | take the visitor to the landing page | click | Pass |
| Home tab | indicate link | hover | Pass |
| Home tab | take the visitor to the landing page | click | Pass |
| Recipes tab | indicate link | hover | Pass |
| Recipes tab | take the visitor to the Recipes page | click |  Pass |
| Register tab | indicate link | hover | Pass |
| Register tab | take the visitor to the Register form | click | Pass |
| Login tab | indicate link | hover | Pass |
| Login tab | take the visitor to the Register form | click | Pass |

<br>

#### Navbar as Logged-in User

|  Element | Expected outcome | Testing performed | Pass |
| :--- | :--- | :--- | :--- |
| Title | indicate link | hover | Pass |
| Title | take the visitor to the landing page | click |  Pass |
| Home tab | indicate link | hover | Pass |
| Home tab | take the visitor to the landing page | click | Pass |
| Recipes tab | indicate link | hover | Pass |
| Recipes tab | take the visitor to the Recipes page | click | Pass |
| My Stuff tab | indicate link | hover | Pass |
| My Stuff tab | take the visitor to the My Stuff form | click | Pass |
| Logout tab | indicate link | hover | Pass |
| Logout tab | take the visitor to the Logout page | click | Pass |

<br>

#### Navbar as Admin

|  Element | Expected outcome | Testing performed | Pass |
| :--- | :--- | :--- | :--- |
| title | indicate link | hover | Pass |
| title | take the visitor to the landing page | click | Pass |
| Home tab | indicate link | hover | Pass |
| Home tab | take the visitor to the landing page | click | Pass |
| Recipes tab | indicate link | hover | Pass |
| Recipes tab | take the visitor to the Recipes page | click | Pass |
| My Stuff tab | indicate link | hover | Pass |
| My Stuff tab | take the visitor to the My Stuff form | click | Pass |
| Logout tab | indicate link | hover | Pass |
| Logout tab | take the visitor to the Logout page | click | Pass |
| Admin tab | indicate link | hover | Pass |
| Admin tab | take the Admin to the django admin panel  | click | Pass |

<br>

#### Home page responsiveness

<hr>

 * is responsive on every screen size
 * logo changes to accomodate available space
 * slogan disappears on smaller screen sizes
 * description disappears on smaller screen sizes
 * call-to action disappears on smaller screen sizes

<br>

#### Home page as Visitor

|  Element | Expected outcome | Testing performed | Pass |
| :--- | :--- | :--- | :--- |
| Register button | indicate link | hover | Pass |
| Register button | take the Visitor to the Register form | click | Pass |

<br>

#### Home page as Logged in User and Superuser

|  Element | Expected outcome | Testing performed | Pass |
| :--- | :--- | :--- | :--- |
| Register button | not visible after login | login | Pass |

<br>

#### Footer 

|  Element | Expected outcome | Testing performed | Pass |
| :--- | :--- | :--- | :--- |
| LinkedIn icon | indicate link | hover | Pass |
| LinkedIn icon | open my LinkedIn page in a new tab | click | Pass |
| Instagram icon | indicate link | hover | Pass |
| Instagram icon | open my Instagram page in a new tab | click | Pass |
| GitHub icon | indicate link | hover | Pass |
| GitHub icon | open my GitHub page in a new tab | click | Pass |

<br>

#### Recipe Filter responsiveness

<hr>

 * is responsive on every screen size
 * each field displays on every screen size
 * the form is available for both Visitors and Users

<br>

#### Recipe Filter elements

| Element | Expected outcome | Testing performed | Pass |
| :--- | :--- | :--- | :--- |
| 'Recipe name contains' field | textfield | input text | Pass |
| 'Difficulty' field | dropdown menu | click | Pass |
| 'Type' field | dropdown menu | click | Pass |
| 'Vegan' field | dropdown menu | click | Pass |
| Search button | apply filter | click | Pass |

 * when using the filter form, more than one filter can be applied at once
 * applying the filter will display only the relevant recipes
 * if there are no results, the user is informed

<br>

#### add your own hyperlink

 * only visible to Logged in Users

| Element | Expected outcome | Testing performed | Pass |
| :--- | :--- | :--- | :--- |
| +add your own link | indicate link | hover | Pass |
| +add your own link | take the user to the recipe creation form | click | Pass |

<br>

#### Recipe cards' responsiveness

<hr>

 * Cards stay responsive on every screen size
 * Images do not stretch or distort
 * Maximum 9 cards are displayed per page
 * Paginate if there are more than 9 cards
 * Cards are stretched links, meaning the user can click anywhere on the card to use it as a link
 * Featured images are displayed if the User has uploaded one
 * Placeholder images are displayed if the User did not add an optional image
 * Cooking time is displayed dynamically on every recipe card
 * A dynamic progress bar is displayed with changing color and label based on the recipe's difficulty
 * If a recipe is vegan, a green leaf is displayed at the top left corner of the card

<br>

#### Recipe cards' elements

| Element | Expected outcome | Testing performed | Pass |
| :--- | :--- | :--- | :--- |
| Recipe Card | indicate link | hover | Pass |
| Recipe Card | take the user to the recipe's detailed page | click | Pass |

<br>

#### Pagination's responsiveness

<hr>

 * Displays when there are more than 9 recipes
 * Responsive on every screen size
 * 'first' button not visible on smallest screen sizes
 * 'last' button not visible on smallest screen sizes
 * 'first' button only visible after the user moved to the next page
 * 'previous' button only visible after the user moved to the next page
 * 'next' button only visible if there are remaining pages
 * 'last' button only visible if the user is not on the last page

<br>

#### Pagination elements

 * if the User has filtered the recipe list, the pagination will work accordingly

<hr>

| Element | Expected outcome | Testing performed | Pass |
| :--- | :--- | :--- | :--- |
| first | indicate function | hover | Pass |
| first | take user to the first page of the results | click | Pass |
| first | keep results when filtered | click | Pass |
| previous | indicate function | hover | Pass |
| previous | take user to the previous page of the results | click | Pass |
| previous | keep results when filtered | click | Pass |
| next | indicate function | hover | Pass |
| next | take user to the next page of the results | click | Pass |
| next | keep results when filtered | click | Pass |
| last | indicate function | hover | Pass |
| last | take user to the last page of the results | click | Pass |
| last | keep results when filtered | click | Pass |

<br>

#### Recipe Detail Page's responsiveness

<hr>

 * Is responsive on every screen size
 * No element is hidden on smaller screen sizes
 * Pencil icon only visible for recipe author
 * Trash-can icon only visible for recipe author
 * Save icon only visible for logged in Users
 * Save icon changes upon click
 * Green leaf next to the recipe's name indicates if a recipe is vegan

<br>

#### Recipe Detail Page elements

| Element | Expected outcome | Testing performed | Pass |
| :--- | :--- | :--- | :--- |
| Save icon - regular | adds recipe to the saved recipes list | click | Pass |
| Save icon - filled | removes recipe from the saved recipes list | click | Pass |
| Pencil icon | take user to recipe editing form | click | Pass |
| Trash-can icon | take user to recipe deletion page | click | Pass |

<br>

#### Comments section responsiveness

<hr>

 * Comments section only visible for logged in Users
 * Comment form only visible for logged in Users
 * Pencil icon for editing visible if a comment belongs to the current User
 * Trash-can icon for deletion visible if a comment belongs to the current User

<br>

#### Comment section elements

| Element | Expected outcome | Testing performed | Pass |
| :--- | :--- | :--- | :--- |
| Comment text | display | submit input | Pass |
| Pencil icon | take user to comment editing form | click | Pass |
| Trash-can icon | take user to comment deletion page | click | Pass |

<br>

#### My Stuff Page's responsiveness

<hr>

 * Is responsive on every screen size
 * No element is hidden on smaller screen sizes
 * Display current user's name on top
 * Display current user's date joined

<br>

#### My Stuff Page elements

| Element | Expected outcome | Testing performed | Pass |
| :--- | :--- | :--- | :--- |
| + sign | indicate link | hover | Pass |
| + sign | take user to the recipe form | click | Pass |
| 'here' | indicate link | hover | Pass |
| 'here' | take user to the recipe form | click | Pass |
| 'recipe' | indicate link | hover | Pass |
| 'recipe' | take user to the recipes paeg | click | Pass |

<br>

#### If there are entries in the my stuff my recipes and my saved recipes tables

| Element | Expected outcome | Testing performed | Pass |
| :--- | :--- | :--- | :--- |
| Recipe-title | indicate link | hover | Pass |
| Recipe-title | take user to the corresponding recipe's detailed page | click | Pass |
| Pencil icon | take user to recipe editing form | click | Pass |
| Trash-can icon | take user to recipe deletion page | click | Pass |
| Unsave icon | take the user to the corresponding recipe's detailed page | click | Pass |
| Unsave icon | remove corresponding recipe from the my saved recipes table | click | Pass |

<br>

### Authorization Pages testing

#### Register page

| Element | Expected outcome | Testing performed | Pass |
| :--- | :--- | :--- | :--- |
| Username field | indicate textfield | hover | Pass |
| Username field | validate input | input | Pass |
| E-mail field | indicate textfield | input | Pass |
| E-mail field | validate input | input | Pass |
| Password field | indicate textfield | input | Pass |
| Password field | validate input | input | Pass |
| Password field | hide characters | input | Pass |
| Password (again) field | validate input | input | Pass |
| Password (again) field | hide characters | input | Pass |
| Signup button | indicate function | hover | Pass |
| Signup button | submit form | click | Pass |
| Signup button | create user instance | click | Pass |
| Signup button | log in new user | click | Pass |
| 'here' | indicate link | hover | Pass |
| 'here' | take user to login page | click | Pass |

<br>

#### Login Page

| Element | Expected outcome | Testing performed | Pass |
| :--- | :--- | :--- | :--- |
| Username field | indicate textfield | hover | Pass |
| Username field | validate input | input | Pass |
| Password field | indicate textfield | input | Pass |
| Password field | validate input | input | Pass |
| Password field | hide characters | input | Pass |
| Sign in button | indicate function | hover | Pass |
| Sign in button | submit form | click | Pass |
| Sign in button | log in user | click | Pass |
| 'sign up' | indicate link | hover | Pass |
| 'sign up' | take user to the register page | click | Pass |
| Remember me | indicate checkbox | hover | Pass |
| Remember me | auto login returning user | reload page | Pass |

<br>

#### Logout Page

| Element | Expected outcome | Testing performed | Pass |
| :--- | :--- | :--- | :--- |
| Sign out button | indicate function | hover | Pass |
| Sign out button | log out current user | click | Pass |
| Sign out button | take user back to landing page | click | Pass |
| Back to recipes button | indicate function | hover | Pass |
| Back to recipes button | take user back to recipes page | click | Pass |
| Back to recipes button | user stays logged in | click | Pass |

<br>

#### Error 404 Page

 * Is responsive on every screen size
 * Inform the user about the error

| Element | Expected outcome | Testing performed | Pass |
| :--- | :--- | :--- | :--- |
| Error404 page | load if entered url does not exist | input wrong url | Pass |
| Back to recipes button | indicate function | hover | Pass |
| Back to recipes button | take user back to recipes page | click | Pass |

<br>


### Forms 

#### Recipe form and Recipe editing form

| Element | Expected outcome | Testing performed | Pass |
| :--- | :--- | :--- | :--- |
| Element | Expected outcome | Testing performed | Pass |
| Recipe Name field | indicate textfield | hover | Pass |
| Recipe Name field | validate input | input | Pass |
| Recipe Name field | raise alert if object exists with the same name | input name of an existing recipe | Pass |
| Recipe Name field | raise alert if not given | no input | Pass |
| Recipe Type field | indicate dropdown menu | click | Pass |
| Recipe Type field | alert if not given | none selected | Pass |
| Ingredients textarea | validate input | input | Pass |
| Ingredients textarea | raise alert if not given | no input | Pass |
| Ingredients textarea | raise alert if too long | input over 1500 characters | Pass |
| Method textarea | validate input | input | Pass |
| Method textarea | raise alert if not given | no input | Pass |
| Method textarea | raise alert if too long | input over 4000 characters | Pass |
| Preparation Time field | indicate dropdown menu | click | Pass |
| Preparation Time field | validate input | select | Pass |
| Preparation Time field | alert if not given | none selected | Pass |
| Cooking Time field | indicate dropdown menu | click | Pass |
| Cooking Time field | validate input | select | Pass |
| Cooking Time field | alert if not given | none selected | Pass |
| Serving Size field | indicate integerfield | click | Pass |
| Serving Size field | validate input | input | Pass |
| Serving Size field | alert if input is negative | input negative numbers | Pass |
| Serving Size field | raise alert if input is 0 | input 0 | Pass |
| Serving Size field | raise alert if input is over 99 | input 100 | Pass |
| Calories Per Serving field | indicate integerfield | click | Pass |
| Calories Per Serving field | validate input | input | Pass |
| Calories Per Serving field | alert if input is negative | input negative numbers | Pass |
| Calories Per Serving field | raise alert if input is under 50 | input 49 | Pass |
| Calories Per Serving field | raise alert if input is over 5000 | input 5001 | Pass |
| Difficulty field | indicate dropdown menu | click | Pass |
| Difficulty field | validate input | select | Pass |
| Difficulty field | alert if not given | none selected | Pass |
| Image button | indicate function | click | Pass |
| Image button | allow user to upload own image | click | Pass |
| Submit button | indicate function | click | Pass |
| Submit button | validate form | click | Pass |
| Submit button | submit recipe | click | Pass |
| Submit button | take user to recipes page | click | Pass |
| Cancel button | indicate function | click | Pass |
| Cancel button | take user back to recipes page  | click | Pass |
| Cancel button | does not submit form | click | Pass |

<br>

#### Comment form

| Element | Expected outcome | Testing performed | Pass |
| :--- | :--- | :--- | :--- |
| Comment textarea | validate input | input | Pass |
| Comment textarea | raise alert if not given | no input | Pass |
| Comment textarea | raise alert if too long | input over 300 characters | Pass |
| Submit button | indicate function | click | Pass |
| Submit button | validate form | click | Pass |
| Submit button | submit comment | click | Pass |
| Submit button | take user back to the same page with comment submitted | click | Pass |

#### Comment editing form

| Element | Expected outcome | Testing performed | Pass |
| :--- | :--- | :--- | :--- |
| Comment textarea | validate input | input | Pass |
| Comment textarea | raise alert if not given | no input | Pass |
| Comment textarea | raise alert if too long | input over 300 characters | Pass |
| Submit button | indicate function | click | Pass |
| Submit button | validate form | click | Pass |
| Submit button | submit comment | click | Pass |
| Submit button | take user back to the same page with comment submitted | click | Pass |
| Cancel button | indicate function | click | Pass |
| Cancel button | take user back to recipes page  | click | Pass |
| Cancel button | does not submit form | click | Pass |

#### Deletion Page

| Element | Expected outcome | Testing performed | Pass |
| :--- | :--- | :--- | :--- |
| Delete button | indicate function | click | Pass |
| Delete button | delete object from database | click | Pass |
| Delete button | take user back to recipes page | click | Pass |
| Cancel button | indicate function | click | Pass |
| Cancel button | take user back to recipes page | click | Pass |
| Cancel button | does not confirm deletion | click | Pass |

<br>

#### Alert messages

| Element | Expected outcome | Testing performed | Pass |
| :--- | :--- | :--- | :--- |
| When | action | expected message | Pass |
| Successful Login | login / register | Successfully signed in as `username` | Pass |
| Successful Logout | logout | 'You have signed out!' | Pass |
| Successful Recipe form | add recipe | 'Your recipe has been created successfully!' | Pass |
| Successful Recipe edit form | edit recipe | 'Your recipe has been updated successfully!' | Pass |
| Successful Recipe deletion | delete recipe | 'Recipe has been deleteted successfully!' | Pass |
| Successful Comment form | add comment | 'Your comment has been added successfully!' | Pass |
| Successful Comment edit form | edit comment | 'Your comment has been updated successfully!' | Pass |
| Successful Comment deletion | delete comment | 'Your comment has been deleted succefully' | Pass |
| Successful Save | save recipe | `recipe_name` has been added to your saved recipes! | Pass |
| Successful Unsave | unsave recipe | `recipe_name` has been removed from your saved recipes! | Pass |

<br>

#### Admin Panel

| Capability | Available |
| :--- | :--- |
| Create User | Yes |
| Edit User| Yes |
| Look up a Recipe | Yes |
| Create Recipe | Yes |
| Edit Recipe | Yes |
| Delete Recipe | Yes |
| Select more recipes at once | Yes |
| Delete more recipes at once | Yes |
| Search comment | Yes |
| Add comment | Yes |
| Edit comment | Yes |
| Select more comments at once | Yes |
| Delete more comments at once | Yes |

<br>

## Bugs

### Solved

<hr>

* Model relation During early development 
   * I had issues with my models, when I was trying to connect my Recipe model with a many-to-many relationship to a model called Allergens. My lack of understanding of how a many-to-many relationship should work ended me up breaking my models beyond repair. Not even deleting the model from the models.py helped. I had to contact Code Institute Tutor Support where Jason helped me out a lot by giving instructions on how to reset my database.

* Rendering form field in template
   * At a later stage in development, I was trying to render the filter form in my recipe template. At this stage, it had 3 fields to filter by, of which one was a TextInput field to look up recipes. I wanted to render every field individually to be able to style them easier, rather than using crispy forms, but my text field would not want to render. When I tried to render {{ form.recipe_name|as_crispy_field }} I got an error stating that the field that I am trying to pass is either non-existent or invalid. I had to contact Code Institute Tutor Support where Joshua pointed out that I am using the icontains lookup type the wrong way. Adding lookup_expr='icontains' to the variable inside the RecipeFilter Class solved this problem and the field was rendering as expected. 

* Pagination bug
   * during manual testing I found that after filtering the recipe list I was able to look through the paginated views in my recipes template, by viewing the next pages, however, when I tried to click on the previous page the filtered list was not working properly and every recipe got listed again without filtering. Replacing the correct url inside the first and previous page-links solved this problem

<hr>

### Note 
 
 * I would like to mention the following problem within one of my template files. The problem is located in the recipes.html template at line 100. Here I am using a bootstrap progress bar, which I tried turning into a dynamic progress-bar by setting it's inline style as seen in the official [documentation](https://getbootstrap.com/docs/4.0/components/progress/) . I am aware of this being a bad practice in coding, and I am not planning to style my elements this way. However, CSS files do not have access to django template variables, so I could not set the dynamic style from within my CSS file. In my model the difficulty field of the recipe model's key and value pairs for difficulty is the following: 20 : 'Easy', 40 : 'Moderate', 60 : ', 80 : 'Challenging. The reason for this is that I found a way to work with these numbers as django template variables. ```{{ recipe.difficulty }}%``` will result in ```20%```,```40%```,```60%``` or ```80%```, depending on the recipe's difficulty level. Despite the problem that is present, my code is working as I expected. I just wanted to notify the assessor that I am fully aware of this problem, and I hope it's not something that would result in a failed attempt at the project submission.
![image of a problem](static/images/at_rule_selector.png)

Back to [README.md](https://github.com/GaborFicsor/steezy-spatula/blob/main/README.md)

Back to [top](#top)