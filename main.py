from bottle import route, run, request, response

@route('/')
def hello():
    return "Hello world!"


@route('/currency')
def get_currency():
    content_type = request.get_header('Content-Type')

    if 'today' in request.query:
        data = "Today exchange rate is 41,5"
    elif 'yesterday' in request.query:
        data = "Yesterday exchange rate is 41,7"
    else:
        data = "Unknown query. Supported queries are /currency?today or /currency?yesterday"

    if content_type == 'application/json':  
        response.content_type = 'application/json'
        return '{"message": "hi from json"}'
    elif content_type == 'application/xml':
        response.content_type = 'application/xml'
        return "<message>hi from xml</message>"
    else:
        response.content_type = 'text/plain'
        return data

if __name__ == '__main__':
    run(port=8000)




