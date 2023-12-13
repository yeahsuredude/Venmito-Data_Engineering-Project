# Venmito Data Engineering Project

## Introduction

Hello and welcome to this data engineering project for Venmito. We're excited to see how you tackle this challenge and provide us with a solution that can bring together disparate data sources into an insightful and valuable resource.

Venmito is a company with several data files in various formats. Our goal is to organize all of this information to gain insights about our clients and transactions. We believe that there is an immense value hidden in these data files, and we are looking for a solution that can help us extract and utilize this value.

We have five files:

- `people.json`
- `people.yml`
- `transfers.csv`
- `transactions.xml`
- `promotions.csv`

Each of these files contains different pieces of information about our clients, their transactions, transfers and promotions.

Your task is to develop a solution that can read these files, match and conform the data, and provide a way to consume this data.

## Requirements

1. **Data Ingestion**: Your solution should be able to read and load data from all the provided files. Take into account that these files are in different formats (JSON, YAML, CSV, XML).

2. **Data Matching and Conforming**: Once the data is loaded, your solution should be able to match and conform the data across these files. This means identifying common entities, resolving inconsistencies, and organizing the data in a unified format.

3. **Data Analysis**: Your solution should be able to process the conformed data to derive insights about our clients and transactions. This would involve implementing data aggregations, calculating relevant metrics, and identifying patterns. These insights will be invaluable in helping us understand our clientele and transaction trends better.

4. **Data Output**: The final output of your solution should enable us to consume the reorganized and analyzed data in a meaningful way. This could be, but is not restricted to, a command line interface (CLI), a database with structured schemas, a GUI featuring interactive visualizations, or a RESTful API. We invite you to leverage other innovative methods that you believe would be beneficial for a company like Venmito.

5. **Code**: The code for your solution should be well-structured and comprehensible, with comments included where necessary. Remember, the quality and readability of the code will be a significant factor in the evaluation of the final deliverable.

Note: The examples provided in these requirements (such as GUI, RESTful API etc.) are purely illustrative. You are free to employ any solution or technology you deem fit for fulfilling these requirements

## Deliverables

1. Source code.
2. A README file that describes your solution, your design decisions, and clear instructions on how to run your code.
3. A method to consume the reorganized and analyzed data.

## Venmito Needs:

We want to be able to see:
1. Which clients have what type of promotion?
2. Give suggestions on how to turn "No" respones from clients in the promotions file?
3. Insights on stores, like:
    - What item is the best seller?
    - What store has had the most profit?
    - Etc.
- **Bonus**:
    - How can we use the data we got from the transfers file?

## Instructions for Submission

1. Complete your project as described above within your fork.
2. Write a detailed README file that explains your approach, the technologies you used, and provides clear instructions on how to run your code.
3. Submit your project by creating a pull request to this repository.

We look forward to seeing your solution!

Thank you,

Venmito

## DISCLAIMER:

This project and its contents are the exclusive property of Xtillion, LLC and are intended solely for the evaluation of the individual to whom it was provided. Any distribution, reproduction, or unauthorized use is strictly prohibited. By accessing and using this project, you agree to abide by these conditions. Failure to comply with these terms may result in legal action.

Please note that this project is provided "as is", without warranty of any kind, express or implied. Xtillion is not liable for any damages or claims that might arise from using or misusing this project.
