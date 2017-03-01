package = pandoc-beamer-notes

# Installs the editable version
install: uninstall package
	pip install -e $(CURDIR)

# Installs the packaged version
testpackage: uninstall package
	pip install dist/$(package)*.tar.gz

# Packs the package into the dist directory and signs it
package: clean
	python setup.py sdist
	gpg --detach-sign --armor dist/$(package)*.tar.gz

# Uninstalls the package from a local installation
uninstall:
	pip freeze | grep $(package) > /dev/null ; \
	if [ $$? -eq 0 ]; then \
		pip uninstall $(package) -y ; \
	fi

clean:
	rm -rf dist

# Publishes to pypitest
testpublish: package
	@read -p "Enter the name of this package to verify upload to pypi test: " name ; \
	if [ "$$name" == "$(package)" ]; then \
		twine register -r pypitest $$(ls dist/*.tar.gz) ; \
		twine upload -r pypitest dist/* ; \
	else \
		echo 'Sorry, this was wrong. Please try again.' ; \
	fi

# Publishes to pypi
publish: package
	@read -p "Enter the name of this package to verify upload to pypi: " name ; \
	if [ "$$name" == "$(package)" ]; then \
		twine register -r pypi $$(ls dist/*.tar.gz) ; \
		twine upload -r pypi dist/* ; \
	else \
		echo 'Sorry, this was wrong. Please try again.' ; \
	fi
