![Brand Image](https://i.postimg.cc/kgPFx4cP/Screen-Shot-2020-03-23-at-12-43-12-PM.png)

# Conscious Consumer
![Travis CI Build](https://travis-ci.com/UPstartDeveloper/conscious-consumer.svg?branch=master) ![Docker Image Size](https://img.shields.io/docker/image-size/zainrazatheupstart/conscious_consumer/latest)

Fitbit for living a green life. [See it Now.](https://consciousconsumer.herokuapp.com)

## Table of Contents
1. [The Why](#the-why)
2. [Getting Started](#getting-started)
    - [Prerequisites](#prerequisites)
    - [Forking this Repository](#forking-the-repository)
    - [Installing Requirements](#installing-requirements)
    - [Run the Project Locally](#run-the-project-locally)
3. [Running the Tests](#running-the-tests)
4. [Technologies Used](#technologies-used)
5. [Navigating the Project](#navigating-the-project)
6. [How to Contribute](#how-to-contribute)
7. [License](#license)
8. [Release Schedule](#release-schedule)
9. [Acknowledgements](#acknowledgements)

## The Why
[Conscious Consumer](https://consciousconsumer.herokuapp.com) is a website that everyday people use to track their carbon footprint. Let's face it: have you stopped to wonder what the cost is to the environment, every time you emit carbon into the atmosphere?

Carbon is a resource just as valuable as our personal health, or the our financial resources. Just like those resources, it carries a heavy cost if taken in excess.

If we're willing to make budgets for our weight to preserve our health, and our spending to preserve our wealth, then it's time we do the same for our carbon, to preserve the health of our environment and the value of this planet we call home.

Please take a look at the following for more context around the idea behind the [Conscious Consumer](https://consciousconsumer.herokuapp.com) project:
- [Slide Deck](https://docs.google.com/presentation/d/1wwWKidDJWLG8-76DlfuFllWm_-uxG6_qBJTMm3xahig/edit?usp=sharing)
- Technical Write-Up (Coming Soon, date TBD)

## Getting Started
### Prerequisites
- Must have Git installed
- Must have a GitHub account
- Must have Python 3.7.* installed
- Must know how to work in a [Python virtual environment](https://realpython.com/python-virtual-environments-a-primer/)

### Forking this Repository
If you would like to improve this project in some way (much appreciated!), then please follow these steps to fork the repository:
1. Fork this repository (click the "Fork" button at the top right of the page, then click on your profile image).
- Clone your forked repository onto your local machine
```
git clone https://github.com/<YOUR_GITHUB_USERNAME>/conscious-consumer.git
```
- Start your virtual environment, and be sure to see the 'Installing Requirements' section below to make sure you have all the required dependencies!

- Create a new branch for the feature you want to work on, or the bug fix you want to make:
```
git checkout -b feature/branch-name or bugfix/branch-name
```
- Make your changes (be sure to commit and push!)
```
git add .
git commit -m "[YOUR COMMIT MESSAGE HERE]"
git push origin branch-name
```

### Installing Requirements

Start by forking this repository (button is in the top right), and then clone your version onto your local machine.

Before anything else - *be sure to start a virtual environment!*

Once you have activated your Python virtual environment, please be sure to run the following command from the command line, to ensure you have all the dependencies
you may need to use for this project:
```
python -m pip install -r requirements.txt
```
You may always double check the dependencies you have using this command:
```
python -m pip list
```
If you install any new dependencies, please be sure to record them! While in the ```conscious_consumer/``` directory, run the following command:
```
python -m pip freeze > requirements.txt
```
Thank you in advance for contributing to this project!
### Run the Project Locally

**Option 1**: Using `virtualenv`

From the same ```conscious_consumer/``` directory, you can run this project locally using the following command:

```
    python manage.py runserver
```

There is much more to the Django framework for Python - if you are ensure of how to do something for the backend of this project, be sure to refer to the stellar [Django documentation](https://docs.djangoproject.com).

**Option 2**: Using Docker

#### Prerequisites:

Make sure you have the latest version of [Docker](https://www.docker.com/get-started) installed. If you are not on macOS or experience any trouble installing Docker Compose, check out the [Docker documentation](https://docs.docker.com/compose/install/).

#### Instructions

1. Once you have done so and have also cloned the repository locally, you can run the project using `docker-compose` in the root directory:

    ```
        docker-compose up --build
    ```

2. Then you can view the project at [http://localhost:8000](http://localhost:8000).

You can also open up Docker Desktop, and view the health of the `conscious_consumer` container on a panel that will look something like below:

![Screenshot from Docker Desktop](https://i.postimg.cc/C1x2fwJM/Screen-Shot-2020-11-27-at-11-30-06-AM.png)

## Running the Tests
Be sure that your virtual environment is activated.

#### For the Whole Project
In the outer conscious_consumer/ directory where ```manage.py```, run the following command to evaluate the automated tests for this project:
```
python manage.py test
```
Observe the output to determine whether your version of this project fails or passes.

#### For a Single App
If you are interested in running the tests associated with only a single app in the project, you can run the same command as above, and then at the end include the name of the specific app as well.

There are currently three Django apps in this project. They are referenced from the command line as follows:
- ```accounts```
- ```budget```
- ```store```
Therefore as an example if I wanted to check the tests related to just the ```budget``` app, the command I would enter is the following:
```
python manage.py test budget
```
If at any point you have trouble analyzing tests, feel free to look inside the ```tests.py``` module in each of the above app directories.

## Technologies Used
- Django - web framework for the backend
- Bootstrap 4 - styling the front end
- PostgreSQL - production database schema
- Django REST Framework - framework building the API (found in the [conscious_consumer.api package](conscious_consumer/api/)).
- AWS S3 - cloud storage for image uploads
- Chart.js - data visualizations using Javascript and JSON
- Heroku - deployment on a production server

## Navigating the Repository
This repository follows the [Django framework](https://docs.djangoproject.com) for making full-stack web applications.
All the code is found in the outer ```conscious_consumer``` directory, because that is the folder for the overall Django project.

There are a few important things to note about the inner directories of this folder:
1. **Apps in Django**: By convention, these subdirectories of ```conscious_consumer``` are also referred to as "apps" in the Django framework. There are several apps in this project, so here is a brief overview of what each of them are, and what their use is (so you know why you may ever want to look inside them):
- ```accounts```: everything related to authentication and user profiles.
- ```api```: creates a RESTful endpoint, to retrieve information about users' ```Goal``` instances. Used in creating data visualizations on the front-end.
- ```budget```: everything related to creating carbon budgets for the user.
- ```static and staticfiles```: all custom CSS, images, and Javascript files used in the project go here. If you add any new static files, you need only to upload them to the ```staticfiles``` directory. In production AWS S3 will be used to deploy static files.
- ```store```: everything related to users finding and connecting with green products and services that help them become more environmentally conscious.
- ```templates```: all HTML files applied to the project as a whole, and not specific to any of the above packages (i.e. the landing page is saved here as```index.html```).
- ```conscious_consumer```: in what may seem strange to Django-beginners, there is also an innner-directory named ```conscious_consumer```! Remember that the project governs over the apps in Django; so this package stores all Python modules pertaining to the project as a whole, not any one specific app. For example, you will find the all-important ```settings``` package in this directory, where you will be able to configure important project settings such as the database used, the URL configuration, static file storage, and more.
2. **Imports**: all of the subdirectories of the outer ```conscious_consumer``` directory are the equivalent of Python packages. In turn, this means an individual Python script in one of these subdirectories (i.e. ```conscious_consumer/budget/models.py```) is the equivalent of a Python module. This means you will need to use the dot operator(.) when importing objects between these scripts.
3. **MVC Architecture**: so you think you're ready to work with apps in Django? Not so fast - read this first if you're new to Django, so you know what each of the main files in the app directories (outlined above) actually mean. Remember you can also always refer back to the [Django documentation](https://docs.djangoproject.com) for more clarification. If you first need to learn what MVC Architecture is conceptually, please look at [this superb explanation on Real Python](https://realpython.com/the-model-view-controller-mvc-paradigm-summarized-with-legos/).

- *Models in Django*: refer to the ```models.py``` module, which outlines the database schema for the feature related to that specific package, and is implemented using the principles of Object-Oriented Programming.
- *Views in Django*: for this, look in the ```urls.py``` module. It contains the URL patterns for the views a user may request from the site.
- *Controllers in Django*: refer to the ```views.py``` module, which contains the code that programs the server to respond to the requests made by the client.

Also, in each of the app subdirectories you will find a ```templates/``` subdirectory, which you may refer to so you can see the HTML used to render each of the views specific to a particular app. Template inheritance is used to reduce the number of HTML files needed - the base template is found in ```conscious_consumer/templates/base.html```.

## How to Contribute
When you are ready to push the branch of your forked repo, please make the following edits to the list on the [CONTRIBUTORS.md](CONTRIBUTORS.md) file. You can use the snippet of Markdown code to get you started. Be sure to leave personalized responses in between wherever you see <>.
```
**<list item number>. <Your Name> **, *<brief description of how you helped this project>
- **Description**: <personal description about yourself>
- **Location**: <where you currently reside>
- **Fun Fact**: <what do you think most people don't know about you?>
- **Find Me**: <[YOUR_NAME](Link to your GitHub Account, social media, or other personal link)>
```
Once you have pushed your branch, go to your fork on GitHub and open a pull request. The team will then evaluate it to see if it can be merged. If not, we will give you feedback explaining why.

Note that although highly suggested, you are not required to add a fun fact or a link to your entry in the contributors file. Thanks for helping out!

## License
This repository is completely open-source, and carries the MIT license. Please see [LICENSE](LICENSE) for more details.

## Release Schedule
Please see [Releases.md](Releases.md) for details on version history. Includes the features included in each release, and the date on which that release was launched.

## Acknowledgements
1. Earth icon made by [Freepik](https://www.flaticon.com/authors/freepik) on [Flaticon](https://flaticon.com/).

2. [User icon](https://www.flaticon.com/free-icon/male-user-shadow_16480) by [Freepik](https://www.flaticon.com/authors/freepik) from [Flaticon](https://www.flaticon.com/).

3. Products found through Phil Sturgeon's [Awesome Earth](https://github.com/philsturgeon/awesome-earth#footprint-calculators) open-source project on GitHub.

4. Photos on home page come from the following creators on Unsplash:
- Drone picture by [Tyler Casey](https://unsplash.com/@tylercaseyprod)
- "Empower" image by [Kelly Sikkema](https://unsplash.com/@kellysikkema)
- Background image by [Benjamin Suter](https://unsplash.com/@benjaminjsuter)

5. Lastly, a big thank you goes to Mom and Dad - thanks so much for your supporting me throughout my time at Make School! - Zain, *March 23, 2020*
