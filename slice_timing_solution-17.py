#- Divide acquisition_order by number of slices, multiply by TR
time_offsets = acquisition_order / 30 * TR
time_offsets
# array([ 0.    ,  1.25  ,  0.0833,  1.3333,  0.1667,  1.4167,  0.25  ,
# 1.5   ,  0.3333,  1.5833,  0.4167,  1.6667,  0.5   ,  1.75  ,
# 0.5833,  1.8333,  0.6667,  1.9167,  0.75  ,  2.    ,  0.8333,
# 2.0833,  0.9167,  2.1667,  1.    ,  2.25  ,  1.0833,  2.3333,
# 1.1667,  2.4167])
