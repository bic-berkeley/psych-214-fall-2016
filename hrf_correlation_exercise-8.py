# This stuff needed to make exercise doctests / build pass
import nibabel as nib
data = nib.load('ds114_sub009_t2r1.nii').get_data()
data_no_0 = data[..., 1:]
neural_prediction = events2neural('ds114_sub009_t2r1_cond.txt', tr, data.shape[-1])
neural_prediction_no_0 = neural_prediction[1:]
