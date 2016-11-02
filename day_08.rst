##########################################
October 31: multiple comparison correction
##########################################

**********
Logistics
**********

* project presentations next week;
* proposal to redistribute 12 percentage points from homework to:

    * project: 50% to 60%
    * participation : 25% to 27%

 See: :doc:`logistics`.

* solutions to :doc:`dummies exercise <on_dummies_exercise>` at :doc:`dummies
  solutions <on_dummies_solution>`.

*******************
Choosing directions
*******************

* on code quality:

  http://www.samueljohnson.com/editing.html#536

    "I would say to Robertson what an old tutor of a college said to one of
    his pupils: 'Read over your compositions, and where ever you meet with a
    passage which you think is particularly fine, strike it out.'"

    Samuel Johnson in James Boswell's "Life of Samuel Johnson".

  There are some automated metrics, of which, be careful::

    pip3 install --user radon
    radon cc .

* learning to code well:

  * read other people's code;
  * review code;
  * make other people review your code;
  * pair coding.
  * "is this the right way to think of the problem?";
  * "have I expressed my thinking clearly in this code?";
  * "what guarantee can I give that the code is correct?;
  * "under what circumstances is the code correct?".

********
Teaching
********

* testing and coverage on the project repositories:

  Test results:

  * https://travis-ci.org/psych-214-fall-2016/project-red
  * https://travis-ci.org/psych-214-fall-2016/project-blue

  Test coverage:

  * https://codecov.io/gh/psych-214-fall-2016/project-red
  * https://codecov.io/gh/psych-214-fall-2016/project-blue

* testing, and t test volumes:

    * :doc:`validate_against_scipy`;
    * pdb++ : ``pip3 install --user pdbpp``;
    * Exercise::

        git clone https://github.com/psych-214-fall-2016/glmtools
        cd glmtools
        pip3 install --user --editable .
        py.test glmtools

* the `Bonferroni correction`_;
* thresholding with `Random fields`_;
* thresholding with the `False Discovery Rate`_;

.. other-stuff

    * family-wise error and FDR;
    * permutation and parametric;
    * small volume correction and ROI analysis.

**********************************
Reading and homework for next week
**********************************

* Prepare project presentations;
* `slice timing correction`_;
* `Rotation in 2D`_
* `optimizing spatial transformations`_.
