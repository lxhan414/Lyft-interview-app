import webapp2

class MainPage(webapp2.RequestHandler):
    def get(self):
        self.response.headers["Content-Type"] = "text/html"
        self.response.write("""
          <html>
            <head><title>Sum of numbers</title></head>
            <body>
              <form action="/test" method="post">
                x: <input type="text" name="x", ><br>
                y: <input type="text" name="y"><br>
                <input type="submit" value="Submit">
              </form>
            </body>
            </html>""")


class Sum(webapp2.RequestHandler):
    def post(self):
        x = self.request.get("x")
        y = self.request.get("y")
        self.response.headers["Content-Type"] = "text/json"
        try:
            res = float(x) + float(y)
            self.response.write({"sum":res})
        except ValueError:
            self.response.write("Invalid input!")


routes = [('/', MainPage), ('/test', Sum)]
my_app = webapp2.WSGIApplication(routes, debug=True)
