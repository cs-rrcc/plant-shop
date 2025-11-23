# Overview of Unbeleafable

The Unbeleafable Plant Shop is an online marketplace that connects horticulturists with customers who want to buy plants. Sellers can create listings, manage inventory, and track sales, while customers can browse plants, 
filter by category, make purchases, and view past orders. The system provides a simple, convenient interface for both buyers and growers, targeting local plant sellers and customers looking to build or expand their gardens.

# Design

## User Stories

Describe the **user stories** for the project, which are short, simple descriptions of a feature told from the perspective of the end user. Each **user story** should include clear **acceptance criteria** and a **point estimate**. The **user stories** must align with the **use case diagram** and should be labeled as US#1, US#2, and so on. We suggest creating a separate Markdown section for each **user story**.

This section describes key user stories identified for the project.

### User Story #1: User Registration

#### Allotted Story Points: 1

As a new user of the system, I want to register for the plant store platform by providing my name, a unique email address, a password, and my role as a horticulturist or customer so that I can either sell or buy plants based on my role. Given that I have supplied all of the required information in the sign up page, when I hit the "Submit" button, then my account should be created and stored in the system.

### User Story #2: View Plant Inventory

#### Allotted Story Points: 2

As a logged-in horticulturist, I want to view all of the plants I have for sale and the plants my competitors have for sale so that I can evaluate the market, update my plant listings, and sell the plants I have grown all in one interface. Given that I am logged in, when the plant dashboard loads, then I can see all of the plants available for sale organized in a convenient format.

### User Story #3: New Plants for Sale

#### Allotted Story Points: 3

As a logged-in horticulturist, I want to create a plant listing with information about the plant's name, color, variety, required climate, and price, so that I can publish a plant listing and sell it to customers. Given that I have entered in the required plant information, when I hit the "List" button, then the plant is saved into the system and can be purchased by customers.

### User Story #4: View Plants for Sale

#### Allotted Story Points: 8

As a customer, I want to view all the plants for sale at the same time or by a specific category so that I can purchase plants and start a garden. Given that I am logged in and on the sale page, when I select the category of plants I want to look from and click the category I want, then a list of plants for sale will be displayed based on the categories/category of my choosing.

### User Story #5: Purchase Plants

#### Allotted Story Points: 13

As a customer, I want to add plants to my cart so that I can purchase them. Given that I am logged-in, the plant being selected is for sale, the plant has been added to my cart, and I am in my cart, when the button "Order Now" has been clicked, then I have purchased the plants and the system records the purchase.

### User Story #6: View Plant Invoice

#### Allotted Story Points: 5

As a customer, I want to view my previous plant orders so that I can keep track of what types of plants I have purchased. Given that I am logged-in and have made a purchase, when I select the "view recent orders" page, then I can view a list of all my orders organized by order date.

## Sequence Diagram

At least one **user story**, unrelated to user creation or authentication, must be detailed using a **sequence diagram**. A **sequence diagram** is a type of UML diagram that shows how objects interact in a particular scenario, emphasizing the order of messages exchanged between components over time. This helps visualize the flow of operations and the responsibilities of different parts of the system.

## Class Model Diagram

Include a **class diagram** that clearly describes the **model classes** used in the project and their associations. A **class diagram** is a UML diagram that represents the structure of the system by showing its classes, their attributes, methods, and the relationships between them (such as inheritance, aggregation, or composition). This helps visualize how the data and logic are organized within the application.

# Development Process

This section should describe, in general terms, how Scrum was applied in the project. Include a table summarizing the division of the project into sprints, the **user story** goals planned for each sprint, the ones actually completed, and the start and end dates of each sprint. You may also add any relevant observations or reflections about the sprints as you see fit.

| Sprint# | Goals           | Start    | End      | Done | Observations |
| ------- | --------------- | -------- | -------- | ---- | ------------ |
| 1       | US#1, US#2, ... | mm/dd/23 | mm/dd/23 | US#1 | ...          |

As in Project 2, you should take notes on the major Scrum meetings: planning, daily scrums, review, and retrospective. These meetings are essential for tracking progress, identifying obstacles, and ensuring continuous improvement. Use the Scrum folder and the shared templates to record your notes in an organized and consistent manner.

Embed an image of the burndown chart here.

# Testing

In this section, share the results of the tests performed to verify the quality of the developed product, including the test coverage relative to the written code. Test coverage indicates how much of your code is exercised by tests, helping assess reliability. There is no minimum coverage requirement, but ensure there is at least some coverage through one white-box test (which examines internal logic and structure) and one black-box test (which validates functionality from the user’s perspective).

| User Story | Feature/Function                 | Date     | Time  | Result |
| ---------- | -------------------------------- | -------- | ----- | ------ |
|            |                                  |          |       |        |
|            |                                  |          |       |        |
|            |                                  |          |       |        |
|            |                                  |          |       |        |
|            |                                  |          |       |        |
|            |                                  |          |       |        |
|            |                                  |          |       |        |
|            |                                  |          |       |        |
|            |                                  |          |       |        |
|            |                                  |          |       |        |