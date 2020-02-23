import setuptools
from os.path import splitext
from glob import glob


with open('README.md', 'r') as fh:
    long_description = fh.read()


setuptools.setup(
    name="mynews_bot",
    description="Get news items from multiple news sources",
    long_description=long_description,
    long_description_content_type="text/markdown", # required as pypi expects reStructuredText by default
    version='0.1.1',
    author="Rajarshi Ghosh",
    author_email="rajarshig89@gmail.com",
    url="https://github.com/rajarshig/mynews_bot",
    keywords=['python', 'command-line', 'rss feed'],
    packages=setuptools.find_packages('src'),  # why providing src
    install_requires=["feedparser"],
    scripts=['src/mynews_bot.py'],
    package_dir={'':'src'},
    platforms='any',
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ],
    entry_points={
        "console_scripts": [
            "mynews-bot=mynews_bot:cmd_runner"  # EntryPoint must be in 'name=module:attrs [extras]' format"
        ]
    },
    python_requires='>=2.7',

)