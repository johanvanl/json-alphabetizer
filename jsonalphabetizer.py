
import webapp2
import cgi

import json

class MainPage(webapp2.RequestHandler):
    def get(self):
        # Didn't want to install the templates library
        # to run locally
        self.response.write(open('index.html', 'r').read())

    def post(self):
        out = None
        try:
            ind = int(self.request.get('inp_indent').strip())
            js = json.loads(self.request.get('ta_json'))
            if self.request.get('rad_group_out') == 'rad_prettify':
                out = json.dumps(js, sort_keys=True, indent=ind)
            else:
                out = json.dumps(js, sort_keys=True, indent=None, separators=(',', ':'))
        except ValueError, e:
            out = 'ERROR : The indent needs to be a number, which indicated the amount of spaces to use.'
        except Exception, e:
            out = 'ERROR : ' + str(e)

        style = '<style type="text/css">html,body{height:100%;}textarea{width:100%;height:98%;}</style>'
        self.response.write(style + '<textarea>' + out + '</textarea>')

application = webapp2.WSGIApplication([
    ('/', MainPage),
], debug=True)

def main():
    from paste import httpserver
    httpserver.serve(application, host='127.0.0.1', port='8080')

if __name__ == '__main__':
    main()
