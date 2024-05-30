import requests
from bs4 import BeautifulSoup
import pandas as pd

USER_AGENT = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36'
Result = []
M_Name = []
M_Year = []
M_Rating = []
try:
    headers = {'user_agent': USER_AGENT}
    resp = requests.get("https://www.imdb.com/chart/top/", headers=headers)
    print(resp.status_code)
    soup = BeautifulSoup(resp.text, 'html.parser')
    # print(soup)
    Movies_detail = soup.find('ul', class_='ipc-metadata-list ipc-metadata-list--dividers-between sc-a1e81754-0 eBRbsI compact-list-view ipc-metadata-list--base')
    Movies_detail = Movies_detail.find_all("li")
    # print(Movies_detail)
    # for i in Movies_detail:
    #     M_Name.append(i.text)
    # print(len(M_Name))

    for i in Movies_detail:
        M_Name.append(i.find('div', class_='ipc-title ipc-title--base ipc-title--title ipc-title-link-no-icon ipc-title--on-textPrimary sc-b189961a-9 iALATN cli-title').a.text.split('.')[1])
    # print(len(M_Name))
    #     M_Name = M_Name.split('.')[1]
        # Result.append(M_Name)
        M_Year.append(i.find('span', class_='sc-b189961a-8 kLaxqf cli-title-metadata-item').text)
        # print(M_Year)
        # Result.append(M_Year)
        M_Rating.append(i.find('span', class_='ipc-rating-star ipc-rating-star--base ipc-rating-star--imdb ratingGroup--imdb-rating').text.split('(')[0])
        # M_Rating = M_Rating.split('(')[0]
        # print(M_Rating)
        # Result.append(M_Rating)


    # print(Result)
except Exception as e:
    print(e)
print(len(M_Name),len(M_Year),len(M_Rating))
df = pd.DataFrame({'Movie_Name': M_Name, 'Movie_Year': M_Year, 'Movie_Rating': M_Rating})
df.to_csv("IMDB_TOP_200_Movies.csv",index = False)

