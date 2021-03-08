current_os = platform.system().lower()
if current_os == "windows":
    parameter = "-n"
else:
    parameter = "-c"

ip = "127.0.0.1"
exit_code = os.system(f"ping {parameter} 1 -w2 {ip} > /dev/null 2>&1")

print(exit_code == 0)
