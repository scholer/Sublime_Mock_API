from setuptools import setup

setup(
    name='Sublime-Mock-API',
    version='0.1',
    description='Install this package in your Sublime Text plugin developer environment to avoid getting editor warnings for the sublime and sublime_plugin imports.',
    url='https://github.com/scholer/Sublime_Mock_API',
    license='GPL v3',
    author='Rasmus Scholer Sorensen',
    author_email='rasmusscholer@gmail.com',
    packages=['sublime_mock_api'],
    py_modules=['sublime', 'sublime_plugin', 'sublime_api'],
)
