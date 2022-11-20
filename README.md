# Finance Tracker

Video Demo: <https://youtu.be/lcYxGyE4bUM>

## About

Finance is a web application to track and monitor your expenditure. You can add financial transactions and the app shows visual representation of your expenditure history.

#### How to use

> You can use navigation bar to switch between pages

* If you are not already logged in, the application prompts you to login. If you don't have a id, you can register by clicking register in the navigation bar
* The __home__ page shows you a visual representation of you'r expenditure history
* The __history__ page shows you your transaction history
* You can click on __add__ in the navigation bar to add a transaction
* You can click on __Sign Out__ on navigation bar to log out.

### Technologies used

> Vue, Vuetify, Flask, SQLAlchemy

___

## Technical Overview

The app is divided into 2 modules, frontend and backend.

* ### __Frontend__

  Frontend contains all the user side codes and modules executed and displayed on the user's devices. The web pages of the site is served by the front server where a page can fetch data from backend using HTTP requests. The various frameworks and libraries used in frontend is detailed below

  * #### __Vue__

    Vue is a front end javascript framework for building user interfaces and single-page applications. Vue builds on top of _html_, _css_ and _javascript_ ans allows to make self contained reusable components for different parts of our page(like form, navigation bar). Vue also comes with different modules as part of its ecosystem like router(used to seamlessly switch between diffrent pages), vuex(used to manage and share state and data between diffrent components and pages).
  
  * #### __Vuetify__

    Vuetify is a component framework for Vue which provides pre-made components(like bootstrap) for us to use in a webpage. Using vuetify eliminated the need to write plain html and css for every component of my webapp.

  * #### __Axios__

    Axios is a HTTP client for Javascript which enables us to make HTTP requests from the browser and handle the transformation of request and response data. This connected the frontend component of my app with the backend as the frontend was now able to request and fetch data from the backend.

  * #### __Chart.js__

    Chart.js is a javascript library for data visualization which enabled me to make different charts in my application like bar chart, pie chart, line chart etc.

* ### __Backend__

  Backend contains all the server side codes and modules which does'nt run on user's device but the user/application(frontend) can communicate with the backend using HTTP requests. Backend receives requests from frontend and provides relevent data/output which the frontend can display to the user. The various frameworks and libraries used in backedn are detailed below.

  * #### __Flask__

    Flask is a web framework for python. Which flask can dynamically serve whole webpages but here it is used just to serve data to the frontend of our application in the form of JSON.

  * ### __SQLAlchemy__

    SQLAlchemy is a SQL toolkit for python. Using SQLAlchemy, rows in a SQL table can be represented as a python class which makes it easier to read and write from SQL Databases.

  * ### __PyJWT__

    PyJWT is a Python library which allows you to encode and decode JSON Web Tokens (JWT). JWT is an open, industry-standard for representing claims securely between two parties. I used JWT for user authentication which is touched on later.

___

Some aspects of the program is detailed below
> Below I will be referencing frontend as application and backend as server

* ### __User Authentication__

  >User authentication is done here using JSON Web Tokens (JWT). The token is just a JSON object which contains the data to be shared and a digital signature signed by a key(here the key holder may be the creater/host of the application). The signature of the token can be verified by the key holder and cannot be forged without the key.

  When logging in with the app, server provides a signed token with some expiry date which the app then stores in local storage. Now with every request with the server, the app also sends the token as a header which the server can verify and provide relevent output. If the token is not valid, expired or the token is not present, the server provides a HTTP error 401, after which the app prompts user to log in again.

* ### __Database__
  
  It required two database tables for this application.

  * A table __user__ to store user information. This has 5 columns: id, public_id, username and password
  * A table __history__ to store user transaction history. This has 5 columns: id, category, amount, description, date_time and user_id

* ### __Data Visualization__

  There are two carts in the home page.

  * __Bar Graph__:
    The bar graph visualizas the user's expenditure trend over the current month and also provides the month's total
  * __Pie Chart__:
    The pie chart visualizes the user's total expenditure in every category with respect to the total expenditure
