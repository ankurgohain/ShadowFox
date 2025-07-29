# import requests as req
# from bs4 import BeautifulSoup as bs

# res = req.get('https://petrolicious.com/blogs/articles/')
# # soup = bs(res.content, 'html.parser')
# print(res.status_code)

# print(res.content)
# # content_div = soup.find('div', class_='article--viewer_content')
# # if content_div:
# #     for para in content_div.find_all('p'):
# #         print(para.text.strip())
# #     else:
# #         print("No content found in the specified div.")

import requests
from bs4 import BeautifulSoup

def sraper(url):
    resp = requests.get(url)
    resp.raise_for_status()
    soup = BeautifulSoup(resp.text, 'html.parser')

    # Title
    title_el = soup.find('h1')
    title = title_el.get_text(strip=True) if title_el else None

    # Author and date
    byline = soup.select_one('byline, .author, .publish-date')
    author = byline.get_text(strip=True) if byline else None

    # Introductory paragraph
    intro = soup.select_one('.article-intro, p')
    intro_text = intro.get_text(strip=True) if intro else None

    # All paragraphs
    paras = soup.find_all('p')
    text = '\n\n'.join(p.get_text(strip=True) for p in paras)

    return {
        'title': title,
        'author': author,
        'intro': intro_text,
        'content': text,
    }

if __name__ == '__main__':
    url = 'https://www.mentalfloss.com/food/british-dish-name-origins'
    data = sraper(url)
    print(data['title'])
    print('By:', data['author'])
    print('\nIntro:', data['intro'])
    print('\n--- Full content excerpt ---\n')
    print(data['content'][:5000] + '...')
