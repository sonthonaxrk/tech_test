# Cron Parser

By candidate <censored to prevent implicit bias>.

# Quickstart

	$ pip install .
	$ cron_parser -h
	$ cron_parser HH:MM < file

Or (given this program takes stdin):

	$ streaming_output | cron_parser HH:MM 

# Running Tests

Installs pytest and runs the suit in a py36 environment. Tox is the correct choice because this is a locally run package.

	$ tox

# Packaging

Creates a pip installable zip file in ./dist/ (not using this for this test because you presumably want the non-packaged tests).

	python setup.py sdist --formats=zip
