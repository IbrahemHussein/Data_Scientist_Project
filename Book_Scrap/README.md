# Web Scraping Project: Books to Scrape

![Books to Scrape Logo](https://fiverr-res.cloudinary.com/images/t_main1,q_auto,f_auto,q_auto,f_auto/gigs/145986054/original/925fe62a845bc86dd7b8bb9f14a22a47372726f7/do-web-scraping-and-logo-design.jpeg) <!-- Add a relevant image if available -->

## 📖 Overview
This project is a web scraper for [Books to Scrape](https://books.toscrape.com), a dummy website designed for practicing web scraping. The scraper extracts book details such as title, price, rating, and availability.

## 🚀 Features
- Scrapes all book categories.
- Extracts book details: title, price, rating, and availability.
- Saves data in a structured format (CSV/JSON).
- Handles pagination for multi-page categories.

## 🛠️ Technologies Used
- **Python**
- **BeautifulSoup** (for parsing HTML)
- **Requests** (for HTTP requests)
- **Pandas** (for data manipulation and export)

## 📂 Project Structure
project/
├── book_scrap.py #  script to scrap the info of the book
├── loop_book.py #  script to scrap all book of website
├── loop_book.py #  script to downloud the image of book
├── requirements.txt # Dependencies
├── data/ # Folder for scraped data
│ ├── books.xlsx # Example output
│ ├── books.txt # image links
│ ├── book_image/ # contains image 
├── README.md # Project documentation
└── .gitignore # Files to ignore in Git

## 🛠️ Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/your-repo-name.git

2. Install dependencies:
    pip install -r requirements.txt

