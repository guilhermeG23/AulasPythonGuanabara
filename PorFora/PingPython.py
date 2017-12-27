from subprocess import check_output
print(check_output("ping www.facebook.com\n", shell=True))

