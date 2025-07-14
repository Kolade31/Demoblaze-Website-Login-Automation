# Demoblaze Selenium Login Automation

The Demoblaze Selenium Login Automation project aims to simplify the login process for the Demoblaze website using the Selenium WebDriver. This project is particularly useful for automating testing scenarios in web applications, allowing developers and testers to efficiently verify login functionalities without manual intervention.

## Features
This project offers several key features. First and foremost, it automates the login process, allowing users to log in to the Demoblaze platform seamlessly. Additionally, the project includes robust unit tests that evaluate both successful and unsuccessful login attempts. This ensures that the login functionality works as intended, providing a reliable user experience. The modular design using classes enhances maintainability, making it easy for developers to update or expand the project's capabilities.

## Requirements
To set up the project, users need to have Python(latest version) installed on their systems. Furthermore, the Selenium library is required for web automation tasks, which can be easily installed via pip. Additionally, users must download the Chrome WebDriver or any other WebDriver compatible with their browser version. This WebDriver acts as a bridge between the Selenium script and the web browser, enabling automated interactions.

## Setup Instructions
Setting up the Demoblaze Selenium project involves a few straightforward steps. First, users should clone the repository from GitHub and navigate to the project directory. Afterward, they must install the required packages, specifically the Selenium library, using pip. Following this, it is crucial to download the Chrome WebDriver that matches the version of the Chrome browser being used. Once downloaded, users should place the WebDriver in a directory that is accessible by the system. Finally, they must update the WebDriver path in both the main.py and test_demoblaze.py files to ensure proper execution of the scripts.

## Running the Tests
To verify that the login functionality works as expected, users can run the automated tests included in the project. This can be accomplished by executing a simple command in the terminal. The unit tests will assess the login process, ensuring that valid credentials lead to a successful login while invalid credentials result in appropriate error messages.

## Generating Reports
Reports will be generated automatically in the reports/ directory after running the tests. You can open report.html in a web browser to view detailed results.

## Project Structure
The project is organized into a clear directory layout that enhances usability. The login_page.py file contains the LoginPage class, which encapsulates the login logic. The test_demoblaze.py file serves as the entry point to execute the login process. This organization facilitates easy navigation and understanding of the project's components.

## Conclusion
In summary, the Demoblaze Selenium Login Automation project provides a valuable tool for automating the login process on the Demoblaze website. With its focus on reliability and maintainability, this project serves as an excellent foundation for further development and enhancement in web automation testing. By following the setup and usage instructions outlined above, users can effectively harness the power of Selenium to streamline their testing processes.

