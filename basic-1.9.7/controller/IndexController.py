from pytonik.Web import App

m = App()

def index():

  data = {'title': 'Pytonik MVC'}

  m.views('index', data)
            