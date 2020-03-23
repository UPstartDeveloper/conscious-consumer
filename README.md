![Brand Image](https://i.postimg.cc/kgPFx4cP/Screen-Shot-2020-03-23-at-12-43-12-PM.png)

# Conscious Consumer
Fitbit for living a green life.

## Table of Contents
1. [The Why](#the-why)
2. [Getting Started](#getting-started)
    - [Prerequisites](#prerequisites)
    - [Installing Requirements](#installing-requirements)
    - [Run the Project Locally](#run-the-project-locally)
3. [Running the Tests](#running-the-tests)
4. [Technologies Used](#technologies-used)
5. [How to Contribute](#how-to-contribute)
6. [License](#license)
7. [Release Schedule](#release-schedule)
8. [Acknowledgements](#acknowledgements)

## The Why

## Getting Started

### Prerequisites
### Installing Requirements
### Run the Project Locally

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

There are currently 3 Django apps in this project. They are referenced from the command line as follows:
- ```accounts```
- ```budget```
- ```store```
Therefore as an example if I wanted to check the tests related to just the ```budget``` app, the command I would enter is the following:
```
python manage.py test budget
```
If at any point you have trouble analyzing tests, feel free to look inside the ```tests.py``` module in each of the above app directories.

## Technologies Used

## How to Contribute
On the branch of your forked repo, please make the following edits to the list on the [CONTRIBUTORS](CONTRIBUTORS) file. You can use the snippet of Markdown code to get you started. Be sure to leave personalized responses in between wherever you see <>.
```
**<list item number>. <Your Name> **, *<brief description of how you helped this project>
- **Description**: <personal description about yourself>
- **Location**: <where you currently reside>
- **Fun Fact**: <what do you think most people don't know about you?>
```
Note that although highly suggested, you are not required to add a fun fact to your entry in the contributors file. Thanks for helping out!

## License
This repository is completely open-source, and carries the MIT license. Please see [LICENSE](LICENSE) for more details.

## Release Schedule
Please see [Releases.md](Releases.md) for details on version history. Includes the features included in each release, and the date on which that release was launched.

## Acknowledgements
Earth icon made by [Freepik](https://www.flaticon.com/authors/freepik) on [Flaticon](https://flaticon.com/).

[User icon](https://www.flaticon.com/free-icon/male-user-shadow_16480) by [Freepik](https://www.flaticon.com/authors/freepik) from [Flaticon](https://www.flaticon.com/).

Products found through Phil Sturgeon's [Awesome Earth](https://github.com/philsturgeon/awesome-earth#footprint-calculators) open-source project on GitHub.

Photos on home page come from the following creators on Unsplash:
- Drone picture by [Tyler Casey](https://unsplash.com/@tylercaseyprod)
- "Empower" image by [Kelly Sikkema](https://unsplash.com/@kellysikkema)
- Background image by [Benjamin Suter](https://unsplash.com/@benjaminjsuter)

Lastly, a big thank you goes to Mom and Dad - thanks so much for your supporting me throughout my time at Make School! - Zain, *March 23, 2020*
