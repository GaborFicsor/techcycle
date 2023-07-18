# TechCycle -- TESTS.md

[Back to README.md](../techcycle/README.md)

[GitHub repository of this project]()

[Deployed website on Heroku]()

<hr>

## CONTENTS

 * [AUTOMATED TESTING](#automated-testing)
    * [W3C Markup validator](#w3c-markup-validator)
    * [W3C CSS validator](#w3c-css-validator)
    * [Python validator](#python-validator)
    * [Techcycle app](#techcycle-app)
    * [Bag app](#the-bag-app)
    * [Home app](#home-app)
    * [Products app](#products-app)
    * [Checkout app](#checkout-app)
    * [Profiles app](#profiles-app)
    * [Accessibility](#accessibility)

 * [MANUAL TESTING](#manual-testing)
    * [Landing page](#landing-page)
    * [Navigation bar](#navigation-bar-and-dropdown-links)
    * [Product cards](#testing-product-cards)
      * [Laptop](#laptop-card)
      * [Phone](#phone-card)
      * [Smartwatch](#smartwatch-card)
      * [Console](#console-card)
    
    * [Detailed page view](#detailed-page-views-testing)
      * [Laptop](#laptop-detailed-page)
      * [Phone](#phone-detailed-page)
      * [Smartwatch](#smartwatch-detailed-page)
      * [Console](#console-detailed-page)

    * [All products views](#all-products-views-testing)
      * [all Laptops](#all-laptops-views)
      * [all Phones](#all-phones-views)
      * [all Smartwatches](#all-smartwatches-views)
      * [all Consoles](#all-consoles-views)

    * [Placing products in the bag](#placing-products-in-the-bag)
    * [Checkout page testing](#checkout-page-testing)
    * [Checkout success page](#checkout-success-page)
    * [Authorization pages](#authorization-pages)
    * [Profile pages](#profile-page)
    * [Adding products](#adding-products)
      * [Laptop](#laptop)
      * [Phone](#phone)
      * [Smartwatch](#smartwatch)
      * [Console](#console)

    * [Editing views](#editing-views)
      * [Laptop](#laptop-and-inventory-editing)
      * [Phone](#phone-and-inventory-editing)
      * [Smartwatch](#smartwatch-and-inventory-editing)
      * [Console](#console-and-inventory-editing)
---

## AUTOMATED TESTING

For automated testing the following external validators were used:
* [W3C Markup Validation](https://validator.w3.org/)
* [W3C Jigsaw](https://jigsaw.w3.org/css-validator/)
* [CI Python Linter](https://pep8ci.herokuapp.com/)

###  W3C Markup Validator

<hr>

The deployed project's address was passed for checking, and the result returned with no errors or warnings

<details>
  <summary>W3C validator results</summary>

![image of filters's python linter result](/assets/images/w3c_results.png)

</details>

### W3C CSS Validator
<hr>

CSS validation was done by direct input and the result returned with no errors or warnings. The only errors returned here were the same errors present in the Boutique Ado walkthrough project where the mobile to nav header is included as a direct child of a navigation element. The mobile-top-nav header's outermost element is a list item element. The li element is meant to be a list inline item which pushes the icons in the top nav header to the center.

<details>
  <summary>Jigsaw results</summary>

![image of filters's python linter result](/assets/images/jigsaw_result.png)

</details>

### Python validator

* Validating Python code was carried out by manually pasting the code from each Python file manually written for this project
* No errors were returned 

#### Techcycle app
<hr>

<details>
  <summary>settings.py</summary>

![image of filters's python linter result](/assets/images/settings.png)

</details>

<details>
  <summary>urls.py</summary>

![image of filters's python linter result](/assets/images/urls.png)

</details>

<details>
  <summary>wsgi.py</summary>

![image of filters's python linter result](/assets/images/wsgi.png)

</details>

#### The bag app
<hr>
<details>
  <summary>apps.py</summary>

![image of filters's python linter result](/assets/images/bag-app-apps.png)

</details>

<details>
  <summary>bag_tools.py</summary>

![image of filters's python linter result](/assets/images/bag-app-bag_tools.png)

</details>

<details>
  <summary>contexts.py</summary>

![image of filters's python linter result](/assets/images/bag-app-contexts.png)

</details>

<details>
  <summary>urls.py</summary>

![image of filters's python linter result](/assets/images/bag-app-urls.png)

</details>

<details>
  <summary>views.py</summary>

![image of filters's python linter result](/assets/images/bag-app-views.png)

</details>

#### Home app
<hr>
<details>
  <summary>admin.py</summary>

![image of filters's python linter result](/assets/images/home_admin.png)

</details>

<details>
  <summary>apps.py</summary>

![image of filters's python linter result](/assets/images/home_apps.png)

</details>

<details>
  <summary>models.py</summary>

![image of filters's python linter result](/assets/images/home_models.png)

</details>

<details>
  <summary>urls.py</summary>

![image of filters's python linter result](/assets/images/home_urls.png)

</details>

<details>
  <summary>views.py</summary>

![image of filters's python linter result](/assets/images/home_views.png)

</details>

#### Products app
<hr>
<details>
  <summary>apps.py</summary>

![image of filters's python linter result](/assets/images/products_apps.png)

</details>

<details>
  <summary>admin.py</summary>

![image of filters's python linter result](/assets/images/products_admin.png)

</details>

<details>
  <summary>urls.py</summary>

![image of filters's python linter result](/assets/images/products_urls.png)

</details>

<details>
  <summary>forms.py</summary>

![image of filters's python linter result](/assets/images/products_forms.png)

</details>

<details>
  <summary>models.py</summary>

![image of filters's python linter result](/assets/images/products_models.png)

</details>

<details>
  <summary>views.py</summary>

![image of filters's python linter result](/assets/images/products_views.png)

</details>

<details>
  <summary>widgets.py</summary>

![image of filters's python linter result](/assets/images/products_widgets.png)

</details>

#### Checkout app
<hr>

<details>
  <summary>admin.py</summary>

![image of filters's python linter result](/assets/images/checkout_admin.png)

</details>

<details>
  <summary>apps.py</summary>

![image of filters's python linter result](/assets/images/checkout_apps.png)

</details>

<details>
  <summary>forms.py</summary>

![image of filters's python linter result](/assets/images/checkout_forms.png)

</details>

<details>
  <summary>models.py</summary>

![image of filters's python linter result](/assets/images/checkout_models.png)

</details>

<details>
  <summary>signals.py</summary>

![image of filters's python linter result](/assets/images/checkout_signals.png)

</details>

<details>
  <summary>urls.py</summary>

![image of filters's python linter result](/assets/images/checkout_urls.png)

</details>

<details>
  <summary>views.py</summary>

![image of filters's python linter result](/assets/images/checkout_views.png)

</details>

<details>
  <summary>webhook_handler.py</summary>

![image of filters's python linter result](/assets/images/checkout_webhook_handler.png)

</details>

<details>
  <summary>webhooks.py</summary>

![image of filters's python linter result](/assets/images/checkout_webhooks.png)

</details>

#### Profiles app
<hr>

<details>
  <summary>apps.py</summary>

![image of filters's python linter result](/assets/images/profiles_apps.png)

</details>

<details>
  <summary>forms.py</summary>

![image of filters's python linter result](/assets/images/profiles_forms.png)

</details>

<details>
  <summary>models.py</summary>

![image of filters's python linter result](/assets/images/profiles_models.png)

</details>

<details>
  <summary>urls.py</summary>

![image of filters's python linter result](/assets/images/profiles_urls.png)

</details>

<details>
  <summary>views.py</summary>

![image of filters's python linter result](/assets/images/profiles_views.png)

</details>




## Accessibility

<hr>

* With keeping accessibility in mind, I provided aria-label texts to hyperlinks and buttons. Also, an alt-description for each image is present throughout the website.

![image of the lighthouse extension's report](static/images/ligthhouse_report.png)

## MANUAL TESTING


### Landing page

| Element | Excpected outcome | Testing performed | Outcome|
| :--- | :--- | :--- | :--- |
|Navbar title| reload home page | clicked |Pass|
|Search bar| indicate text input | hover |Pass|
|Search button| submit text input|clicked|Pass|
|Profile Icon| toggle drop-down |clicked|Pass|
|Shopping Cart|load cart page|clicked|Pass|
|All Products|load all products page|clicked|Pass|
|Laptops|toggle dropdown|clicked|Pass|
|Phones|toggle dropdown|clicked|Pass|
|Smartwatches|toggle dropdown|clicked|Pass|
|Consoles|toggle dropdown|clicked|Pass|
|Sale|load all products page with items on sale|clicked|Pass|
|Carousel images|slide content|observed|Pass|
|Carousel consoles button| load consoles page | clicked |Pass|
|Carousel sale button| load all products page with items on sale | clicked |Pass|
|Carousel slider|slide content on click|clicked|Pass|
|Featured Laptops|display random laptops |refreshed page|Pass|
|Why choose TechCycle section|display|observed|Pass|
|Accordion|toggle accordion when another one opens |clicked|Pass|
|Small Icons|display|observed|Pass|
|Newsletter|submit form|clicked submit|Pass|
|Facebook link|opens facebook on new page|clicked|Pass|
|Instagram Link|opens instagram on new page|clicked|Pass|
|LinkedIn link|opens linkedin on new page|clicked|Pass|
|Laptops|open laptops page |clicked|Pass|
|Phones|open phones page|clicked|Pass|
|Smartwatches|open smartwatches page|clicked|Pass|
|Consoles|open consoles page|clicked|Pass|
|Inspections|open inspections page|clicked|Pass|
|Sustainability|open sustainability page|clicked|Pass|
|Conditions|opens conditions page|clicked|Pass|
|Policy|opens policy page|clicked|Pass|
|Home|opens home page|clicked|Pass|
|Products|opens all products page|clicked|Pass|
|Cart|opens cart page|clicked|Pass|
|Sale|opens all products page with items on sale|clicked|Pass|
|Stripe Icon|opens official stripe page on a new tab|clicked|Pass|
|Django Icon|opens official django page on a new tab|clicked|Pass|
|AWS Icon|opens official AWS page on a new tab|clicked|Pass|
<hr>
<br>
<br>


### Navigation bar and dropdown links

| Element | Excpected outcome | Testing performed | Outcome|
| :--- | :--- | :--- | :--- |
| Laptops by price | load laptops page with price ascending | clicked | Pass|
| Asus Laptops | load laptops page with asus laptops| clicked | Pass|
| All Laptops | load laptops page | clicked | Pass|
| Phones by price | load phones page with price ascending | clicked | Pass|
| Samsung Phones | load phones page with samsung phones | clicked | Pass|
| iPhones | load phones page with iphones | clicked | Pass|
| All Phones | load phones page | clicked | Pass|
| Smartwatches by price | load smartwatches page with price ascending| clicked | Pass|
| Galaxy Watches | load smartwatches page with samsung watches | clicked | Pass|
| Apple Watch | load smartwawtches page with apple watches | clicked | Pass|
| All Watches | load smartwatches page | clicked | Pass|
| Consoles by Price | load consoles with price ascending | clicked | Pass|
| Nintendo | load consoles page with nintendos | clicked | Pass|
| Playstation | load consoles page with playstations | clicked | Pass|
| Xbox | load consoles page with xbox-es | clicked | Pass|
| All Consoles | load consoles page | clicked | Pass|
<hr>
<br>
<br>

### Testing product cards

#### Laptop card

| Element | Excpected outcome | Testing performed | Outcome|
| :--- | :--- | :--- | :--- |
| Laptop card | display | observed | Pass|
| Laptop card image | render image | observed | Pass|
| Laptop card details | render details | observed | Pass|
| Laptop card price | render price | observed | Pass|
| Laptop card sale indicator| render sale price if item on sale | observed | Pass|
| Laptop card in stock indicator| render in stock if item is not out of stock| observed| Pass|
| Laptop card out of stock indicator| render if out of stock| observed | Pass|
| Laptop card image| turn grey when out of stock| observed| Pass |
| Laptop card image link | load Laptop detailed page| clicked | Pass|
| Laptop card hover effect| cast shadow| hovered mouse| Pass|
<hr>
<br>
<br>

#### Phone card

| Element | Excpected outcome | Testing performed | Outcome|
| :--- | :--- | :--- | :--- |
| Phone card | display | observed | Pass|
| Phone card image | render image | observed | Pass|
| Phone card details | render details | observed | Pass|
| Phone card price | render price | observed | Pass|
| Phone card sale indicator| render sale price if item on sale | observed | Pass|
| Phone card in stock indicator| render in stock if item is not out of stock| observed| Pass|
| Phone card out of stock indicator| render if out of stock| observed | Pass|
| Phone card image| turn grey when out of stock| observed| Pass |
| Phone card image link | load Phone detailed page| clicked | Pass|
| Phone card hover effect| cast shadow| hovered mouse| Pass|
<hr>
<br>
<br>

#### Smartwatch card

| Element | Excpected outcome | Testing performed | Outcome|
| :--- | :--- | :--- | :--- |
| Smartwatch card | display | observed | Pass|
| Smartwatch card image | render image | observed | Pass|
| Smartwatch card details | render details | observed | Pass|
| Smartwatch card price | render price | observed | Pass|
| Smartwatch card sale indicator| render sale price if item on sale | observed | Pass|
| Smartwatch card in stock indicator| render in stock if item is not out of stock| observed| Pass|
| Smartwatch card out of stock indicator| render if out of stock| observed | Pass|
| Smartwatch card image| turn grey when out of stock| observed| Pass |
| Smartwatch card image link | load Smartwatch detailed page| clicked | Pass|
| Smartwatch card hover effect| cast shadow| hovered mouse| Pass|
<hr>
<br>
<br>

#### Console card

| Element | Excpected outcome | Testing performed | Outcome|
| :--- | :--- | :--- | :--- |
| Console card | display | observed | Pass|
| Console card image | render image | observed | Pass|
| Console card details | render details | observed | Pass|
| Console card price | render price | observed | Pass|
| Console card sale indicator| render sale price if item on sale | observed | Pass|
| Console card in stock indicator| render in stock if item is not out of stock| observed| Pass|
| Console card out of stock indicator| render if out of stock| observed | Pass|
| Console card image| turn grey when out of stock| observed| Pass |
| Console card image link | load Console detailed page| clicked | Pass|
| Console card hover effect| cast shadow| hovered mouse| Pass|
<hr>
<br>
<br>

### Detailed page views testing

#### Laptop detailed page

 Element | Excpected outcome | Testing performed | Outcome|
| :--- | :--- | :--- | :--- |
| Laptop name | rendering | observed | Pass |
| in stock indicator | displaying if laptop is not out of stock | observed | Pass |
| This item is out of stock | rendering if item is out of stock | observed | Pass |
| only a few left indicator | displaying if stock count is less than or equal to 2 | observed | Pass |
| List of available conditions | display conditions where stock_count is at least 1 | observed | Pass |
| Laptop image | display | observed | Pass |
| Laptop image | turns grey if laptop is out stock | observed | Pass |
| Laptop price | displaying | observed | Pass |
| Laptop price | displaying lowest available price if all conditions are available | observed | Pass |
| Laptop price | displaying lowest available price if only 2 conditions are available | observed | Pass |
| Laptop price | displaying lowest available price if only 1 condition is available | observed | Pass |
| Laptop price | hidden if out of stock | observed | Pass |
| Laptop out of stock | displays instead of the price if laptop is out of stock | observed | Pass |
| Laptop form quantity input | can adjust quantity | tested with input | Pass |
| Laptop form condition dropdown | displaying available conditions with their prices | observed and selected | Pass |
| Laptop form condition dropdown | if any of the conditions if out of stock it can not be selected | observed | Pass |
| Laptop form condition dropdown | if all conditions are out stock all selectable options are disabled | observed | Pass |
| Laptop form condition dropdown | if all conditions are out of stock display "This item is currently out of stock" | observed | Pass |
| Laptop form condition quantity input | if all conditions are out of stock quantity input is disabled | observed | Pass | 
| Laptop form button | render with the text add to cart if laptop is available | observed | Pass | 
| Laptop form button | disable if out of stock | observed | Pass |
| Laptop form button | add laptop to bag with selected quantity and condition | clicked | Pass |
| Keep shopping button | load all products page | clicked | Pass |
| Laptop specification details | rendering all fields | observed | Pass |
| Laptop features details | rendering all fields | observed | Pass |
| Laptop extras details | rendering all fields | observed | Pass |
<hr>
<br>
<br>

#### Phone detailed page

 Element | Excpected outcome | Testing performed | Outcome|
| :--- | :--- | :--- | :--- |
| Phone name | rendering | observed | Pass |
| in stock indicator | displaying if phone is not out of stock | observed | Pass |
| This item is out of stock | rendering if item is out of stock | observed | Pass |
| only a few left indicator | displaying if stock count is less than or equal to 2 | observed | Pass |
| List of available conditions | display conditions where stock_count is at least 1 | observed | Pass |
| Phone image | display | observed | Pass |
| Phone image | turns grey if phone is out stock | observed | Pass |
| Phone price | displaying | observed | Pass |
| Phone price | displaying lowest available price if all conditions are available | observed | Pass |
| Phone price | displaying lowest available price if only 2 conditions are available | observed | Pass |
| Phone price | displaying lowest available price if only 1 condition is available | observed | Pass |
| Phone price | hidden if out of stock | observed | Pass |
| Phone out of stock | displays instead of the price if phone is out of stock | observed | Pass |
| Phone form quantity input | can adjust quantity | tested with input | Pass |
| Phone form condition dropdown | displaying available conditions with their prices | observed and selected | Pass |
| Phone form condition dropdown | if any of the conditions if out of stock it can not be selected | observed | Pass |
| Phone form condition dropdown | if all conditions are out stock all selectable options are disabled | observed | Pass |
| Phone form condition dropdown | if all conditions are out of stock display "This item is currently out of stock" | observed | Pass |
| Phone form condition quantity input | if all conditions are out of stock quantity input is disabled | observed | Pass | 
| Phone form button | render with the text add to cart if phone is available | observed | Pass | 
| Phone form button | disable if out of stock | observed | Pass |
| Phone form button | add phone to bag with selected quantity and condition | clicked | Pass |
| Keep shopping button | load all products page | clicked | Pass |
<hr>
<br>
<br>

#### Smartwatch detailed page

Element | Excpected outcome | Testing performed | Outcome|
| :--- | :--- | :--- | :--- |
| Smartwatch name | rendering | observed | Pass |
| in stock indicator | displaying if phone is not out of stock | observed | Pass |
| This item is out of stock | rendering if item is out of stock | observed | Pass |
| only a few left indicator | displaying if stock count is less than or equal to 2 | observed | Pass |
| List of available conditions | display conditions where stock_count is at least 1 | observed | Pass |
| Smartwatch image | display | observed | Pass |
| Smartwatch image | turns grey if phone is out stock | observed | Pass |
| Smartwatch price | displaying | observed | Pass |
| Smartwatch price | displaying lowest available price if all conditions are available | observed | Pass |
| Smartwatch price | displaying lowest available price if only 2 conditions are available | observed | Pass |
| Smartwatch price | displaying lowest available price if only 1 condition is available | observed | Pass |
| Smartwatch price | hidden if out of stock | observed | Pass |
| Smartwatch out of stock | displays instead of the price if phone is out of stock | observed | Pass |
| Smartwatch form quantity input | can adjust quantity | tested with input | Pass |
| Smartwatch form condition dropdown | displaying available conditions with their prices | observed and selected | Pass |
| Smartwatch form condition dropdown | if any of the conditions if out of stock it can not be selected | observed | Pass |
| Smartwatch form condition dropdown | if all conditions are out stock all selectable options are disabled | observed | Pass |
| Smartwatch form condition dropdown | if all conditions are out of stock display "This item is currently out of stock" | observed | Pass |
| Smartwatch form condition quantity input | if all conditions are out of stock quantity input is disabled | observed | Pass | 
| Smartwatch form button | render with the text add to cart if phone is available | observed | Pass | 
| Smartwatch form button | disable if out of stock | observed | Pass |
| Smartwatch form button | add phone to bag with selected quantity and condition | clicked | Pass |
| Keep shopping button | load all products page | clicked | Pass |
<hr>
<br>
<br>

#### Console detailed page

Element | Excpected outcome | Testing performed | Outcome|
| :--- | :--- | :--- | :--- |
| Console name | rendering | observed | Pass |
| in stock indicator | displaying if phone is not out of stock | observed | Pass |
| This item is out of stock | rendering if item is out of stock | observed | Pass |
| only a few left indicator | displaying if stock count is less than or equal to 2 | observed | Pass |
| List of available conditions | display conditions where stock_count is at least 1 | observed | Pass |
| Console image | display | observed | Pass |
| Console image | turns grey if phone is out stock | observed | Pass |
| Console price | displaying | observed | Pass |
| Console price | displaying lowest available price if all conditions are available | observed | Pass |
| Console price | displaying lowest available price if only 2 conditions are available | observed | Pass |
| Console price | displaying lowest available price if only 1 condition is available | observed | Pass |
| Console price | hidden if out of stock | observed | Pass |
| Console out of stock | displays instead of the price if phone is out of stock | observed | Pass |
| Console form quantity input | can adjust quantity | tested with input | Pass |
| Console form condition dropdown | displaying available conditions with their prices | observed and selected | Pass |
| Console form condition dropdown | if any of the conditions if out of stock it can not be selected | observed | Pass |
| Console form condition dropdown | if all conditions are out stock all selectable options are disabled | observed | Pass |
| Console form condition dropdown | if all conditions are out of stock display "This item is currently out of stock" | observed | Pass |
| Console form condition quantity input | if all conditions are out of stock quantity input is disabled | observed | Pass | 
| Console form button | render with the text add to cart if phone is available | observed | Pass | 
| Console form button | disable if out of stock | observed | Pass |
| Console form button | add phone to bag with selected quantity and condition | clicked | Pass |
| Keep shopping button | load all products page | clicked | Pass |
<hr>
<br>
<br>

### All products views testing

#### All Laptops views

Element | Excpected outcome | Testing performed | Outcome|
| :--- | :--- | :--- | :--- |
| Laptop heading at the top | renders | observed | Pass |
| Laptop brands displaying as buttons | rendering | observed | Pass |
| DELL button | filtering the displayed Laptops | clicked | Pass |
| HP button | filtering the displayed Laptops | clicked | Pass |
| ASUS button | filtering the displayed Laptops | clicked | Pass |
| MSI button | filtering the displayed Laptops | clicked | Pass |
| Lenovo button |filtering the displayed Laptops | clicked | Pass |
| Acer button |filtering the displayed Laptops | clicked | Pass |
| Infinix button | filtering the displayed Laptops | clicked | Pass |
| Apple button | filtering the displayed Laptops | clicked | Pass |
| Reset button | resetting brand filter to none | clicked | Pass |
| Result number | updating on filtering | filtered for brands | Pass |
| Sort by Price | Low dropdown menu | sorts laptops with cheapest firt | clicked | Pass |
| Sort by Price | High dropdown menu | sorts laptops with most expensive first | clicked | Pass |
<hr>
<br>
<br>

#### All Phones

Element | Excpected outcome | Testing performed | Outcome|
| :--- | :--- | :--- | :--- |
| Phone heading at the top | renders | observed | Pass |
| Phone brands| displaying as buttons | observed | Pass |
| Huawei button |filtering the displayed Phones | clicked | Pass |
| Xiaomi button |filtering the displayed Phones | clicked | Pass |
| Oppo button |filtering the displayed Phones | clicked | Pass |
| Samsung button| filtering the displayed Phones | clicked | Pass |
| Google button |filtering the displayed Phones | clicked | Pass |
| Apple button| filtering the displayed Phones | clicked | Pass |
| Reset button |resetting brand filter to none | clicked | Pass |
| Result number |updating on filtering | filtered for brands | Pass |
| Sort by Price| Low dropdown menu | sorts Phones with cheapest firt | clicked | Pass |
| Sort by Price |High dropdown menu | sorts Phones with most expensive first | clicked | Pass |
<hr>
<br>
<br>

#### All Smartwatches

Element | Excpected outcome | Testing performed | Outcome|
| :--- | :--- | :--- | :--- |
| Smartwatch heading at the top | renders | observed | Pass |
| Smartwatch brands |displaying as buttons | observed | Pass |
| Garmin button |filtering the displayed Smartwatches | clicked | Pass |
| Apple button |filtering the displayed Smartwatches | clicked | Pass |
| Samsung button| filtering the displayed Smartwatches | clicked | Pass |
| Reset button |resetting brand filter to none | clicked | Pass |
| Result number| updating on filtering | filtered for brands | Pass |
| Sort by Price Low dropdown menu | sorts Smartwatches with cheapest firt | clicked | Pass |
| Sort by Price High dropdown menu | sorts Smartwatches with most expensive first | clicked | Pass |
<hr>
<br>
<br>


#### All Consoles

Element | Excpected outcome | Testing performed | Outcome|
| :--- | :--- | :--- | :--- |
| Console heading at the top | renders | observed | Pass |
| Console brands| displaying as buttons | observed | Pass |
| Microsoft button| filtering the displayed Consoles | clicked | Pass |
| Sony button| filtering the displayed Consoles | clicked | Pass |
| Nintendo button| filtering the displayed Consoles | clicked | Pass |
| Reset button |resetting brand filter to none | clicked | Pass |
| Result number |updating on filtering | filtered for brands | Pass |
| Sort by Price |Low dropdown menu | sorts Consoles with cheapest firt | clicked | Pass |
| Sort by Price| High dropdown menu | sorts Consoles with most expensive first | clicked | Pass |
<hr>
<br>
<br>

### Placing products in the bag

Element | Excpected outcome | Testing performed | Outcome|
| :--- | :--- | :--- | :--- |
| Laptop in bag| rendering with selected amount and condition in bag | added a laptop to the bag |Pass|
| Same Laptop in bag| same laptop rendering but with incremented amount | added a laptop with the same condition to the bag |Pass|
| Same Laptop with different condition| rendering separately | added the same laptop but with in different condition to the bag |Pass|
| Phone in bag| rendering with selected amount and condition in bag | added a phone to the bag |Pass|
| Same Phone in bag| same phone rendering but with incremented amount | added a phone with the same condition to the bag |Pass|
| Same Phone with different condition| rendering separately | added the same phone but with in different condition to the bag |Pass|
| Smartwatch in bag| rendering with selected amount and condition in bag | added a smartwatch to the bag |Pass|
| Same Smartwatch in bag| same smartwatch rendering but with incremented amount | added a smartwatch with the same condition to the bag |Pass|
| Same Smartwatch with different condition| rendering separately | added the same smartwatch but with in different condition to the bag |Pass|
| Console in bag| rendering with selected amount and condition in bag | added a console to the bag |Pass|
| Same Console in bag| same console rendering but with incremented amount | added a console with the same condition to the bag |Pass|
| Same Console with different condition| rendering separately | added the same console but with in different condition to the bag |Pass|
| Remove button | removes associated products | clicked |Pass|
| Empty cart | rendering when all products are removed | removed all products from bag| Pass |
| Keep shopping button | rendering when cart is empty | observed | Pass |
| Keep shopping button | loads all products page | clicked | Pass |
| Checkout button | rendering if at least one item is in the bag | observed | Pass |
| Checkout button | proceeds to checkout page | clicked | Pass |
| Shipping included | rendering if at least one item is in the bag| observed | Pass |
| Laptop details | rendering for laptops in the bag | observed | Pass |
| Phone details | rendering for phone in the bag | observed | Pass |
| Smartwatch details | rendering for smartwatches in the bag | observed | Pass |
| Console details | rendering for consoles in the bag | observed | Pass |
| Condition | rendering the selected condition for each item in the bag | observed | Pass |
| Price | rendering the selected price for every product | observed | Pass |
| Quantity | rendering the right amount for each item in the bag | observed | Pass |
| Subtotal | incrementing if the same condition of an item is added | added same item with same condition to the bag | Pass |
<hr>
<br>
<br>

### Checkout page testing

Element | Excpected outcome | Testing performed | Outcome|
| :--- | :--- | :--- | :--- |
| Checkout form | rendering | observed | Pass |
| Order summary | rendering with items from the bag | observeed | Pass |
| Order total | calculating item prices | added items to the bag | Pass |
| Checkout form labels | visible | observed | Pass |
| Adjust Cart button | takes user back to cart | clicked | Pass |
| Checkout form Full Name field | expects input | added input | Pass |
| Checkout form Email Address field | excpects email address as input | added input without @ | Pass |
| Checkout form Phone Number | expects input | added input | Pass |
| Checkout form Country dropdown box | expects selection | selected random input | Pass |
| Checkout form Postal Code | expects input | added input | Pass |
| Checkout form Postal Code | can be left blank | left blank | Pass |
| Checkout form Town or City | expects input | added input | Pass |
| Checkout form Street Address1 | expects input | added input | Pass |
| Checkout form Street Address2 | expects input | added input | Pass |
| Checkout form Street Address2 | can be left blank | left blank | Pass |
| Checkout form County | expects input | added input | Pass |
| Checkout form County | can be left blank | left blank | Pass |
| Payment form card field | expects seriously valid input | tested with 4242 4242 4242 4242 | Pass |
| Complete order button | won't proceed if form has missing fields | left required fields black | Pass |
| Complete order button | proceeds with the checkout if the form is valid | added valid input | Pass |
| Passing checkout form with valid information | loading overlay pops up |
<hr>
<br>
<br>

### Checkout success page

Element | Excpected outcome | Testing performed | Outcome|
| :--- | :--- | :--- | :--- |
| Page | Loads if checkout was successful | purchased items | Pass |
| OrderForm | displays with correct order data | purchased items | Pass |
| Home button | takes the user back to the landing page | clicked | Pass |


### Authorization pages

Element | Excpected outcome | Testing performed | Outcome|
| :--- | :--- | :--- | :--- |
| Person Icon in the navigation bar | opens drodpown | clicked | Pass |
| Link for Registering | takes the user the sign up page | clicked | Pass |
| Link for Logging ig | takes the user to the login page | clicked | Pass |
| Sign in form | rendering | observed | Pass |
| Sign up first on sign in page | takes the user to the sign up page | clicked | Pass |
| Home button on Sign In page | takes the user to the landing page | clicked | Pass |
| Sign in form | submits only when form is valid | entered invalid input | Pass |
| Sign in form | submits only when form is valid | entered valid input | Pass |
| Password reset link | takes the user to the password resetting page | clicked | Pass |
| Password reset form | takes email field as input | entered wrong input | Pass |
| Password reset form | works only if the user is registered | tried inexistent email | Pass |
| Password reset form | submits if the email is valid | tried valid email | Pass |
| Password reset form | sends email for changing passowrd | checked email address  | Pass |
| Password reset link | takes the user to the change password page | clicked | Pass |
| Resetting password form | takes input for new passowrd | added input | Pass |
| Reset password button | takes the user to the change password page | clicked | Pass |
| Sign up Form | rendering sign up fields | observed | Pass |
| Email field | expects email as input | tried wrong input | Pass |
| Email again field | excepts same value as Email field | added wrong input | Pass |
| Username field | excpets username as input | added input | Pass |
| Password field | excpets password | added input | Pass |
| Password again field | excpets same value as password field | added wrong input | Pass |
| Sign up button | takes the user to the email verification page | clicked | Pass |
| Verify You E-mail Address page | loads if form is valid | observed | Pass |
| Verify You E-mail Address page | sends verification email | email recieved | Pass |
| Link in email | takes user to the confirm email page | clicked | Pass |
| Confirm button | sets up account and takes user to landing page | clicked | Pass |
| Logout link | rendering instead of login link when user is logged in | observed | Pass |
| Home button | takes to user to the home page | clicked | Pass |
| Sign out button | signs user out | clicked | Pass |
<hr>
<br>
<br>

### Profile page

Element | Excpected outcome | Testing performed | Outcome|
| :--- | :--- | :--- | :--- |
| Profile page view | loads when clicking My profile link in the navigation bar | clicked | Pass |
| My Profile form | rendering empty form | observed | Pass |
| My Profile form phone number field | expecting input | added input | Pass |
| My Profile form street address 1 field | expecting input | added input | Pass |
| My profile form street address 2 field | expecting input | added input | Pass |
| My profile page Town or City field | expecting input | added input | Pass |
| My profile page County field | expecting input | added input | Pass |
| My profile page Postal Code field | expecting input | added input | Pass |
| My profile page Country field | expecting selection from dropdown | selected | Pass |
| Update Information | saves my profile form | clicked | Pass |
| Order History | renders with correct details | observed | Pass |
| Order Number | blue color suggesting it's a hyperlink | clicked | Pass |
| Loads previous order details | order details are correct | observed | Pass |
| Updated information | autofills checkout form | observed | Pass |
<hr>
<br>
<br>

### Adding products

#### Laptop

Element | Excpected outcome | Testing performed | Outcome|
| :--- | :--- | :--- | :--- |
| Laptopform | rendering | observed | Pass |
| Stock info notice | rendering | observed | Pass |
| Price notice | rendering | observed | Pass |
| Category field | automatically selects laptop | observed | Pass |
| Brand field | expects input | added input | Pass|
| Series field | expects input | added input | Pass|
| Model field | expects input | added input | Pass|
| Color field | expects input | added input | Pass|
| Price field | expects input | added input | Pass|
| Sale field | expects true | clicked checkbox | Pass|
| Image Field field | expects image | added image | Pass|
| Image Url field | expects input | added input | Pass|
| Label field | expects input | added input | Pass|
| Cpu brand field | expects input | added input | Pass|
| Cpu name field | expects input | added input | Pass|
| Cpu variant field | expects input | added input | Pass|
| Cores field | excpets selection from dropdown menu | selected | Pass |
| Ram field | expects input | added input | Pass|
| Storage size field | expects input | added input | Pass|
| Gpu field | expects input | added input | Pass|
| Os field | expects input | added input | Pass|
| Weight field | expects input | added input | Pass|
| Screen size field | expects selection from dropdown menu | selected | Pass |
| Dimension field | expects input | added input | Pass|
| Hdmi field | expects input | added input | Pass|
| Usb field | expects input | added input | Pass|
| Keyboard field | expects input | added input | Pass|
| Touchscreen field | expects true | clicked checkbox | Pass |
| Backlit field | expects true | clicked checkbox | Pass |
| Finger print sensor field | expects true | clicked checkbox | Pass |
| Add product | creates object and loads it's page | clicked | Pass |
<hr>
<br>
<br>

#### Phone

Element | Excpected outcome | Testing performed | Outcome|
| :--- | :--- | :--- | :--- |
| Phoneform | rendering | observed | Pass |
| Stock info notice | rendering | observed | Pass |
| Price notice | rendering | observed | Pass |
| Category field | automatically selects laptop | observed | Pass |
| Brand field | expects input | added input | Pass|
| Series field | expects input | added input | Pass|
| Model field | expects input | added input | Pass|
| Color field | expects input | added input | Pass|
| Price field | expects input | added input | Pass|
| Sale field | expects true | clicked checkbox | Pass|
| Image Field field | expects image | added image | Pass|
| Image Url field | expects input | added input | Pass|
| Sim field | expects input | added input | Pass|
| Cpu field | expects input | added input | Pass|
| Ram field | expects input | added input | Pass|
| Storage size field | expects input | added input | Pass|
| Battery field | expects input | added input | Pass|
| Reolusion field | expects input | added input | Pass|
| Camera front field | expects input | added input | Pass|
| Camera rear field | expects input | added input | Pass|
| Os field | expects selection from dropdown menu | selected | Pass |
| Add product | creates object and loads it's page | clicked | Pass |
<hr>
<br>
<br>

#### Smartwatch

Element | Excpected outcome | Testing performed | Outcome|
| :--- | :--- | :--- | :--- |
| Smartwatchform | rendering | observed | Pass |
| Stock info notice | rendering | observed | Pass |
| Price notice | rendering | observed | Pass |
| Category field | automatically selects laptop | observed | Pass |
| Brand field | expects input | added input | Pass|
| Series field | expects input | added input | Pass|
| Model field | expects input | added input | Pass|
| Color field | expects input | added input | Pass|
| Price field | expects input | added input | Pass|
| Sale field | expects true | clicked checkbox | Pass|
| Image Field field | expects image | added image | Pass|
| Image Url field | expects input | added input | Pass|
| Connectivity field | expects input | added input | Pass|
| Display field | expects input | added input | Pass|
| Screen Size field | expects input | added input | Pass|
| Resolution field | expects input | added input | Pass|
| Water resistance field | expects input | added input | Pass|
| Heart rate monitor field  field | expects true | clicked checkbox | Pass|
| Gps  field | expects true | clicked checkbox | Pass |
| Os field | expects input | added input | Pass|
| Add product | creates object and loads it's page | clicked | Pass |
<hr>
<br>
<br>

#### Console

Element | Excpected outcome | Testing performed | Outcome|
| :--- | :--- | :--- | :--- |
| Consoleform | rendering | observed | Pass |
| Stock info notice | rendering | observed | Pass |
| Price notice | rendering | observed | Pass |
| Category field | automatically selects laptop | observed | Pass |
| Brand field | expects input | added input | Pass|
| Series field | expects input | added input | Pass|
| Model field | expects input | added input | Pass|
| Color field | expects input | added input | Pass|
| Price field | expects input | added input | Pass|
| Sale field | expects true | clicked checkbox | Pass|
| Image Field field | expects image | added image | Pass|
| Image Url field | expects input | added input | Pass|
| Storage size field | expects input | added input | Pass |
| Add product | creates object and loads it's page | clicked | Pass |
<hr>
<br>
<br>


### Editing views

Element | Excpected outcome | Testing performed | Outcome|
| :--- | :--- | :--- | :--- |
| edit button on laptop detail page | rendering if user is superuser | observed | Pass |
| delete button on laptop detail page | rendering if user is superuser | observed | Pass |
| edit button on phone detail page | rendering if user is superuser | observed | Pass |
| delete button on phone detail page | rendering if user is superuser | observed | Pass |
| edit button on smartwatch detail page | rendering if user is superuser | observed | Pass |
| delete button on smartwatch detail page | rendering if user is superuser | observed | Pass |
| edit button on console detail page | rendering if user is superuser | observed | Pass |
| delete button on console detail page | rendering if user is superuser | observed | Pass |
<hr>
<br>
<br>

#### Laptop and inventory editing


Element | Excpected outcome | Testing performed | Outcome|
| :--- | :--- | :--- | :--- |
| edit button on laptop page | takes the user to the laptops editing view with the laptops details| clicked | Pass |
| cancel button | takes the user back to the laptop's page | clicked | Pass |
| update product button | updates product details and reloads laptop detailed page | clicked | Pass |
| edit inventoty button on laptop editing page | takes the user to the laptop's inventory model's editing page | clicked | Pass |
| editing inventory page | loads inventory of the laptop we're editing | observed | Pass |
| inventory stock_count field | only editable field | observed | Pass |
| Back button | takes the user back to the laptop editing page | clicked | Pass |
| Update Inventory button | updates inventory and reloads laptop's detailed page | clicked | Pass |
<hr>
<br>
<br>

#### Phone and inventory editing


Element | Excpected outcome | Testing performed | Outcome|
| :--- | :--- | :--- | :--- |
| edit button on phone page | takes the user to the phones editing view with the phones details| clicked | Pass |
| cancel button | takes the user back to the phone's page | clicked | Pass |
| update product button | updates product details and reloads phone detailed page | clicked | Pass |
| edit inventoty button on phone editing page | takes the user to the phone's inventory model's editing page | clicked | Pass |
| editing inventory page | loads inventory of the phone we're editing | observed | Pass |
| inventory stock_count field | only editable field | observed | Pass |
| Back button | takes the user back to the phone editing page | clicked | Pass |
| Update Inventory button | updates inventory and reloads phone's detailed page | clicked | Pass |
<hr>
<br>
<br>

#### Smartwatch and inventory editing


Element | Excpected outcome | Testing performed | Outcome|
| :--- | :--- | :--- | :--- |
| edit button on Smartwatch page | takes the user to the Smartwatchs editing view with the Smartwatchs details| clicked | Pass |
| cancel button | takes the user back to the Smartwatch's page | clicked | Pass |
| update product button | updates product details and reloads Smartwatch detailed page | clicked | Pass |
| edit inventoty button on Smartwatch editing page | takes the user to the Smartwatch's inventory model's editing page | clicked | Pass |
| editing inventory page | loads inventory of the Smartwatch we're editing | observed | Pass |
| inventory stock_count field | only editable field | observed | Pass |
| Back button | takes the user back to the Smartwatch editing page | clicked | Pass |
| Update Inventory button | updates inventory and reloads Smartwatch's detailed page | clicked | Pass |
<hr>
<br>
<br>

#### Console and inventory editing


Element | Excpected outcome | Testing performed | Outcome|
| :--- | :--- | :--- | :--- |
| edit button on Console page | takes the user to the Consoles editing view with the Consoles details | clicked | Pass |
| cancel button | takes the user back to the Console's page | clicked | Pass |
| update product button | updates product details and reloads Console detailed page | clicked | Pass |
| edit inventoty button on Console editing page | takes the user to the Console's inventory model's editing page | clicked | Pass |
| editing inventory page | loads inventory of the Console we're editing | observed | Pass |
| inventory stock_count field | only editable field | observed | Pass |
| Back button | takes the user back to the Console editing page | clicked | Pass |
| Update Inventory button | updates inventory and reloads Console's detailed page | clicked | Pass |



### Testing responsiveness

<hr>

 * Responsiveness of the page was tested manually using Google Chrome developer tools
   * The website is confirmed to be responsive on every screen size without any distortion
   * Images do not stretch or distort in smaller screen sizes
   * Texts remain readable on every screen size
   * Pages look nice on as small as 320px wide




Back to [README.md](https://github.com/GaborFicsor/steezy-spatula/blob/main/README.md)

Back to [top](#top)