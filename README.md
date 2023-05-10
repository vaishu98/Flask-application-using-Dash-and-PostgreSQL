# Flask-Dash Stock Dashboard

This project is a stock dashboard built using Flask and Dash, allowing users to view and analyze the price of stocks over time. The dashboard displays four graphs on the landing page, each representing the price of a different stock. Users have the option to select the date and time range for each graph, providing flexibility in data exploration.

## Technical Details
The following are the technical details and requirements to run the project successfully:

### Framework: 
The application is built using Flask, a popular Python web framework, and Dash, a Python framework for building analytical web applications.

### Database: 
PostgreSQL is used as the database system for storing stock data. The project includes a Docker image that starts a PostgreSQL service.

### Docker: 
The entire application is packaged into a Docker image, which includes the code to start the PostgreSQL service and perform necessary setup tasks.

### Initialization: 
After the PostgreSQL service becomes up and running, a bash script is executed to create a username and database as specified in the local.env file. SQL scripts are then executed to create the necessary schema and insert some dummy data.

### Real-Time Data: 
The application supports real-time data updates by polling data into the PostgreSQL database. This allows users to view and analyze up-to-date stock information.

### Dependencies: 
All required Python packages are listed in the requirements.txt file. These packages need to be installed for the Flask application to run successfully.

## Getting Started

To run the project locally, follow the steps below:

**1. Clone the Repository:** Start by cloning this repository to your local machine.

**2. Move to Project Directory:** Open a terminal and navigate to the project directory.

**3. Build and Start Containers:** Run the following command to build the Docker image and start the containers:

`docker-compose up --build`

This command will start the Flask application container and the PostgreSQL database container.

**4. Access the Dashboard:** Once the containers are up and running, open a web browser and navigate to localhost:8888/ to access the stock dashboard.

**5. Explore and Analyze Data:** On the landing page, you will see four graphs representing the price of different stocks over time. Use the date and time range selectors to customize the data displayed on each graph. You can also explore real-time data by allowing the application to poll and update the database.

## Customization and Configuration
If you wish to customize or configure the project, you can make changes to the following files:

* **main.py:** This file contains the main Flask application code, including the Dash layout and callbacks. Modify this file to change the structure and behavior of the stock dashboard.

* **local.env:** Update this file to specify the desired username and database for PostgreSQL. Make sure to reflect these changes in the bash_script.sh file as well.

* **bash_script.sh:** Adjust this script to include any additional setup tasks or configurations you require for the PostgreSQL service or database.

* **stock1.sql, stock2.sql, stock3.sql, stock4.sql**: Modify this SQL scripts to define the database schema and tables according to your specific needs. You can have all the sql commands in a single file for convenience.

* **requirements.txt:** Add or remove Python packages in this file based on your project's dependencies.

## Contributing
If you would like to contribute to this project, please follow these guidelines:

1. Fork the repository and clone it to your local machine.

2. Create a new branch for your features or bug fixes:
`git checkout -b my-new-feature`

3. Make the necessary changes and commit them:
`git commit -am 'Add some feature`

4. Push the changes to your branch:
`git push origin my-new-feature`

5. Submit a pull request, describing your changes and improvements. Be sure to include relevant details and any necessary documentation updates.