
# I can import a standalone module that is located in the same directory
import sys 
sys.path.append("C:/Repos/Udemy_Python_Bootcamp/Python Scripts/my_pkg")
from my_module import my_fcn
import my_main_script
from my_sub_pkg import my_sub_script

my_fcn()
my_main_script.report_main()
my_sub_script.sub_report()