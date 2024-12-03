import subprocess

executable = './build/calculator'
input_data = '1\n-\n2'


#subprocess.run(executable, input=input_data, text=True, shell=False, capture_output=True)

print(subprocess.run(executable, input=input_data, text=True, shell=False, capture_output=True).stdout)

#echo -e "1\n+\n2" | ./build/calculator

# print("Return Code: ", result().returncode)
# print("Output: ", result().stdout)
# print("Error (if any): ", result().stderr)

