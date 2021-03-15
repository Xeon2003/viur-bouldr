import os, logging

for skelModule in os.listdir(os.path.dirname(__file__)):
	if skelModule == "__init__.py" or not skelModule.endswith(".py"):
		continue

	try:
		__import__(skelModule[:-3], globals(), locals(), level=1)
	except ImportError:
		logging.error("Unable to import skeleton %s" % skelModule[:-3])

	except:
		raise

del skelModule
