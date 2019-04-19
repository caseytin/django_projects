# TMD Study Spots

## Assignment Overview

This is a collaborative final project for SI 364: Building Interactive Applications. Project members include Casey Tin, Carrington Tubman, Verity Sturm, and Eli Lustig. This project follows certain requirements, as listed below:

* The project must be a web site that can be accessed and viewed.
* The project must have at least six data models (i.e. tables)
* The project must have at least three Many-to-One relationships between models and at least one Many-to-Many relationship
* The project must have a feature for end-users to log in. This can be using the internal Django authorization with manually created accounts or use a social login from one or more of the common providers (Github, Google, Twitter, Facebook, etc).
* The project must have at least one example of data coming into the site from users. This could be as simple as a comment or ranking capability or you could build a completely social site intended to be built by the crowd.
* The project is intended to have a nice graphic design - it does not have to be stunning but it also not be default browser with Times New Roman font on a white background


## Project Details

TMD Study Spots will be under the ownership of [The Michigan Daily](https://michigandaily.com), and will be an ongoing project. For the purposes of the final project deadline, we are looking to create a MVP (minimum viable product) and continue to add functionality/scalability accordingly. 

The basis of this project comes out of the desire to create a long-lasting product for The Michigan Daily that also adheres to our final project guidelines for SI 364. This site will function primarily as a rating system for on-campus and off-campus study spots at the University of Michigan. For users without user accounts, the ability to search for a study spot through predetermined filters will be available. User interaction with the site will be enabled through the ability to leave comments and review study spots, given that the current user is logged-in. Logged-in users will also have the ability to update photos and features of existing study spots, or create new study spot postings.

Our six data models that fulfill the criteria of the final assignment include study spot features, photos for each study spot, location of each study spot, rating of each study spot, user comments, and all users. (NOTE: some of these will be modified/removed upon iteration of our MVP.)

## Installation Requirements
* `python3`
* `django 2.1.7`
* `HTML5/CSS3`

## Starting the application
TBD!

## Routes
* `/` ==> `index.html`
* `/admin` ==> `admin.html` (ADMIN USERS ONLY)
* `/login` ==> `login.html`
* `/logout` ==> `logout.html`
* Rest is TBD!
