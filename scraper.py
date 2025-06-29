
from playwright.sync_api import sync_playwright

def scrape_chapter():
    url = "https://en.wikisource.org/wiki/The_Gates_of_Morning/Book_1/Chapter_1"
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)  # Headless=False = opens browser visibly
        page = browser.new_page()
        page.goto(url)

        #  Wait for the content section to load
        page.wait_for_selector("#mw-content-text")

        #  Take screenshot
        page.screenshot(path="chapter1_screenshot.png", full_page=True)

        #  Extract chapter text
        content = page.inner_text("#mw-content-text")
        with open("chapter1_raw.txt", "w", encoding="utf-8") as f:
            f.write(content)

        print("Scraping complete! ")
        browser.close()

if __name__ == "__main__":
    scrape_chapter()
