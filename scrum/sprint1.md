# Project Three Initial Plan

## Date/Time: 11/19/25-15:30

Participants: Andrew, Mckenna, and Kobe

* It was decided by the group to make a small garden store, Unbeleafable, using Python Flask, HTML, CSS, and Sqlite3.
* A multi-tiered architecture approach will not be implemented because the primary focus of the project is to complete all six user stories and the required notes for the project within the allotted time frame.
* Condensed Overview Statement:
  * The goal of this project is to develop a web application that optimizes the sale, purchase, and distribution of plants, flowers, and other greenery.
* The six user stories will be in the README and a separate product backlog file will be created as well.
* Deployment will be tested with each sprint but testing, both white box and black box, will be implemented across the multiple sprints.

# Sprint Planning

## Date/Time: 11/19/25-16:00

Participants: Andrew, Mckenna, and Kobe

Goal Statement: Our focus is for all users to register and log in to the application and for horticulturists to create and view plant sale listings in Unbeleafable. We believe it delivers essential user functionality to the shopping platform. This will be confirmed when users can register and login as well as when horticulturists can view and create plant listings.

Estimated sprint completion date: November 26th

Estimated story points for this sprint: 6

User stories included in sprint: #1, #2, and #3

* The group chose to tackle three user stories for this sprint for several reasons. First, the register, login, and logout functionality has been done in previous projects so it will be easy to replicate for this one. Second, user stories two and three rely on each other to offer meaning to the user. Therefore, they will be implemented together to ensure the requirements are thoroughly tested and met. Finally, these three stories are the simplest to tackle while building the project from the ground up.

Tentative Work:

* [X] Base HTML populated with login, logout, and dashboard buttons based on the user.
* [X] Populate CSS file.
* [X] Plant dashboard for the seller/horticulturist.
* [X] Plant creation page for seller.
* [X] Plant update page for seller.
* [X] Error page for major errors (like objects not committing to database).
* [X] Generic CSS to make it easier to view everything.
* [X] Form to sign up for the website.
* [X] Form to create or update a plant.
* [X] Sign up functionality route.
* [X] Login functionality route.
* [X] Logout functionality route.
* [X] Plant dashboard for seller route.
* [X] Plant creation route/method.
* [X] Plant update route/method.
* [X] User model.
* [X] Plant model.
* [X] Class diagram.
* [X] Sequence diagram.
* [X] Use case diagram.
* [X] Product backlog.
* [X] User story notes.
* [X] Project overview written.

Assigned Sprint Work:

* Kobe: Plan for the project, base HTML, and CSS.
* Andrew: Plan for the project, use case diagram, sequence diagram, sign up route, login route, logout route, and create plant route.
* Mckenna: Plan for the project, create GitHub public repository, enforce main branch protection rules, set up skeleton of project, scrum notes, class UML diagram, init file, both required models (user and plant), login form, sign up form, plant creation/update form, seller dashboard view functionality route, populate all HTML files other than base.html, and begin testing deployment with Docker.

# Daily Scrums

## 11/21/25-14:40

Participants: Andrew and Mckenna

Andrew:

* What did I do yesterday to help the team?
  * Helped plan for the project and identify what needs to be done.
* What will I do today to help the team?
  * I will work on the use case diagram and the sequence diagram.
* Do I see any impediment that prevents me from making progress?
  * Nothing should stop me from making progress today.

Mckenna:

* What did I do yesterday to help the team?
  * First, I set up the public repository, enforced rules on the main branch, and set up the project skeleton. I also summarized what was discussed in our planning meetings in the "sprint1.md" file.
* What will I do today to help the team?
  * I will be on call if anyone has questions or wants to brainstorm but I will only be able to create the "__init__.py" file and the user model today.
* Do I see any impediment that prevents me from making progress?
  * Yes, for both me and my team. I am taking the afternoon off to visit a family member in the hospital.

Overall Notes:

* The initial project planning activities are going smoothly, allowing everyone to contribute to the project's vision.
* Making sure everyone had updated meeting notes was a tedious process.

## 11/22/25-14:40

Participants: Andrew, Mckenna, and Kobe

Kobe:

* What did I do yesterday to help the team?
  * Yesterday, I didn't actively do much as a lot of the planning was done whilst I was unavailable, however, I remained 'on call' and was ready to assist when available!
* What will I do today to help the team?
  * I will continue to plan for how the web-app will run and work, whilst remaining 'on call' to assist with the creation of anything. Furthermore, I will start working on the core HTML files for the project.
* Do I see any impediment that prevents me from making progress?
  * Not much. Only a few household chores that I will have to take care of with my parents, but that is all.

Andrew:

* What did I do yesterday to help the team?
  * I worked on the sequence diagram and the use case diagram.
* What will I do today to help the team?
  * I will finish writing the signup, login, logout, and create plant routes. Code will be cleaned with pycodestyle before pushing as well.
* Do I see any impediment that prevents me from making progress?
  * Yesterday I made some repo mistakes and spent time fixing them but they are fixed now so I am not facing any impediments.

Mckenna:

* What did I do yesterday to help the team?
  * I did not do much to help the team because I was tending to family matters. All I did was create the "init" file and the user model but I made sure both followed PEP-8 standards with pycodestyle.
* What will I do today to help the team?
  * Today I will do the class diagram, I will populate the model file with the plant model, and I will work on the forms to create a user, create a plant, and update a plant.
* Do I see any impediment that prevents me from making progress?
  * Yes, I have another project that needs to be done which will interfere with my ability to focus on this one.

Overall Notes:

* There was a major miscommunication involving where the project was located. However, everyone is on the public repository now.
* There was another miscommunication with the user stories but it was resolved during the meeting.
* Using pycodestyle is a learning curve.

## 11/23/25-13:30

Participants: Andrew, Mckenna, and Kobe

Kobe:

* What did I do yesterday to help the team?
  * Yesterday I remained on call and began to plan what to do for templates / static.
* What will I do today to help the team?
  * Today I will complete the base html template and static/style.css sheet.
* Do I see any impediment that prevents me from making progress?
  * I have work today, but that is it.

Andrew:

* What did I do yesterday to help the team?
  * Yesterday I finished writing the signup, login, logout, and create plant routes and made sure everything followed pycodestyle before pushing.
* What will I do today to help the team?
  * I will create the project overview based on the notes we have made so far.
* Do I see any impediment that prevents me from making progress?
  * None today because the repository issues have been fixed.

Mckenna:

* What did I do yesterday to help the team?
  * I created the necessary models and forms for sprint one (plant and user creation based).
* What will I do today to help the team?
  * Today I will work on the functionality to view the plants for sale with a focus on function decomposition. I will also make sure all the python code adheres to PEP-8 and the stakeholders' expectations. I will make a few adjustments to the plant model and plant form to ensure consistency with the user stories. Also, I will populate all of the HTML files required for this sprint once the base HTML file is done.
* Do I see any impediment that prevents me from making progress?
  * Yes, nothing can be tested so the code being developed could be buggy and cause an impediment today and tomorrow.

Overall Notes:

* It is still difficult to coordinate features pushes because of everyone's busy schedules during our fall break.
* The group is struggling to keep up with and remember all of the stakeholders' requirements alongside the user story requirements.

## 11/24/25-15:00

Participants: Andrew and Mckenna

Andrew:

* What did I do yesterday to help the team?
  * Yesterday I wrote the project overview.
* What will I do today to help the team?
  * Today I tested User Stories 1–3 (signup, login, seller dashboard) and updated the UML files to match our current models. I also verified the competitor listings' logic on the seller dashboard.
* Do I see any impediment that prevents me from making progress?
  * I don't see anything stopping me from continuing work today.

Mckenna:

* What did I do yesterday to help the team?
  * I worked on decomposing some functions in the project, ensuring everything was following PEP-8 standards, populated all the HTML files needed for this sprint, and I updated the objects required for creating a plant.
* What will I do today to help the team?
  * Today I will test all the user stories with Docker, I will proof the user stories, update the class diagram to better match the project direction, and I will plan for tomorrow's sprint meetings.
* Do I see any impediment that prevents me from making progress?
  * No, everything has been going well.

Overall Notes:

* We are on track to finish sprint one a day earlier than expected.
* The team hopes implementing deployment early will make it easier to test against the project requirements.

# Sprint Review

## 11/25/25-13:00

Participants: Andrew, Kobe, and Mckenna

Notes/Topics Discussed:

* Project overview accurately describes the project and was well written.
* User stories have been proofed and contain clear acceptance criteria.
* Development process notes area has been populated and contains a good summary of the sprint.
* The manual tests performed helped create a project test paper trail.
* The diagrams are easy to read and accurately depict the project's models, use case scenario, and functionality.
* Final walkthrough of user stories one, two, and three was successful and showed all acceptance criteria were met.
* The final walkthrough included three users: two horticulturists and one customer.
* The final walkthrough also showed the team that the web application not only functions well, but is visually appealing.
* User story one, user registration is considered done.
* User story two, view plant inventory was fully tested with user story three and is considered done.
* User story three was deemed done as well.
* With all the three user stories done, six user story points were spent this sprint.
* Testing deployment went smoothly even though only three user stories have been implemented.

# Sprint Retrospective

## 11/25/25-13:15

Participants: Andrew, Kobe, and Mckenna

#### What went wrong:

Andrew:

* Not being on the public repository caused a delay in getting my work to the rest of the group.

Kobe:

* Nothing went wrong for me during this sprint.

Mckenna:

* It took too much time to gather and refine the user stories. This caused a delay in the project because we could not get started until the notes were properly compiled in the README.
* Additionally, no one was able to access the public repository until two days into the sprint which also caused a development delay.

#### What can improve for the next sprint:

* Pay close attention to both our requirements (user stories) and the primary stakeholders' requirements for the entire project.
* Work on better communicating user stories, notes, and actions related to the repository.
