from setuptools import setup, find_packages

setup(
	name="filebrowser_s3",
	version="1.0.1",
	description="An S3 fix for Mezzanine's media manager.",
	author = 'Mozilla Foundation',
	author_email = 'pomax@mozillafoundation.org',
	maintainer="Pomax",
	maintainer_email="pomax@mozillafoundation.org",
	url = 'https://github.com:Jamie-BitFlight/filebrowser_s3',
	download_url = 'https://github.com:Jamie-BitFlight/filebrowser_s3/archive/1.0.1.tar.gz',
	packages=find_packages(),
	include_package_data=True,
	zip_safe=False,
	classifiers=[],
)
