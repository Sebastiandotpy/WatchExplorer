import os
import django
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from webdriver_manager.chrome import ChromeDriverManager
import time
from datetime import datetime
from pytz import timezone

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'WatchExplorer.settings')
django.setup()

from watchlist.models import WatchData, Category

def scrape_watch_data():
    # Create a new instance of the Chrome driver
    driver = webdriver.Chrome(ChromeDriverManager().install())

    # Navigate to the URL
    url = "https://www.watchrecon.com"
    driver.get(url)

    try:
        # Wait for the page to load completely (you can adjust the sleep duration if needed)
        time.sleep(5)

        # Find all gallery item containers
        gallery_items = driver.find_elements("css selector", ".galleryItemContainer.med")

        print("Number of gallery items:", len(gallery_items))

        count = 0
        for item in gallery_items:
            if count >= 5:  # Limit to 5 entries
                break

            print("---")
            # Extract the title
            title_element = item.find_element("css selector", ".subjectInfo a")
            title = title_element.text.strip()
            print("Title:", title)

            # Extract the brand
            brand_element = item.find_element("css selector", ".brandInfo a")
            brand = brand_element.text.strip()
            print("Brand:", brand)

            # Extract the model
            try:
                model_element = item.find_element("css selector", ".modelInfo a")
                model = model_element.text.strip()
            except NoSuchElementException:
                model = ""
            print("Model:", model)

            # Extract the price
            try:
                price_element = item.find_element("css selector", ".priceInfo")
                price = price_element.text.strip()
            except NoSuchElementException:
                try:
                    price_element = item.find_element("css selector", ".listing__tag.listing__tag--sell")
                    price = price_element.text.strip()
                except NoSuchElementException:
                    price = ""
            print("Price:", price)

            # Get the current date and time with time zone information
            current_datetime = datetime.now(timezone('Europe/Berlin'))

            # Convert the datetime object to the desired format
            post_date = current_datetime.strftime("%Y-%m-%d %H:%M:%S")

            # Extract the source
            source_element = item.find_element("css selector", ".sourceInfo")
            source = source_element.text.strip()
            print("Source:", source)

            # Extract the user name
            user_name_element = item.find_element("css selector", ".userNameInfo a")
            user_name = user_name_element.text.strip()
            print("User Name:", user_name)

            # Fetch the category by name
            category_name = "Watch datas"  # Replace with the actual category name
            try:
                category = Category.objects.get(name=category_name)
            except Category.DoesNotExist:
                category = None

            # Create an instance of WatchData model
            watch_data = WatchData(
                title=title,
                brand=brand,
                model=model,
                price=price,
                post_date=post_date,
                source=source,
                user_name=user_name,
                category=None
            )

            # Save the watch data
            watch_data.save()

            count += 1

    except NoSuchElementException as e:
        print("Element not found:", e)

    # Close the browser
    driver.quit()

# Call the scrape_watch_data function to test it
scrape_watch_data()
