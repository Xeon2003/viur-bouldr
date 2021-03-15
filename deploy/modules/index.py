from viur.core import conf, errors, exposed, request
from viur.core.render.html import default as default_render
from viur.core.utils import currentRequest

class Index(object):

	def __init__(self, *args, **kwargs):
		self.render = default_render(self)

	@exposed
	def index(self, *args, **kwargs):
		if len(args) > 1 or kwargs:
			raise errors.NotFound()

		template = self.render.getEnv().get_template("index.html")
		return template.render(start=True)

	@exposed
	def sitemap_xml(self, *args, **kwargs):
		currentRequest.get().response.headers["Content-Type"] = "text/xml"
		return self.render.view({}, tpl="sitemap")

Index.html = True