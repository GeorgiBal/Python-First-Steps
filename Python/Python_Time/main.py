import time

print(time.ctime(0))  # shows epoch = when your computer thinks time began

print(time.time())  # return current seconds since epoch

print(time.ctime(time.time()))  # returns the current day and time

time_object = time.localtime()
print(time_object)  # returns current time information

utc_time = time.gmtime()  # returns UTC time
print(utc_time)

local_time = time.strftime("%B %d %Y %H:%M:%S", time_object)  # formats current time information
print(local_time)

time_string = "20 April, 2022"
time_format = time.strptime(time_string, "%d %B, %Y")  # converts time
print(time_format)

time_tuple = (2022, 4, 10, 4, 20, 0, 0, 0, 0)
chosen_time = time.asctime(time_tuple)  # convert tuple to time information
print(chosen_time)

epoch_time = time.mktime(time_tuple)  # convert tuple to seconds since epoch time
print(epoch_time)
