from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.common.keys import Keys
import queue
import os
#from exif.settings import NGINX_HOST, PHANTOMJS_HOST, PHANTOMJS_PORT

from threading import Thread
import pickle
import pika
from base64 import b64decode

NGINX_HOST = os.getenv('NGINX_HOST')
PHANTOMJS_HOST = os.getenv('PHANTOMJS_HOST')
PHANTOMJS_PORT = os.getenv('PHANTOMJS_PORT')
RABBIT_HOST = os.getenv('RABBIT_HOST')
base_url = "http://{0}/".format(NGINX_HOST)


# we might have people messing with both and it needs to refresh it's state. aka clear cookies, readd cookies etc
class Victim(Thread):

    def __init__(self):
        Thread.__init__(self)
        self.driver = webdriver.Remote(command_executor="{0}:{1}".format(PHANTOMJS_HOST, PHANTOMJS_PORT), desired_capabilities=DesiredCapabilities.PHANTOMJS)
        self.flag = "SUN{why_bo0ther_with_ex1f}"


    def auth(self):
        self.driver.get(base_url+"login")
        elem = self.driver.find_element_by_name("username")
        elem.send_keys("pontifex")
        elem = self.driver.find_element_by_name("password")
        elem.send_keys("apexlegends?")
        elem.send_keys(Keys.RETURN)

    def checkAuth(self):
        self.driver.get(base_url+'/')
        try:
            elem = self.driver.find_element_by_name('login')
        except:
            self.auth()

    def addToQueue(self, instance):
        self.queue.put(instance)

    def visitImage(self, user_id, filename):
        try: # it always gives UnableToSetCookieException need to figure out why "errorMessage":"Unable to set Cookie""
            self.driver.add_cookie({"domain":NGINX_HOST, "name":"flag", "value":self.flag})
        except Exception as e:
            pass
        try:
            self.driver.add_cookie({"domain":NGINX_HOST, "name":"jwtsess", "value":"eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyIjoidGhlcm9jayIsInNpZyI6Imh0dHA6Ly9uZ2lueC9zdGF0aWMvc2VjcmV0LmtleSIsInJvbGUiOiJ1c2VyIn0.GyJM1uu-079ZjNPS4eeTPJ2kqoNPO6WXQknMlTP03gs"})
        except Exception as e:
            pass
        try:
            self.driver.add_cookie({"domain":NGINX_HOST, "name":"jwtsess", "value":"eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyIjoidGhlcm9jayIsInNpZyI6Imh0dHA6Ly9uZ2lueC9zdGF0aWMvc2VjcmV0LmtleSIsInJvbGUiOiJ1c2VyIn0.GyJM1uu-079ZjNPS4eeTPJ2kqoNPO6WXQknMlTP03gs"})
        except Exception as e:
            print(e)
        self.driver.get(base_url+"bot/exif/{0}/{1}".format(user_id, filename))
        return 1

    def callback(self, ch, method, properties, body):
        image = pickle.loads(b64decode(body))
        attempts = 0
        while True: # try to get the page, check auth if fails
            try:
                print("bot trying {0}".format(image))
                attempts += 1
                if attempts > 4:
                    break
                self.checkAuth()
                self.visitImage(image['user_id'], image['filename'])
                break
            except Exception as e:
                print(e)
                self.auth()
                continue

    def run(self):
        connection = pika.BlockingConnection(pika.ConnectionParameters(RABBIT_HOST))
        channel = connection.channel()
        channel.queue_declare(queue='victim')
        channel.basic_consume(self.callback, queue='victim', no_ack=True)
        channel.start_consuming()

Victim().run()
