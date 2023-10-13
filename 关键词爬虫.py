import requests  
from bs4 import BeautifulSoup  
  
# Define the URL of the e-commerce website and the keyword to scrape  
url = 'https://www.example.com'  
keyword = 'product'  
  
# Send a GET request to the website and parse the HTML using BeautifulSoup  
response = requests.get(url)  
soup = BeautifulSoup(response.text, 'html.parser')  
  
# Find all the products on the website that contain the keyword  
products = soup.find_all(class_='product-list')  
for product in products:  
    name = product.find(class_='product-name').text  
    if keyword in name:  
        print(name)
