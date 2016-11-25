#- Initialize the SliceTiming batch object, and fill parameters
#- Run the slice timing on the fixed image `fds114_sub009_t2r1.nii`
st = SliceTiming()
st.inputs.in_files = 'fds114_sub009_t2r1.nii'
st.inputs.num_slices = num_slices
st.inputs.time_repetition = TR
st.inputs.time_acquisition = TA
st.inputs.slice_order = acq_order
st.inputs.ref_slice = 1
