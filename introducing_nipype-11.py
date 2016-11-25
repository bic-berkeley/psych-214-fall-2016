import nipype_settings
import nipype.interfaces.matlab as nim
mlab = nim.MatlabCommand()
mlab.inputs.script = "spm ver"  # get SPM version
mlab.run()
# <...>
