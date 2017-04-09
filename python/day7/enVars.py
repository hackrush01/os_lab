import os
# print("All Env vars: ", os.environ)
print("Details of only PATH variable: ", os.environ['PATH'])
print("Details of only HOME variable: ", os.environ['HOME'])
print("Details of only TERM variable: ", os.environ['TERM'])
print("Current working directory: ", os.getcwd())
os.chdir("/root/OS_LAB_IT/python")
print("Current working directory: ", os.getcwd())
print("Group ID connected with present process: ", os.getgid())
print("User ID connected with present process: ", os.getuid())
print("List of group IDs", os.getgroups())
print("Get present process ID: ", os.getpid())
print("Get parent process ID: ", os.getppid())