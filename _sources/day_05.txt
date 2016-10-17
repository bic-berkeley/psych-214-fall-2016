##############################################
October 10: exploring the general linear model
##############################################

***********
Python path
***********

* :doc:`using_pythonpath`;
* :download:`stimuli.py` file;
* :download:`test_stimuli.py` file;
* ::

    mkdir code
    mv stimuli.py code

* Install pytest if you haven't got it already::

    pip install pytest

* Show that the tests don't work yet::

    py.test test_stimuli.py

* Set Python path;
* Finally::

    mv test_stimuli.py code
    py.test code/test_stimuli.py

******************************
Simple and multiple regression
******************************

* finish going through the `introduction to the General Linear Model`_;
* we get the same results in R::

    psychopathy = c(11.416,   4.514,  12.204,  14.835,
                    8.416,   6.563,  17.343, 13.02,
                    15.19 ,  11.902,  22.721,  22.324)
    clammy = c(0.389,  0.2  ,  0.241,  0.463,
               4.585,  1.097,  1.642,  4.972,
               7.957,  5.585,  5.527,  6.964)
    res = lm(psychopathy ~ clammy)
    print(summary(res))

* :doc:`diag_inverse`;
* :doc:`subtract_mean_math`;
* :doc:`on_estimation_exercise`;
* on `matrix rank`_;
* :doc:`mean_test_example`.

*****************
Correlation again
*****************

* Make sure you have :download:`stimuli.py` and ``pearson.py`` on your Python
  path.  (``pearson.py`` comes from the exercise in :doc:`pearson_functions`);
* :doc:`correlation_2d_exercise`.

**********************************
Reading and homework for next week
**********************************

* Finish the :doc:`on_estimation_exercise` |--| see
  :doc:`github_glm_homework`;
* Do preliminary work on projects to prepare for project pitch next week.
