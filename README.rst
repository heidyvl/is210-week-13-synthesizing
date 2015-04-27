####################
IS 210 Assignment 13
####################
******************
Synthesizing Tasks
******************

:College: CUNY School of Professional Studies
:Course-Name: Software Application Programming I
:Course-Code: IS 210
:Points: 21
:Due-Date: 2015-05-04T09:00:00

Overview
========

It is very common in computer programming to create a class to manage the input
and output operation of data stored in a file on the computer's hard drive. In
the following tasks you will create an object that can get, set and delete
other pickled Python objects to and from a file. Make sure to review Chapter 9
of the text. Lutz covers how to use the native Python pickle module.

.. note::

    In the interest of brevity, assume that all tasks asking you to create new
    functions are doing so within the context of your new class. The ``self``
    attribute is implied for all such functions and is missing from lists of
    arguments.

Instructions
============

The following tasks will either have you interacting with existing files in
the assignment repository or creating new ones on the fly. Don't forget to add
your interpreter directive, utf-8 encoding, and a short docstring with any new
files that you create!

.. important::

    In these exercises, you may, on occasion, come across a task that requres
    you to research or use a function or method not directly covered by the
    course text. Since Python is such a large language it would be impossible
    for the author to have included descriptions of each and every available
    function which would largely duplicate the offical Python documentation.

    A *vital* skill to successful programming is being comfortable searching
    for and using official language documentation sources like the
    `Python String Documentation`_ page. Throughout our coursework we will be
    practicing both the use of the language in practice and the search skills
    necessary to become functional programmers.

Synthesizing Tasks
==================

Task 01
-------

You've already instantiated and used some classes already if you consider your
prior use of such classes like the ``Decimal()`` class. We've also now covered
how to create your own custom classes.

Specifications
^^^^^^^^^^^^^^

#.  Create a file named ``picklecache.py``. In ``picklecache.py``:

#.  Import the ``os`` and ``pickle`` modules.

#.  Create a new class named ``PickleCache`` with a constructor function that
    has two arguments:
    
    #.  ``file_path`` (string, optional) Defaults to ``datastore.pkl``

    #.  ``autosync`` (bool, optional) Defaults to ``False``
    
    The constructor must also define the following  *instance* attributes:

    #.  Pseudo-private attribute* named ``__file_path``. It must assigned the
        constructor variable ``file_path`` value.

    #.  Pseudo-private attribute named ``__data`` instantiated as an empty
        dictionary object.

    #.  A non-private attribute named ``autosync``

Examples
^^^^^^^^

.. code:: pycon

    >>> cacher = PickleCache()
    >>> kprint cacher._PickleCache__file_path
    'datastore.pkl'
    >>> print cacher._PickleCache__file_object
    None
    >>> print cacher._PickleCache__data
    {}

Task 02
-------

The ``self.__data`` attribute is pseudo-private and not by convention
accessible to outside objects. Therefore, you will need to create a public
method that allows key value pairs to be stored within the class. Here we'll
use Python's ``__setitem__`` magic method to make our cache behave like a
dictionary.

Specifications
^^^^^^^^^^^^^^

#.  Create a function within ``PickleCache`` named ``__setitem__()`` that takes
    two arguments:
    
    #.  ``key`` (required)
      
    #.  ``value`` (required)
      
    It will then save the pair in the ``self.__data`` dictionary.

#.  Additionally, define a ``__len__()`` function that takes no arguments
    (other than ``self``) and returns the length of ``self.__data``

Examples
^^^^^^^^

.. code:: pycon

    >>> pcache = PickleCache()
    >>> pcache['test'] = 'hello'
    >>> print pcache._PickleCache__data['test']
    'hello'
    >>> len(pcache)
    1

Task 03
-------

You will also need a way to retrieve data from the PickleCache object and
handlers for when data cannot be found.

Specifications
^^^^^^^^^^^^^^

#.  Create a method named ``__getitem__`` that takes one argument:
    
    #.  ``key`` (required)

    It must use this key to return the requested value from the ``self.__data`` 
    dictionary.

#.  If a key cannot be found, allow it to throw a ``TypeError`` or ``KeyError``
    normally.

Examples
^^^^^^^^

.. code:: pycon

    >>> pcache = PickleCache()
    >>> pcache['test'] = 'hello'
    >>> print pcache['test']
    'hello'

Task 04
-------

There needs to be a way to remove unwanted objects from the ``PickleCache``
object. This method is similar to the previous task but deletes a value
instead.

Specifications
^^^^^^^^^^^^^^

#.  Create a method named ``__delitem__`` that accepts one argument:

    #.  ``key`` (required)

#.  Use the ``key`` attribute and the ``del`` statement to remove any entries
    from the ``__data`` attribute with the same key.


Examples
^^^^^^^^

.. code:: pycon

    >>> pcache = PickleCache()
    >>> pcache['test'] = 'hello'
    >>> print len(pcache)
    1
    >>> del pcache['test']
    >>> print len(pcache)
    0

Task 05
-------

At this point you have created a standard class that can set, get and delete
objects while the program is running. Now you will make the data persist by
pickling it and saving it to a file. This way the data can be accessed the next
time the program runs.

You care going to need to use the ``os.path.exists()`` and ``os.path.getsize
()`` methods as part of your conditional logic.

Specifications
^^^^^^^^^^^^^^

#.  Create a new method method named ``load()``. It does not have any extra
    arguments.

    #.  Open the ``self.__file_path`` for reading only if it exists and has a
        file size greater than zero.

        #.  Use ``os.path.exists(self.__file_path)`` and
            ``os.path.getsize(self.__file_path)`` to check if the file at
            ``self.__file_path`` exists and if its size is greater than ``0``

        #.  Use ``pickle.load()`` to load the file object and save its
            contents in ``self.__data``

        #.  Close the file object.

        #.  Add a ``load()`` call to this classes' constructor

Examples
^^^^^^^^

.. code:: pycon

    >>> import pickle
    >>> fh = open('datastore.pkl', 'w')
    >>> pickle.dump({'foo': 'bar'}, fh)
    >>> fh.close()
    >>> pcache = PickleCache('datastore.pkl')
    >>> print pcache['foo']
    'bar'

Task 06
-------

Your cache class needs to be able to save its stored data to file when
commanded to do so. This is especially important if the PickleCache were to
be used in a program running for more than just a few moments. Now you will
use the ``pickle.dump()`` method and the file object ``close()`` methods to
accomplish this.

Specifications
^^^^^^^^^^^^^^

#.  Create a new method named ``flush()``.

#.  Open the file found at ``self.__file_path`` as *writeable*

#.  Use ``pickle.dump()`` to save the data found in the ``PickleCache``
    ``__data`` attribute to the ``PickleCache`` ``__file_object`` attribute
    to the writeable file object.

#.  Close the file object after dumping your pickle file.

Examples
^^^^^^^^

.. code:: pycon

    >>> pcache = PickleCache()
    >>> pcache['foo'] = 'bar'
    >>> pcache.flush()
    >>> fhandler = open(pcache._PickleCache__file_path, 'r')
    >>> data = pickle.load(fhandler)
    >>> print data
    {'foo': 'bar'}

Task 07
-------

We now have a dictionary-like object that can write out the data it stores to
a caching file. It also loads that file by default, effectively resuming the
data at its last-known state. The last trick is to implement our auto-sync
feature so that the file cache can be written after each major data changing
operation.

Specifications
^^^^^^^^^^^^^^

#.  Update the ``__getitem__()`` method to call ``self.flush()`` if
    ``self.autosync`` is ``True``

#.  Repeat the prior step for the ``__delitem__()`` method.

Congratulations! You've completed a simple file-backed caching engine! Now, if
``autosync`` is set to ``True`` all additions, changes, and deletes will be
synchronized to the disk cache.

.. note::

    You'll note that I directed you to set ``autosync`` to default to
    ``False``. The reason is that this would create a very "chatty" system
    that would regularly be writing to disk. Consider it in the context of
    something like a loop! It's not always desirable to write out to files on
    a regular basis as it can be extremely slow.

.. note::

    This implementation has several flaws that would prevent it from being
    useful in a production context. Worst among them is the fact that the
    entire file is being written each time the cache is flushed. When
    autosync is enabled it would be preferable to only append or remove the
    changed lines instead of overwrite the entire file. This is a case where
    the file append flag might be helpful.

Examples
^^^^^^^^

.. code:: pycon

    >>> pcache1 = PickleCache(autosync=True)
    >>> pcache1['apples'] = 'oranges'
    >>> pcache2 = PickleCache()
    >>> print pcache2['apples']
    'oranges'


Executing Tests
===============

Code must be functional and pass tests before it will be eligible for credit.

Linting
-------

Lint tests check your code for syntactic or stylistic errors To execute lint
tests against a specific file, simply open a terminal in the same directory as
your code repository and type:

.. code:: console

    $ pylint filename.py

Where ``filename.py`` is the name of the file you wish to lint test.

Unit Tests
----------

Unit tests check that your code performs the tested objectives. Unit tests
may be executed individually by opening a terminal in the same directory as
your code repository and typing:

.. code:: console

    $ nosetests tests/name_of_test.py

Where ``name_of_test.py`` is the name of the testfile found in the ``tests``
directory of your source code.

Running All Tests
-----------------

All tests may be run simultaneously by executing the ``runtests.sh`` script
from the root of your assignment repository. To execute all tests, open a
terminal in the same directory as your code repository and type:

.. code:: console

    $ bash runtests.sh

Submission
==========

Code should be submitted to `GitHub`_ by means of opening a pull request.

As-of Lesson 02, each student will have a branch named after his or her
`GitHub`_ username. Pull requests should be made against the branch that
matches your `GitHub`_ username. Pull requests made against other branches will
be closed.  This work flow mimics the steps you took to open a pull request
against the ``pull`` branch in Week Two.

For a refresher on how to open a pull request, please see homework instructions
in Lesson 01. It is recommended that you run PyLint locally after each file
is edited in order to reduce the number of errors found in testing.

In order to receive full credit you must complete the assignment as-instructed
and without any violations (reported in the build status). There will be
automated tests for this assignment to provide early feedback on program code.

When you have completed this assignment, please post the link to your
pull request in the body of the assignment on Blackboard in order to receive
credit.

.. _GitHub: https://github.com/
.. _Python String Documentation: https://docs.python.org/2/library/stdtypes.html
