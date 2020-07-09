# implemented by Michael Pabst

import rosbag
import numpy as np
import matplotlib.pyplot as plt
import sys
import pdb
from openpyxl import Workbook # pip install openpyxl 
from openpyxl.styles import Font, Color, colors
import os


# read messages 
def readmsg_turtle_vel(topic_name_1):
	global bag
	count_msg = bag.get_message_count(topic_name_1) 
	# set arrays to store data
	data1 = []
	data2 = []
	data3 = []
	data4 = []
	data5 = []
	data6 = []

	# set a flag
	# loop over the topic to read evey message
	for topic, msg, t in bag.read_messages(topics=topic_name_1):
		data1.append(msg.linear.x)
		data2.append(msg.linear.y)
		data3.append(msg.linear.z)
		data4.append(msg.angular.x)
		data5.append(msg.angular.y)
		data6.append(msg.angular.z)

	#convert list to array
	data1 = np.array(data1)
	data2 = np.array(data2)
	data3 = np.array(data3)
	data4 = np.array(data4)
	data5 = np.array(data5)
	data6 = np.array(data6)
	data_turtle_vel = np.vstack([data1,data2,data3,data4,data5,data6])

	return [data_turtle_vel, count_msg,data1]

def calcErrorturtle_vel(data_turtle_vel,count_msg):

	var = data_turtle_vel
	error_mean_all = var[0,:]
	mean_value = np.mean(var[0,:])

	sum_error_turtle_vel = mean_value

	return sum_error_turtle_vel

def main():
	#bagfile
	path = '/home/michaelpabst2/rosbag_reader/rosbags'
	out_dir = '/home/michaelpabst2/rosbag_reader/results'
	items = os.listdir(path)
	group = "turtle"
	for i in [items[0]]:
		name = i[:-4]
		print(name)

		bagfile_txt = "{}.txt".format(name)
		bagfile = '{}'.format(name)

		excel_turtle_vel_plot = 'cen_plot_{}.xlsx'.format(name)

		# choose one topic  
		global bag
		bag  = rosbag.Bag(os.path.join(path,i))
		topic_name_1 = '/turtle1/cmd_vel'  
		data_turtle_vel,count_msg,data1 = readmsg_turtle_vel(topic_name_1)
		
		sum_error_turtle_vel= calcErrorturtle_vel(data_turtle_vel,count_msg)

		#############################################################################


		#save data in file
		outputdir = os.path.join(out_dir, group, name[:name.find('_')])
		if not os.path.exists(outputdir):
			os.makedirs(outputdir)

		with open(os.path.join(outputdir, bagfile_txt),"w") as f:
			f.write(group+'\n')
			f.write('bag-file:{}\n'.format(bagfile))
			f.write('error_turtle_vel:{}\n'.format(str(sum_error_turtle_vel)))

		f.close()

		# ############################################################################

		# save data for plots
		# turtle_vel
		listA = data1
		L=[listA]
		wb = Workbook()
		ws1 = wb.active # work sheet
		ws1.title = "turtle_vel"
		for i in range(len(listA)):
			for j in range (len(L)):
					_ = ws1.cell(column=j+1, row=i+1, value=L[j][i])

		ft_b = Font(name='Calibri',color=colors.BLACK, bold=False, size=11)
		a1 = ws1['A1']
		b1 = ws1['B1']
		a1.font = ft_b
		b1.font = ft_b

		wb.save(os.path.join(outputdir, excel_turtle_vel_plot))

		###########################################################################  

	
if __name__ == '__main__':
	main()
	global bag
	bag.close()