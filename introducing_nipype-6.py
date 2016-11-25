import nipype.interfaces.matlab as nim
mlab = nim.MatlabCommand()
mlab.inputs.script = "version"  # get MATLAB version
mlab.run()
# <...>
