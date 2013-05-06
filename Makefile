test:
	@python test/__init__.py -f

publish:
	@python setup.py sdist upload

.PHONY: test