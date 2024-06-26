import subprocess

# Define the commands to run, corrected for apparent path errors
commands = [
    #r"python fbleau.py C:\\Users\\ss6365\\Desktop\\location_privacy_final\\uci\\fbleau ln",
    #r"python fbleau.py C:\\Users\\ss6365\\Desktop\\location_privacy_final\\uci\\fbleau log10",
    #r"python fbleau.py C:\\Users\\ss6365\\Desktop\\location_privacy_final\\\\uci\\\\fbleau ln",
    #r"python fbleau.py C:\\Users\\ss6365\\Desktop\\location_privacy_final\\\\uci\\\\fbleau log10",
    #r"python fbleau.py C:\\Users\\ss6365\\Desktop\\location_privacy_final\\\uci\\\fbleau ln",
    #r"python fbleau.py C:\\Users\\ss6365\\Desktop\\location_privacy_final\\\uci\\\fbleau log10",
    #r"python fbleau.py C:\\Users\\ss6365\\Desktop\\location_privacy_final\\uci\\fbleau ln",
    #r"python fbleau.py C:\\Users\\ss6365\\Desktop\\location_privacy_final\\uci\\fbleau log10",

    r"python fbleau.py C:\\Users\\ss6365\\Desktop\\location_privacy_final\\uci\\fbleau ln",
    r"python fbleau.py C:\\Users\\ss6365\\Desktop\\location_privacy_final\\collected\\fbleau ln",
    r"python fbleau.py C:\\Users\\ss6365\\Desktop\\location_privacy_final\\geolife\\fbleau ln",
    r"python fbleau.py C:\\Users\\ss6365\\Desktop\\location_privacy_final\\tdrive\\fbleau ln",


]

# Execute each command sequentially
for command in commands:
    print(f"Executing: {command}")
    # Using shell=True can be a security hazard with untrusted input. Since you control the strings here, it should be okay.
    result = subprocess.run(command, shell=True, check=True)
    if result.returncode == 0:
        print("Command executed successfully.")
    else:
        print("Command failed.")
        break  # If a command fails, break the loop to avoid proceeding with dependent commands

print("All commands executed.")
