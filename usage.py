from scraper import get_elements_data
import pandas as pd

url = "https://www.imdb.com/chart/moviemeter/"
element_xpath = "//ul[contains(@class, 'ipc-metadata-list')]/li//h3"
data_xpath = "./text()"

results = get_elements_data(url, element_xpath, data_xpath, scroll=False)
print(results)

for item in results:
    print(item)

df = pd.DataFrame(results)
df.to_csv("imdb_trending_movies.csv", index=False)
