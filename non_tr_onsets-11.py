for hr_onset, hr_duration, amplitude in zip(
           high_res_onset_indices, high_res_durations, amplitudes):
    hr_onset = int(round(hr_onset))  # index - must be int
    hr_duration = int(round(hr_duration))  # makes index - must be int
    high_res_neural[hr_onset:hr_onset + hr_duration] = amplitude
plt.plot(high_res_times, high_res_neural)
# [...]
plt.xlabel('Time (seconds)')
# <...>
plt.ylabel('High resolution neural prediction')
# <...>
