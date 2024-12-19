# JobHive
 JobHive automates the process of finding job listings from popular job search websites such as Indeed, Mynimo, and JobStreet. With JobHive, you can specify your desired skills or job titles, location, and the number of pages to scrape, and it will collect relevant job opportunities for you. Say goodbye to manually browsing multiple websites for job openings — JobHive streamlines the job search process, saving you time and effort.

## Problem it Solves

Searching for job opportunities can be a time-consuming and daunting task, especially when you're looking across multiple websites. JobHive solves this problem by automating the process of finding job listings from various platforms. Instead of manually visiting each website and searching for jobs, JobHive allows users to specify their criteria once and scrape job listings from multiple websites in a single run. This saves time and effort, making the job search process more efficient and manageable.

## Motivation

As a CS Grad and job seeker, automating the process of finding job opportunities can be incredibly valuable. It allows me to focus my time and energy on other important tasks, such as honing my skills, working on personal projects, or preparing for interviews. By automating the job search process with JobHive, I can streamline the process of finding relevant job listings, stay organized, and increase my chances of discovering new opportunities that align with my skills and career goals.

## Features

- Scrapes job listings from Indeed, Mynimo, and JobStreet websites.
- Allows users to specify the skill or job title, location, and number of pages to scrape.
- Stores scraped job data in CSV files for further analysis or processing.

## Requirements

- Python 3.9
- Dependencies:
  - Selenium
  - BeautifulSoup4
  - Typer

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/jay01varma/JobHive.git
   ```

2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. Navigate to the project directory:

   ```bash
   cd JobHive
   ```

2. Run the main.py file:

   ```bash
   python main.py
   ```

3. Follow the prompts to specify the skill or job title, location, website, and number of pages to scrape.

    ``` bash
    python main.py --skill_name " " --location " " --site indeed/ --num_pages 3
    ```
## Contributing

Contributions are welcome! If you'd like to contribute to JobHive, please follow these steps:

1. Fork the repository.
2. Create your feature branch (`git checkout -b feature/YourFeature`).
3. Commit your changes (`git commit -am 'Add some feature'`).
4. Push to the branch (`git push origin feature/YourFeature`).
5. Create a new Pull Request.

Please ensure that your code adheres to the existing coding style and conventions.

## License

This project is licensed under the MIT License.

## Acknowledgements

- This project was inspired by the need for a convenient way to search and collect job listings from multiple websites.
- I am grateful to the open-source community for providing libraries and tools that made this project possible.

## Contact
Name: **Jay Dilip Varma**  
Email: jay01varma@gmail.com  
LinkedIN: [jay01varma](https://www.linkedin.com/in/connect-wtih-jay-varma/)
