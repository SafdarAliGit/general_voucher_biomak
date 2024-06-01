from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in general_voucher_biomak/__init__.py
from general_voucher_biomak import __version__ as version

setup(
	name="general_voucher_biomak",
	version=version,
	description="general_voucher_biomak",
	author="VUT",
	author_email="safdar211@gmail.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
