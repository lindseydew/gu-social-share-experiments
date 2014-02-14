import webapp2
import os
import jinja2

jinja_environment = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.join(os.path.dirname(__file__), "templates")))

class MainPage(webapp2.RequestHandler):

    def get(self):
        template = jinja_environment.get_template('index.html')

        template_values = {}

        self.response.out.write(template.render(template_values))

class CtaPanel(webapp2.RequestHandler):

    def get(self):
        template = jinja_environment.get_template('cta.html')

        template_values = {}

        self.response.out.write(template.render(template_values))

application = webapp2.WSGIApplication([
    ('/', MainPage),
    ('/social/cta', CtaPanel)
], debug=True)