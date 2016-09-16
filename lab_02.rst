################
Git walk-through
################

Basic configuration
===================

We need to tell git about us before we start. This stuff will go into
the commit information by default.

.. workrun::
    :hide:

    rm -rf our_work

.. workrun::

    git config --global user.name "Matthew Brett"
    git config --global user.email "matthew.brett@gmail.com"

git often needs to call up a text editor. We will use Atom as our text editor
(see `associating text editors with git`_):

.. workrun::

    git config --global core.editor "atom --wait"

We also turn on the use of color, which is very helpful in making the
output of git easier to read:

.. workrun::

    git config --global color.ui "auto"

Getting help
============

.. workrun::
    :allow-fail:

    git

Try ``git help add`` for an example.

Initializing the repository
===========================

We first make a new empty directory that will be version controlled with git.

.. workrun::
    :hide:

    mkdir our_work

Create the git repository:

.. workrun::

    cd our_work
    git init

Show the new ``.git`` directory:

.. prizerun::

    ls .git

There are only a couple of empty sub-directories in the ``.git/objects``
directory:

.. prizerun::

    ls .git/objects/*

.. _git-add:

git add - put stuff into the staging area
=========================================

Type this file in Atom and save:

.. prizewrite:: our_paper.txt

    This is the first sentence of the new paper.

Add to the staging area:

.. prizerun::

    git add our_paper.txt

.. prizevar:: our_paper_1_hash

    git rev-parse :our_paper.txt

Check we added the file to the staging area:

.. prizerun::

    git status

Show yourself there is a new sub-directory and file in ``.git/objects``:

.. prizerun::
    :hide-out:

    ls .git/objects/*

Looking at real git objects
===========================

Now we're going to read the new object in Python, and find the hash of its
contents.  You don't need to do this kind of thing to use git.  This is to
practice to some Python, and to show you how git stores its files.

To read the new object, you'll need a few new bits of Python.

Here's how to read the binary contents of a whole file into memory:

.. nbplot::
    :include-source: false

    >>> with open('our_paper.txt', 'wt') as fobj:
    ...     fobj.write('This is the first sentence of the new paper.\n')
    ...
    45

.. nbplot::

    >>> # Open a file in Read Binary mode to read bytes
    >>> fobj = open('our_paper.txt', 'rb')
    >>> # Read contents as bytes
    >>> contents = fobj.read()  # Read the whole file
    >>> fobj.close()
    >>> type(contents)
    <class 'bytes'>

Here's how to calculate the SHA1 hash value for the file contents:

.. nbplot::

    >>> # Import the Python module that calculates hash values
    >>> import hashlib
    >>> # Generate the SHA1 hash string for these bytes
    >>> hashlib.sha1(contents).hexdigest()
    'cb083f8092a8bfbe55a215e1b45e9f33b9dec86f'

This is the same value as the terminal command ``shasum`` calculates on a
file:

.. prizerun::

    shasum our_paper.txt

The new file in ``.git/objects`` is *compressed* using a program called
``zlib``.  To un-compress some bytes that have been compressed with ``zlib``,
use the ``decompress`` function in the Python ``zlib`` module:

.. nbplot::

    >>> import zlib
    >>> zlib.decompress
    <built-in function decompress>

.. prizevar:: sha_fname

    echo "function sha_fname { echo \${1:0:2}/\${1:2}; }; sha_fname "

.. prizevar:: our_paper_1_fname

    fname=$({{ sha_fname }} {{ our_paper_1_hash }})
    echo ".git/objects/$fname"

Now |--| what is the *decompressed* contents of the new ``.git/objects`` file?
Do you recognize it?  What is the SHA1 hash of the decompressed contents?  Do
you recognize that?  Start with something like:

.. prizeout::

    echo ">>> fobj = open('{{ our_paper_1_fname }}', 'rb')"

where |our_paper_1_fname| is the new file that appeared in your
``.git/objects`` directory when you staged ``our_paper.txt``.

When you are done, have a look at the solution in: `reading git objects
<https://matthew-brett.github.io/curious-git/reading_git_objects.html>`_.

.. nbplot::
    :include-source: false

    >>> import os
    >>> os.remove('our_paper.txt')

Make a first commit
===================

Remember what will go into this commit:

.. prizerun::

    git status

Make the commit:

.. prizerun::
    :dont-run:

    git commit

.. prizecommit:: commit_1_sha 2016-09-15 14:30:13
    :hide:

    git commit -m "First version of the paper"

Review what you have so far in your history:

.. prizerun::
    :hide-out:

    git log

Show what branch you are on, with the hash of the current commit:

.. prizerun::
    :hide-out:

    git branch -v

Edit again, check and commit
============================

Edit the paper file again to add some text:

.. prizewrite:: our_paper.txt

    This is the first sentence of the new paper.

    Crucially, this is the second sentence.

Check the difference between what you had before and what you have now:

.. prizerun::
    :hide-out:

    git diff

Add the changes to the staging area::

    # What goes here?

.. prizerun::
    :hide:

    git add our_paper.txt

Our customary check:

.. prizerun::
    :hide-out:

    git status

Make the commit:

.. prizerun::
    :dont-run:

    git commit

.. prizecommit:: commit_2_sha 2016-09-15 14:35:13
    :hide:

    git commit -m "Second version of the paper"

Look at the project history again:

.. prizerun::
    :hide:

    git log

Check the parent hashes recorded in each commit.  How?::

    # Check the parents

Check which hash the default branch is pointing to now:

.. prizerun::
    :hide-out:

    git branch -v

A new file
==========

Make a new file like this:

.. prizewrite:: our_analysis.py

    # An analysis of our data
    # Details to be confirmed

    print("Tada!")

Check the status of the file.

Add the file to the staging area.

Make a commit.

.. prizerun::
    :hide:

    git add our_analysis.py

.. prizecommit:: commit_3_sha 2016-09-15 14:40:13
    :hide:

    git commit -m "Add analysis"

A prettier log command
======================

.. workrun::

    git config --global alias.slog "log --oneline --graph"

.. prizerun::

    git slog

Thinking about objects again
============================

See if you can guess how many files there are now in ``.git/objects``.

What do these objects store?

If you have the hash of an object, you can check the contents with ``git
cat-file -p`` followed by the first 7 digits of the hash value |--| e.g.

.. prizevar:: sha_7

    echo "function sha_7 { echo \${1:0:7}; }; sha_7 "

.. prizevar:: our_paper_1_hash_7

    {{ sha_7 }} {{ our_paper_1_hash }}

.. prizerun::

    git cat-file -p {{ our_paper_1_hash_7 }}

See if you can find the hash of the object corresponding to the directory
listing for our most recent commit, and display its contents.  Hint: Find the
hash for the current commit message.  Try displaying the contents for the
current commit message.

Moving files
============

Try moving a file (renaming) using ``git mv``:

.. prizerun::

    git mv our_analysis.py our_first_analysis.py

Check the status.  Do you need to add anything to the staging area?

Make a commit.

Now you have made a commit, check the new directory listing for our latest
commit.  What changed?

.. prizecommit:: commit_4_sha 2016-09-15 14:45:13
    :hide:

    git commit -m "Move analysis file"

Making a new branch
===================

Make a new branch with:

.. prizerun::

    git branch work-from-home

Use ``git branch -v`` to check the hash that this new branch points to.

Have a look at the file ``.git/HEAD``.  What is it telling us?

Tell git to start working on the new branch instead of our previous branch:

.. prizerun::

    git checkout work-from-home

Have a look at ``git branch -v`` again.  What changed?  How about the file
``.git/HEAD``?

.. prizerun::
    :hide:

    echo "" >> our_paper.txt
    echo "The third sentence starts the crescendo." >> our_paper.txt

Now see if you can replicate the following changes to ``our_paper.txt``:

.. prizeout::

    git diff

Your job is to make the output from ``git diff`` look the same as the output
above.

When you've finished, add the changes to the staging area and then commit.

.. prizerun::
    :hide:

    git add our_paper.txt

.. prizecommit:: work_from_home_1_sha 2016-09-15 14:50:13
    :hide:

    git commit -m "Move analysis file"

Check where you are with ``git slog``, and ``git branch -v``.

Now go back to your previous branch, called ``master``:

.. prizerun::

    git checkout master

Create this data file, add it to the staging area and commit.

.. prizewrite:: our_data.csv

    0,210,32
    1,212,30
    2,220,29

.. prizerun::
    :hide:

    git add our_data.csv

.. prizecommit:: master_1_sha 2016-09-15 14:50:13
    :hide:

    git commit -m "Add data file"

Merging
=======

Now we want to merge the work from the ``work-from-home`` branch.  Put another
way, we want to merge the ``work-from-home`` branch into our current branch,
``master``. What git command would do this action?  Scan the output of ``git
help`` for clues, then ``git help <command>`` when you've found the command
you need.

Do the merge.

.. prizerun::
    :hide:

    git merge work-from-home

Check the output of ``git branch -v`` again.

Have a look at the output of ``git slog``.

What do you see with ``git log --parents``?

Conflicts
=========

The merge that you just did should have been simple, with no conflicts.

Conflicts can occur when you have made changes to the same file on two
different branches, and you try and merge them.  If the changes are on or near
the same lines in the file, git will complain and ask you to work out which
changes you want to keep.

Make and checkout a new branch ``asking-for-trouble``.

.. prizerun::
    :hide:

    git branch asking-for-trouble
    git checkout asking-for-trouble
    echo "" >> our_paper.txt
    echo "Fourth sentence gets to the point." >> our_paper.txt
    git add our_paper.txt
    git commit -m "Advocate the fourth"

Edit ``our_paper.txt`` and add a sentence like "Fourth sentence gets to the
point."   Add to the staging area and then commit.

Checkout the ``master`` branch again.

Edit ``our_paper.txt`` and add a sentence like "Fourth sentence is still
warm-up."  Add to the staging area and commit.

.. prizerun::
    :hide:

    git checkout master
    echo "" >> our_paper.txt
    echo "Fourth sentence is still warm-up." >> our_paper.txt
    git add our_paper.txt
    git commit -m "Nay-say the fourth"

Now try merging the ``asking-for-trouble`` branch into our current
(``master``) branch. What do you see?

.. prizerun::
    :allow-fail:
    :hide:

    git merge asking-for-trouble

When the merge failed, git wrote some text into the file where the changes
clash.  ``our_paper.txt`` might look like this:

.. prizeout::

    cat our_paper.txt

The lines between ``<<<<<<< HEAD`` and ``=======`` are the changed lines from
the branch we are merging *into* (``master`` in our case).  The lines between
``=======`` and ``>>>>>>> asking-for-trouble`` are the changes from the branch
we are merging (``asking-for-trouble`` in our case).

Open the ``our_paper.txt`` file and remove the new marker lines in the text.
Choose how you'd like to combine your two different changes to the file.  When
the file is ready, save it, then add it to the staging area and do a commit.

Check all is well with ``git slog``.

.. prizerun::
    :hide:

    cat << EOF > our_paper.txt
    This is the first sentence of the new paper.

    Crucially, this is the second sentence.

    The third sentence starts the crescendo.

    Fourth sentence is still warm-up, then gets to the point.
    EOF
    git add our_paper.txt
    git commit -m "Resolve conflict"

The end
=======

Congratulations!  You now know the basics of working with a single git
repository.

.. include:: working/object_names.inc
