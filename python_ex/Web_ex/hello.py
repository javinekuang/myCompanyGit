__author__ = 'sd'


def application(environ, start_response):
    start_response('200 OK', [('Content-Type', 'text/html')])
    return '''
    <style>
    h1{color:#333333;
    font-size:48px;
    }
    </style>
    <h1>Hello,Javine!<h1>
    <script>
    function a()
    {
        document.getElementsByTagName('h1')[0].style.color='#ff0000';
    }
    </script>
    <body>
    <h1 onmousemove="a()" >hi,Funny!!!</h1>
    </body>'''


