# Sprint Planning

## Date/Time: 12/02/25-16:30

Participants: Andrew, Mckenna, and Kobe

Goal Statement: Our focus is enabling the customer to view their previous orders from the store within the Unbeafable application. We believe this feature will allow customers to feel confident in purchasing from Unbealfable because they can keep track of their purchases on our platform. This will be confirmed when the customer can view their previous orders and the plants that were in each order.

Estimated sprint completion date: December 6th

Estimated story points for this sprint: 5

User stories included in sprint: #6

* For the last sprint, the team decided to focus on just one user story. This was so testing, deployment, and general polishing tasks of the project's README file would be the primary focus after the user story was completed. Furthermore, only tackling one user story will allow the team to perform a thorough code review to ensure the code base is PEP-8 compliant.

Tentative Work:

* [X] User Story 6
  * [X] View order HTML
  * [X] View Order Route
    * [X] List all orders organized by order date
    * [X] Click view order button
      * [X] view order items page
      * [X] list all plants bought in that order
* [X] Robust error handling
* [X] Comments
* [X] Test coverage HTML and photo
* [X] White box testing
  * [X] Update Readme with info
* [X] Black box testing
  * [X] Update readme with info
* [X] Docker Deployment
* [X] Finalized README
* [X] Finalized scrum notes
* [X] Burndown generated

Assigned Sprint Work:

* Kobe: White box testing, black box testing, and team evaluation
* Andrew: View order route and HTML, view order items route and HTML, fix view cart logic, and team evaluation
* Mckenna: Scrum notes, order and order items queries, burndown chart, fix code base comments, Docker deployment tests, and team evaluation

# Daily Scrums

## 12/03/25-13:00

Participants: Mckenna, Andrew, and Kobe

Kobe:

* What did I do yesterday to help the team?
  * Yesterday I was apart of the sprint meeting and helped divide work up.
* What will I do today to help the team?
  * Today I worked on tackling the start of black box testing.
* Do I see any impediment that prevents me from making progress?
  * I have band practice today, but as we are tracking bass, I should have some free time during rehearsal to tackle what I need to do or at least get a start.

Andrew:

* What did I do yesterday to help the team?
  * Yesterday I attended the sprint meeting and helped plan for the final stretch of the project. I performed manual tests before the code base was pushed to main as well.
* What will I do today to help the team?
  * I will refactor the view cart logic to better match clean code standards. I will also peform manual tests.
* Do I see any impediment that prevents me from making progress?
  * No blockers today.

Mckenna:

* What did I do yesterday to help the team?
  * Yesterday, I held the sprint planning meeting and compiled all of the notes from it. I also coordinated the notes and README file for the second sprint and pushed everything to the main branch.
* What will I do today to help the team?
  * I plan on working on the queries for returning the orders and the order items for the view order dashboard.
* Do I see any impediment that prevents me from making progress?
  * Yes, my work will not be distributed to my team right away because my schedule is very busy today.

Overall Notes:

* User story six is expected to be completed very early on in the sprint.
* Extensive Docker deployment tests will occur once all the user stories have been implemented.

## 12/04/25-15:20

Participants: Andrew, Mckenna, and Kobe

Kobe:

* What did I do yesterday to help the team?
  * Yesterday I began the planning and writing of the black box test.
* What will I do today to help the team?
  * Today I will finalize and finish up the black box testing and make sure tests pass with OK. I will also begin the white box testing and then remain 'on-call' to assist where I can while also helping managing tests and other such things.
* Do I see any impediment that prevents me from making progress?
  * None!

Andrew:

* What did I do yesterday to help the team?
  * Yesterday I updated the view cart route to match our refactored logic. I also manually tested that the Order and Order Item objects populate correctly into database.
* What will I do today to help the team?
  * Today I worked on the view order and view items in order HTML and routes.
* Do I see any impediment that prevents me from making progress?
  * No blockers right now might have to refactor some of the routes.

Mckenna:

* What did I do yesterday to help the team?
  * I worked on the functions that query for the orders and the order items in each order.
* What will I do today to help the team?
  * Today, I will create a function to grab a single order so our route for getting orders will be decomposed properly and follow clean coding standards. I will also test Docker deployment with all six user stories and make note of the manual tests. Furthermore, I will update the README to polish our current notes. Finally, I will be available for other tasks that come up.
* Do I see any impediment that prevents me from making progress?
  * Yes, I am working on two projects at once and have a lot of chores. Getting code to my team will take time.

Overall Notes:

* The current black box tests were not in scope of the assignment and will need to be re-done.
* Generating the burndown chart will take time as the format in the ".xlsx" file makes it difficult to generate a line chart.

## 12/06/25-14:00

Participants: Mckenna

Mckenna:

* What did I do yesterday to help the team?
  * I was unable to work on the project, so I did not do much to help the team.
* What will I do today to help the team?
  * I will make sure our code base, excluding the init file, is compliant with PEP-8 standards. I will polish the README to make sure it follows the project rubric. I will add the header comments to all the source code files and ensure that test coverage is included in the repository. Finally, I will proof all of the note documents to correct grammar errors and format inconsistencies.
* Do I see any impediment that prevents me from making progress?
  * Yes, I have a migraine so working on this project will be slower than normal.

Overall Notes:

* A lot of the README file needed to be edited so it will be easier to understand and read.
* The source code files will need to be heavily reviewed to ensure comments are PEP-8 compliant.

# Sprint Review

## 12/07/25-13:45

Participants: Andrew, Kobe, and Mckenna

Notes/Topics Discussed:

* A final walkthrough of all the user stories was conducted using both Docker and running the application manually in VSCode.
* Five points were planned for this sprint, the group agrees that five points were spent.
* User story six was thoroughly tested and the customer can view their past orders chronologically and they can view the items in each order.
* User story six is considered done.
* A part of the code base was deleted which caused several bugs. This issue was caught before deployment though.
* During the final code review, error handling was mistakenly left out in the "view_cart" function. This issue was also caught and fixed before deployment.
* Black box and white box testing were successfully implemented in this sprint.
* The code base faced a few small adjustments to abide by clean code standards

# Sprint Retrospective

## 12/07/25-14:00

Participants: Andrew, Kobe, and Mckenna

#### What went wrong:

Andrew: 

* I had to redo a few routes because some of the functions were doing more than they should. I ran into some Git merge issues that caused extra commits and merged some things outside of current sprint. The view orders/view items pages took a few tries to get right so they matched our team’s style and decomposition setup.

Kobe:

* Having to use the specific formatting tripped me up a few times and there were many times I had completely forgot. I also had a hard time trying to find the exact rubric / criteria at times.

Mckenna:

* Finishing this project was tough because I had other major assignments due and some health problems arise,
* It was also tough having to constantly decompose functions and ensure the code base followed clean code standards and was PEP-8 compliant.

#### What can improve for the next sprint/project:

* Ensure that everyone starts the project as soon as possible.
* Have more consistent pushes to the dev branch so more people can work on the project at once.
