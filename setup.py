# -*- coding: utf-8 -*-
"""Installer for the imioweb.policy package."""

from setuptools import find_packages
from setuptools import setup


long_description = "\n\n".join(
    [
        open("README.rst").read(),
        open("CONTRIBUTORS.rst").read(),
        open("CHANGES.rst").read(),
    ]
)


setup(
    name="imioweb.policy",
    version="1.0b9",
    description="Policy for the installation of buildout.imioweb",
    long_description=long_description,
    # Get more from https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        "Environment :: Web Environment",
        "Framework :: Plone",
        "Framework :: Plone :: 5.2",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Operating System :: OS Independent",
        "License :: OSI Approved :: GNU General Public License v2 (GPLv2)",
    ],
    keywords="Python Plone",
    author="Nicolas Demonte",
    author_email="support@imio.be",
    url="https://pypi.python.org/pypi/imioweb.policy",
    license="GPL version 2",
    packages=find_packages("src", exclude=["ez_setup"]),
    namespace_packages=["imioweb"],
    package_dir={"": "src"},
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        # -*- Extra requirements: -*-
        "plone.api>=1.8.3",
        "Products.GenericSetup>=1.8.2",
        "setuptools",
        "z3c.jbot",
        "eea.facetednavigation",
        "collective.faceted.taxonomywidget",
        "plone.app.imagecropping",
        "plone.app.mosaic",
        "imioweb.theme",
        "collective.behavior.banner",
        "collective.behavior.gallery",
        "collective.easyform",
        "collective.preventactions",
        "iaweb.mosaic",
        "pas.plugins.imio",
        "collective.faceted.map",
        "imioweb.core",
        "collective.sendinblue>=2.0",
        "collective.folderishtypes[dexterity]",
        "imio.prometheus",
    ],
    extras_require={
        "test": [
            "plone.app.testing",
            # Plone KGS does not use this version, because it would break
            # Remove if your package shall be part of coredev.
            # plone_coredev tests as of 2016-04-01.
            "plone.testing>=5.0.0",
            "plone.app.contenttypes",
            "plone.app.robotframework[debug]",
        ]
    },
    entry_points="""
    [z3c.autoinclude.plugin]
    target = plone
    """,
)
