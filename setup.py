#
# This file is autogenerated during plugin quickstart and overwritten during
# plugin makedist. DO NOT CHANGE IT if you plan to use plugin makedist to update 
# the distribution.
#

from setuptools import setup, find_packages

kwargs = {'author': 'Eric Hendricks',
 'author_email': 'eric.hendricks@nasa.gov',
 'classifiers': ['Intended Audience :: Science/Research',
                 'Topic :: Scientific/Engineering'],
 'description': 'OpenMDAO component wrapper for HSR_Noise',
 'download_url': '',
 'entry_points': '[openmdao.component]\nhsrnoise_wrapper.hsrnoise.HSRNOISE=hsrnoise_wrapper.hsrnoise:HSRNOISE\n\n[openmdao.container]\nhsrnoise_wrapper.geometry.Geometry=hsrnoise_wrapper.geometry:Geometry\nhsrnoise_wrapper.hsrnoise.HSRNOISE=hsrnoise_wrapper.hsrnoise:HSRNOISE\nhsrnoise_wrapper.MEflows.MEflows=hsrnoise_wrapper.MEflows:MEflows\nhsrnoise_wrapper.stream.Stream=hsrnoise_wrapper.stream:Stream',
 'include_package_data': True,
 'install_requires': ['openmdao.main'],
 'keywords': ['openmdao'],
 'license': 'Apache License, Version 2.0',
 'maintainer': 'Kenneth Moore',
 'maintainer_email': 'kenneth.t.moore-1@nasa.gov',
 'name': 'hsrnoise_wrapper',
 'package_data': {'hsrnoise_wrapper': ['sphinx_build/html/.buildinfo',
                                       'sphinx_build/html/genindex.html',
                                       'sphinx_build/html/index.html',
                                       'sphinx_build/html/objects.inv',
                                       'sphinx_build/html/pkgdocs.html',
                                       'sphinx_build/html/py-modindex.html',
                                       'sphinx_build/html/search.html',
                                       'sphinx_build/html/searchindex.js',
                                       'sphinx_build/html/srcdocs.html',
                                       'sphinx_build/html/usage.html',
                                       'sphinx_build/html/_modules/index.html',
                                       'sphinx_build/html/_modules/hsrnoise_wrapper/geometry.html',
                                       'sphinx_build/html/_modules/hsrnoise_wrapper/hsrnoise.html',
                                       'sphinx_build/html/_modules/hsrnoise_wrapper/MEflows.html',
                                       'sphinx_build/html/_modules/hsrnoise_wrapper/stream.html',
                                       'sphinx_build/html/_modules/hsrnoise_wrapper/test/test_hsrnoise_wrapper.html',
                                       'sphinx_build/html/_sources/index.txt',
                                       'sphinx_build/html/_sources/pkgdocs.txt',
                                       'sphinx_build/html/_sources/srcdocs.txt',
                                       'sphinx_build/html/_sources/usage.txt',
                                       'sphinx_build/html/_static/ajax-loader.gif',
                                       'sphinx_build/html/_static/basic.css',
                                       'sphinx_build/html/_static/comment-bright.png',
                                       'sphinx_build/html/_static/comment-close.png',
                                       'sphinx_build/html/_static/comment.png',
                                       'sphinx_build/html/_static/default.css',
                                       'sphinx_build/html/_static/doctools.js',
                                       'sphinx_build/html/_static/down-pressed.png',
                                       'sphinx_build/html/_static/down.png',
                                       'sphinx_build/html/_static/file.png',
                                       'sphinx_build/html/_static/jquery.js',
                                       'sphinx_build/html/_static/minus.png',
                                       'sphinx_build/html/_static/plus.png',
                                       'sphinx_build/html/_static/pygments.css',
                                       'sphinx_build/html/_static/searchtools.js',
                                       'sphinx_build/html/_static/sidebar.js',
                                       'sphinx_build/html/_static/underscore.js',
                                       'sphinx_build/html/_static/up-pressed.png',
                                       'sphinx_build/html/_static/up.png',
                                       'sphinx_build/html/_static/websupport.js',
                                       'test/__init__.py',
                                       'test/base.input',
                                       'test/base.output',
                                       'test/base_hsr.dump',
                                       'test/hsr_template.input',
                                       'test/test_hsrnoise_wrapper.py']},
 'package_dir': {'': 'src'},
 'packages': ['hsrnoise_wrapper', 'hsrnoise_wrapper.test'],
 'url': 'https://github.com/OpenMDAO-Plugins/hsrnoise_wrapper',
 'version': '0.2.1',
 'zip_safe': False}


setup(**kwargs)

