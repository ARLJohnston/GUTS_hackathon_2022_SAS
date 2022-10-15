from certifi import where
import data_collection as dc

def get_point_time(time):
    student_times = dc.security_data.copy()
    student_times[['Start', 'End']] = student_times['Time'].str.split('-', 1, expand=True).to_numpy()
    student_times = student_times.drop('Time',axis=1)
    student_times['Start'] = student_times['Start'].astype(int)
    student_times['End'] = student_times['End'].astype(int)

   
    student_times_array = student_times.to_numpy()
    #print(student_times_array)
    next_day_mask = dc.np.array(student_times_array[:,3] > student_times_array[:,4])
    student_times_array[next_day_mask,4] += 2400
    print(student_times_array.shape)
    #student_times_array[:,4] = dc.np.where(,student_times_array[:,4],student_times_array[:,4]+2400)

    mask = dc.np.where((student_times_array[:,3] < time)&(student_times_array[:,4] > time))
    
    return student_times_array[mask]
    




print(get_point_time(2400))
