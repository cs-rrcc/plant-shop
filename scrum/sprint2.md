# Sprint Planning

## Date/Time: 11/25/25-14:00

Participants: Andrew, Mckenna, and Kobe

Goal Statement: Our focus is enabling the customer to view specific categories from active plant listings and enable them to put them into their cart to then purchase later within our application. We believe these features will allow customers to make educated decisions on what plants they need to buy. This will be confirmed when the customer can view plant listings by category and complete an order form their cart.

Estimated sprint completion date: December 3rd

Estimated story points for this sprint: 21

User stories included in sprint: #4, #5

* The group chose to tackle the highest point stories for sprint two for a few reasons. First, this sprint will be the longest of the project, taking around eight days to complete. So, more features should hopefully be tackled since there is more time to complete them. Also, user stories four and five relied on the stories implemented in the previous sprint so they could not have been tackled until now. Finally, these user stories are surrounding functionality for the customer role, so they can be naturally grouped together.

Tentative Work:

* [X] Populate customer dashboard HTML.

  * [X] List all plants at first.
  * [X] Button labeled add to cart.
* [X] View cart page HTML.
* [X] Fix all plants function to only return plants with a quantity greater than 0.
* [X] Cart Model
* [X] Cart Item Model
* [X] Order Model
* [X] Order Item Model
* [X] Plant Category Drop-down Form
* [X] Order Button
* [X] Customer dashboard:

  * [X] Create one cart object associated with the user if one has no been created already.
  * [X] View all plants on open.
  * [X] View plants by category via drop-down for submission.
* [X] Customer add to cart:

  * [X] Assuming item quantity is not zero, a button next to the add to cart can be clicked. This would create a new cart item associated with the user's cart and the plant selected.
* [X] Customer view cart and purchase items.

  * [X] Display total value of items in cart.
  * [X] When place order is clicked, an order object and order item objectes are created from the cart object and the cart item objects.
  * [X] The current cart is set to inactive.
  * [X] Query to database to remove bought plants.
  * [X] Create order object.
  * [X] Populate order items with cart items.

Assigned Sprint Work:

* Kobe: Start add to cart route, function check for plant quantity, and functionality for populating cart item objects.
* Andrew: View cart route and HTML page, and applying cart at checkout functionality.
* Mckenna: Scrum notes, cart model, cart item model, object model, object item model, HTML for customer dashboard, form for categories on customer dashboard, get plants by category function, start customer dashboard route, order creation route, and function decomposition for all the add to cart and order creation code.


# Daily Scrums

## 11/26/25-14:40

Participants: Kobe and Mckenna

Kobe:

* What did I do yesterday to help the team?
  * Yesterday I was unable to totally tackle anything outside of very loose planning on my end for what to do.
* What will I do today to help the team?
  * I will plan further and attempt to get a start on my routes.py work. (Primarly adding a function to make sure plant quantity > 0 and also only plants with that quantity are displayed)
* Do I see any impediment that prevents me from making progress?
  * It is holiday break and I don't have much motivation to work. But alas, I will work!

Mckenna:

* What did I do yesterday to help the team?
  * I conducted the sprint planning meeting and compiled all of the notes from it and organized them for the team in Discord.
* What will I do today to help the team?
  * I will populate the customer dashboard HTML page and add a category view form for returning plants by category. I will also get started on the customer dashboard route and implement the get plants by category function. I will edit the plant form to ensure only positive numbers (zero and above) can be inputted as the plant's quantity. Finally, I will get started on the cart and cart item models so user story five can be started soon.
* Do I see any impediment that prevents me from making progress?
  * No, my primary focus is this project today, so I should be able to make a lot of progress.

Overall Notes:

* User story four is progressing faster than expected.
* It was decided that instead of deleting plant listings, horticulturists could change the quantity to zero instead.
* Zero filtering will be applied to the get plant queries for other horticulturists and the customers.

## 11/28/25-15:20

Participants: Andrew, Mckenna, and Kobe

Kobe:

* What did I do yesterday to help the team?
  * Yesterday I began the work on the routes.py and customer_dashboard.html work.
* What will I do today to help the team?
  * Today I will finish both files of which I started and then proceeded to push / commit them to the repository.
* Do I see any impediment that prevents me from making progress?
  * None!

Andrew:

* What did I do yesterday to help the team?
  * Yesterday I worked on planning out the cart functionality and tested the customer dashboard.
* What will I do today to help the team?
  * Today I will finish the view cart route, add the HTML page for displaying cart items, and the order now button with functionality.
* Do I see any impediment that prevents me from making progress?
  * No major blockers right now. Everything is working.

Mckenna:

* What did I do yesterday to help the team?
  * I did not do much to help every one out because it was Thanksgiving.
* What will I do today to help the team?
  * Today I will break down functions so it will be easier to run and debug the code base. I will also plan for how the order model will work.
* Do I see any impediment that prevents me from making progress?
  * I am was consulting today so I will not be able to contribute much to the team.

Overall Notes:

* The project is progressing at an execellent pace.
* Remembering to break down functions when developing features has been a challenge.
* Pycode style has been easier to use and it is simpler to code with the PEP-8 standard now.

## 11/29/25-17:00

Participants: Mckenna

Mckenna:

* What did I do yesterday to help the team?
  * I decomposed several of the routes into helper functions. I also made note of a few errors with the models.
* What will I do today to help the team?
  * Throughout the day I will work on the order model, the order items model, and adjust the client and cart models to use enums properly. I will then re-test the cart and user models to ensure the enums are properly used.
* Do I see any impediment that prevents me from making progress?
  * I have a very busy day so it will be challenging finding time to sit down and work on everything.

Overall Notes:

* It was realized that we should be referencing the models made in the last sprint more when programming for this sprint.
* Docker deployment is still being tested in this sprint and it going smoothly.

## 11/30/25-15:00

Participants: Mckenna

Mckenna:

* What did I do yesterday to help the team?
  * Yesterday I focused on creating the order model and the order items model. Also, I edited the user model and the cart model to include enums as originally planned in the class diagram. Finally, I re-tested creating a user and cart to ensure the enum types and routes were working together.
* What will I do today to help the team?
  * The focus of today will be to create the order and order items objects when the user hits the "Order Now" button in their cart page. Additionally, I will make sure these objects are recorded in the database. Finally, I will slowly start incorporating more robust error handling.
* Do I see any impediment that prevents me from making progress?
  * Yes, I am working on two projects at once and chores so my pushes to GitHub will be delayed. Also, delegating project tasks will be delayed due to my busy schedule.

Overall Notes:

* Populating the order and order items tables was tedious and required a lot of debugging and testing.
* A lot of manual tests will need to occur before this sprint is considered done.

## 12/01/25-14:00

Participants: Andrew and Mckenna

Andrew:

* What did I do yesterday to help the team?
  * Yesterday I worked on view cart routes and the html.
* What will I do today to help the team?
  * Today I updated the view cart route to match our refactored logic. I also manually tested that the Order and Order Item objects populate correctly into database.
* Do I see any impediment that prevents me from making progress?
  * No blockers right now everything is working correctly from my tests.

Mckenna:

* What did I do yesterday to help the team?
  * I developed the functionality for the user to submit their order and have it saved in the system. So, I worked on populating the order and order items objects in the database after the "Order Now" button was hit by the user. I also moved the order functionality to a separate function for easier code reviewing.
* What will I do today to help the team?
  * Today, I will polish our current scrum notes and plan for the next sprint. I will also fix the class UML diagram to better reflect the order and order item objects. Finally, I will thoroughly test the application to ensure we are ready to finish the sprint.
* Do I see any impediment that prevents me from making progress?
  * No, I am able to dedicate a lot of time to this project today.

Overall Notes:

* This sprint is expected to finish a day early.
* Error handling is slowly being updated to be more robust.

# Sprint Review

## 12/2/25-15:45

Participants: Andrew, Kobe, and Mckenna

Notes/Topics Discussed:

* Final walkthrough of user stories four and five were considered successful.
* Twenty-one points were planned for this sprint and the group agrees that twenty-one story points were spent/achieved during it.
* User story four was tested and the customer can view plants by both variety and climate via a drop down menu.
* User story five's tests showed that when the user clicks the "Order Now" button, their order is saved in the system, their cart is emptied, and they will get a new cart if they purchase more items after their order.
* User story four, view plants for sale, and user story five, purchase plants, are considered done.
* The code base looks well organized and seems to follow clean code standards.

# Sprint Retrospective

## 12/2/25-16:05

Participants: Andrew, Kobe, and Mckenna

#### What went wrong:

Andrew:

* No major issues other than remembering to decompose functions so all of the code is not in each route.

Kobe:

* There were some issues with files populating on GitHub when pulling from origin. This caused a slight delay in getting code from everyone.

Mckenna

* It was difficult to balance working on the project during the fall break. I took too much time off causing delays in code releases and notes being distributed to the team.
* I did not closely follow the class diagram for some of the objects developed in the models file, which caused a design miscommunication.

#### What can improve for the next sprint:

* Devote more time to the project so code pushes are not delayed for the other team members.
* Adjust the diagrams and notes right away so everyone understands the design changes being made.
