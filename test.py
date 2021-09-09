import requests

r = requests.get("https://mangatx.com/wp-content/uploads/WP-manga/data/manga_5f082169c334b/5641ebf822cc7fadc63949668ad4b048/003.jpg")
print(r.status_code)
