# Venmito Data Engineering Project

## Introduction
Welcome to the Venmito Data Engineering Project. Our goal is to leverage disparate data sources to uncover insights about our clients, their transactions, and how they interact with promotions. Venmito, a leading payment platform, seeks to enhance service delivery through a deeper understanding of user behavior and operational efficiency.

This project involves processing data from multiple formats—JSON, YAML, CSV, XML—matching and conforming this data to extract valuable insights.

## Requirements

### Data Ingestion
Your solution must read and load data from all provided files in their respective formats.

### Data Matching and Conforming
After loading, the solution should match and conform data across these files, resolving inconsistencies and organizing the data into a unified format. The conformed data should be persisted through suitable storage solutions to ensure its availability for future use and analysis.

### Data Analysis
The project requires processing the conformed data to derive insights on client interactions with promotions, transaction trends, and more. Specific analyses include:

- Client engagement with promotions.
- Insights on store performance and best-selling items.
- Financial flows from fund transfers.

### Data Output
The output should present the analyzed data in a consumable format, potentially through a CLI, database, interactive GUI, Jupyter Notebook, or RESTful API.

## Getting Started

### Prerequisites
- Python 3.8+
- Jupyter Notebook

### Installation
To set up your environment:
```bash
git clone https://github.com/yeahsuredude/Venmito-Data_Engineering-Project.git
cd venmito-data-project
pip install -r requirements.txt
```

## Usage
Navigate to the project directory and start Jupyter Notebook:
```bash
jupyter notebook
```

Open `data_analysis.ipynb` for a walkthrough of data processing and analysis.

## Project Structure
- `people_data.py`: Processes people data.
- `data_ingestion.py`: Ingests transaction, transfer, and promotion data.
- `persistence.py`: Handles data persistence.
- `data_analysis.ipynb`: Interactive notebook for analysis.

## Contributing
Contributions are welcome! Please fork the repository and submit pull requests for review.

## License
This project is licensed under the MIT License - see LICENSE.md for details.

## Acknowledgements
Thanks to all contributors and the Venmito team for their support.

## Contact
For inquiries, please contact Jonathan Mena at jonmena7@gmail.com.

## Disclaimer
This project is provided "as is", without warranty of any kind. It is intended solely for evaluation and educational purposes. Unauthorized distribution or use is prohibited. By using this project, you agree to abide by these terms.
