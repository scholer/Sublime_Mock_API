
# Sublime Mock API

A simple package providing mock/dummpy versions of the modules otherwise provided by Sublime Text.
Use this to avoid getting syntax errors or import errors when developing 
and testing your Sublime Text plugins.

The primary module of importance in this package is the `sublime_api` module.
This mocks the built-in API module provided by the Sublime Text execution environment,
and is required in order to invoke many of the functions generally used when 
developing Sublime Text plugins.

The `sublime.py` and `sublime_plugin.py` python modules distributed with this package 
are based on the identically-named files distributed with Sublime Text 3.

The `sublime` and `sublime_plugin` modules included with this package *have been slightly altered* 
to make them easier to use in a plugin development environment.
For instance, loading the original `sublime` module will go in and override/redirect 
`sys.stdout` and `sys.stderr`.

NOTE: The GPL LICENSE under which this package is distributed DOES NOT APPLY TO THE 
`sublime` and `sublime_plugin` modules; these modules are based on files from the
Sublime Text installation, and is subject to the Sublime Text license.

(However, since the `sublime.py` and `sublime_plugin.py` files are freely available 
for download with the Sublime Text installer, hopefully the authors won't mind them 
being derived and distributed with this package - since they are only used by people
working to create plugins for Sublime Text.)


## Installation:

1. As always, you should probably create a dedicated, project-specific 
	virtual environment, using your tool of choice 
	(e.g. `venv`, `virtualenv`, `pipenv`, `poetry`, `conda`, etc.)

	* For example, to create and activate a new `conda` environment:

			conda create -n sublime-dev
			conda activate sublime-dev

	* You can (and should) install any additional dependencies that you need for 
		your plugin development in the same virtual environment.


2. Install this package using `pip`:

		pip install git+https://github.com/scholer/Sublime_Mock_API


3. Test your installation: 
	Load up your python interpreter and check that you can import the modules from this package:
	
		> python
		( Pyhton 3.x.y welcome banner )
		>>> import sublime_mock_api
		>>> import sublime_mock_api.mock_api
		>>> import sublime_api
		>>> import sublime
		>>> import sublime_plugin
		
	* If all of the above imports succeed without error, the installation is successful.


### Setting up your editor:

Most editors (PyCharm, Visual Studio Code, etc) have an option to select which 
python interpreter to use for your project.
As long as you select the interpreter for the environment you created above,
your editor should pick up the mocked `sublime_api`, `sublime`, and `sublime_plugin` modules
without further configuration.





## Alternative ways to configure your development environment


#### 1. Using the `sublime` and `sublime_plugin` modules that comes with your Sublime Text installation

If you feel that downloading and installing this `Sublime Mock API` package is too much work,
then you can also just add your Sublime Text installation path 
to your environment PATH (or your PYTHONPATH variable).

This works reasonably well in terms of basic "editor linting", 
where your editor checks your code against the `sublime` and `sublime_plugin` modules.
However, since both the `sublime` and `sublime_plugin` modules tries to import `sublime_api`,
which is not available to your editor, the editor may not work optimally in terms of code 
checking and code completion.

And obviously, if you would like to create and run automated tests of your plugins 
outside of Sublime Text, then you will need to provide some kind of mocked module,
so that your plugin can load `sublime` and `sublime_plugin` modules without 
encountering ImportErrors.



## Contributing:

You are very welcome to contribute to this package, if you feel it can be improved in any way.

Mocking the entire sublime_api module is pretty extensive, 
and this package is only doing the most basic job right now.

If you would like to contribute, just fork this repository on GitHub,
make the changes you would like to provide, and submit a pull request on GitHub.



## Prior art:

A quick Google search only found the following so far (please add if you find more):

* https://github.com/devaos/sublime-remote/blob/master/remote/sublime_api.py
* https://github.com/spywhere/Javatar/blob/master/tests/stubs/sublime_api.py
* https://github.com/limetext/lime - 
	"Open source API-compatible alternative to the text editor Sublime Text". 
	Written in Go.
* https://github.com/xi-editor/xi-editor
