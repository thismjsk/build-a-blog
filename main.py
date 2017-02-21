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
from google.appengine.ext import db

template_dir = os.path.join(os.path.dirname(__file__), 'templates')
jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader(template_dir), autoescape = True)

class Index(webapp2.RequestHandler):
    def get(self):
        self.redirect("/blog")

class NewPost(webapp2.RequestHandler):
    def get(self):
        t = jinja_env.get_template("newpost.html")
        content = t.render(
        )
        self.response.write(content)

    def post(self):
        title = self.request.get("title")
        post_body = self.request.get("post_body")

        if title and post_body:
            post = Posts(title = title, post_body = post_body)
            post.put()
            self.redirect("/")
        else:
            error = "You are missing something from your post!"
            t = jinja_env.get_template("newpost.html")
            content = t.render(
            title = title,
            post_body = post_body,
            error = error
            )
            self.response.write(content)

class Posts(db.Model):
    title = db.StringProperty(required = True)
    post_body = db.TextProperty(required = True)
    created = db.DateTimeProperty(auto_now_add = True)

class RecentPosts(webapp2.RequestHandler):
    def get(self):
        query = Posts.all().order("-created")
        recent_posts = query.fetch(limit = 5)

        t = jinja_env.get_template("frontpage.html")
        content = t.render(posts = recent_posts
        )
        self.response.write(content)



class ViewPostHandler(webapp2.RequestHandler):
    def get(self, id):
        self.response.write(id) #currently set up to just print the ID



app = webapp2.WSGIApplication([
    ('/', Index),
    webapp2.Route('/blog/<id:\d+>', ViewPostHandler),
    ('/blog', RecentPosts),
    ('/newpost', NewPost)


], debug=True)
