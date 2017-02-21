#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import webapp2, jinja2, os

template_dir = os.path.join(os.path.dirname(__file__), 'templates')
jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader(template_dir))

class MainHandler(webapp2.RequestHandler):
    def get(self):
        t = jinja_env.get_template("frontpage.html")
        content = t.render(
        )
        self.response.write(content)

class ViewPostHandler(webapp2.RequestHandler):
    def get(self, id):
        self.response.write(id) #currently set up to just print the ID

class RecentPosts(webapp2.RequestHandler):
    def get(self):
        pass

class NewPost(webapp2.RequestHandler):
    def get(self):
        pass



app = webapp2.WSGIApplication([
    ('/', MainHandler),
    webapp2.Route('/blog/<id:\d+>', ViewPostHandler),
    ('/blog', RecentPosts),
    ('/newpost', NewPost)


], debug=True)
