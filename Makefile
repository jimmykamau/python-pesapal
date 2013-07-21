test:
	@python test/__init__.py -f

publish:
	@python setup.py sdist upload

clean:
	@rm -rf build dist pesapal.egg-info $(shell find -name '*.pyc')

.PHONY: test publish clean