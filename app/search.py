from flask import request, make_response, jsonify

from app import app
from app.modules.crawler import StringCrawler
from app.views import response


@app.route('/')
def testApplication():
    return response('success','Application running', 200)

@app.route('/search', methods=['GET'])
def startSearch():

    term = request.args.get('term')
    url = request.args.get('url')

    try:
        if not term:
            raise Exception('No term specified')

        if not url:
            raise Exception('No url specified')

            
        search = StringCrawler(term, [url])
        result = search.crawl_string()


        return make_response(
            jsonify({
                'action': 'search',
                'status': 'success',
                'result': result
            })), 200

    except Exception as e:
        return response('failed', '{0}'.format(e), 500)
