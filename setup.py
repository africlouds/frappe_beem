from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in frappe_beem/__init__.py
from frappe_beem import __version__ as version

setup(
	name="frappe_beem",
	version=version,
	description="Frappe Integration with Beem Africa communication platform",
	author="Africlouds Ltd",
	author_email="info@africlouds.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
