from flask import Flask, request, jsonify
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)

@app.route('/search', methods=['GET'])
def search():
    query = request.args.get('query')
    if not query:
        return jsonify({'error': 'No query provided'}), 400

    # Google検索のURLを構築
    url = f"https://www.google.com/search?q={query}"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
    }

    # Google検索を実行
    response = requests.get(url, headers=headers)
    if response.status_code != 200:
        return jsonify({'error': 'Failed to retrieve search results'}), 500

    # BeautifulSoupを使って検索結果を解析
    soup = BeautifulSoup(response.text, 'html.parser')
    results = []
    for g in soup.find_all('div', class_='BVG0Nb'):
        title = g.find('h3').text if g.find('h3') else 'No title'
        link = g.find('a')['href'] if g.find('a') else 'No link'
        results.append({'title': title, 'link': link})

    return jsonify(results)

if __name__ == '__main__':
    app.run(debug=True)