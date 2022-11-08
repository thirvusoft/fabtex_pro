from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in fabtex_pro/__init__.py
from fabtex_pro import __version__ as version

setup(
	name="fabtex_pro",
	version=version,
	description="fabtex",
	author="Thirvusoft",
	author_email="fabtex@gmail.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
