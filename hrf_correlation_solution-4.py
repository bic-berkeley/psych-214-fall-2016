#: Read in stimulus file, return neural prediction
def events2neural(task_fname, tr, n_trs):
    """ Return predicted neural time course from event file
# ...
    Parameters
    ----------
    task_fname : str
        Filename of event file
    tr : float
        TR in seconds
    n_trs : int
        Number of TRs in functional run
# ...
    Returns
    -------
    time_course : array shape (n_trs,)
        Predicted neural time course, one value per TR
    """
    task = np.loadtxt(task_fname)
    if task.ndim != 2 or task.shape[1] != 3:
        raise ValueError("Is {0} really a task file?", task_fname)
    task[:, :2] = task[:, :2] / tr
    time_course = np.zeros(n_trs)
    for onset, duration, amplitude in task:
        time_course[onset:onset + duration] = amplitude
    return time_course
