import data_collection as dc

def get_point_time(time):
    student_times = dc.security_data.copy()
    student_times[['Start', 'End']] = student_times['Time'].str.split('-', 1, expand=True).to_numpy()
    student_times = student_times.drop('Time',axis=1)
    student_times['Start'] = student_times['Start'].astype(int)
    student_times['End'] = student_times['End'].astype(int)
   
    student_times_array = student_times.to_numpy()
    #print(student_times_array)
    
    
    mask = dc.np.where((student_times_array[:,3] < time)&(student_times_array[:,4] > time))
   
    print(student_times_array[mask])

  
    #mask = dc.np.where(dc.np.all(dc.np.char.strip(student_times_array[:,3])<str(time) , dc.np.char.strip(student_times_array[:,4])>str(time)),student_times_array,None) 
  
    #splitted_sec = splitted_sec[mask]
    #print(splitted_sec)


#print(dc.get_security_time())
get_point_time(350)
