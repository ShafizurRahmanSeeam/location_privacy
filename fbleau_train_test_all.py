import subprocess

# Define the commands to run, corrected for apparent path errors
commands = [

    r' python split_train_test_fbleau.py C:\Users\ss6365\Desktop\location_privacy_final\geolife\machine_learning\attack1 C:\Users\ss6365\Desktop\location_privacy_final\geolife\fbleau\train C:\Users\ss6365\Desktop\location_privacy_final\geolife\fbleau\test',
    r' python check.py "C:\Users\ss6365\Desktop\location_privacy_final\geolife\fbleau\train" "C:\Users\ss6365\Desktop\location_privacy_final\geolife\fbleau\test"',

    r' python split_train_test_fbleau.py C:\Users\ss6365\Desktop\location_privacy_final\tdrive\machine_learning\attack1 C:\Users\ss6365\Desktop\location_privacy_final\tdrive\fbleau\train C:\Users\ss6365\Desktop\location_privacy_final\tdrive\fbleau\test',
    r' python check.py "C:\Users\ss6365\Desktop\location_privacy_final\tdrive\fbleau\train" "C:\Users\ss6365\Desktop\location_privacy_final\tdrive\fbleau\test"',

   
   r' python split_train_test_fbleau.py C:\Users\ss6365\Desktop\location_privacy_final\uci\machine_learning\attack1 C:\Users\ss6365\Desktop\location_privacy_final\uci\fbleau\train C:\Users\ss6365\Desktop\location_privacy_final\uci\fbleau\test',
   r' python check.py "C:\Users\ss6365\Desktop\location_privacy_final\uci\fbleau\train" "C:\Users\ss6365\Desktop\location_privacy_final\uci\fbleau\test"',

    r' python split_train_test_fbleau.py C:\Users\ss6365\Desktop\location_privacy_final\collected\machine_learning\attack1 C:\Users\ss6365\Desktop\location_privacy_final\collected\fbleau\train C:\Users\ss6365\Desktop\location_privacy_final\collected\fbleau\test',
    r' python check.py "C:\Users\ss6365\Desktop\location_privacy_final\collected\fbleau\train" "C:\Users\ss6365\Desktop\location_privacy_final\collected\fbleau\test"',

 

#    r' python split_train_test_fbleau.py C:\Users\ss6365\Desktop\location_privacy_final\tdrive\machine_learning\attack20 C:\Users\ss6365\Desktop\location_privacy_final\tdrive\fbleau_20\train C:\Users\ss6365\Desktop\location_privacy_final\tdrive\fbleau_20\test',
#    r' python check.py "C:\Users\ss6365\Desktop\location_privacy_final\tdrive\fbleau_20\train" "C:\Users\ss6365\Desktop\location_privacy_final\tdrive\fbleau_20\train"',

#    r' python split_train_test_fbleau.py C:\Users\ss6365\Desktop\location_privacy_final\tdrive\machine_learning\attack30 C:\Users\ss6365\Desktop\location_privacy_final\tdrive\fbleau_30\train C:\Users\ss6365\Desktop\location_privacy_final\tdrive\fbleau_30\test',
#    r' python check.py "C:\Users\ss6365\Desktop\location_privacy_final\tdrive\fbleau_30\train" "C:\Users\ss6365\Desktop\location_privacy_final\tdrive\fbleau_30\train"',

#    r' python split_train_test_fbleau.py C:\Users\ss6365\Desktop\location_privacy_final\tdrive\machine_learning\attack40 C:\Users\ss6365\Desktop\location_privacy_final\tdrive\fbleau_40\train C:\Users\ss6365\Desktop\location_privacy_final\tdrive\fbleau_40\test',
#    r' python check.py "C:\Users\ss6365\Desktop\location_privacy_final\tdrive\fbleau_40\train" "C:\Users\ss6365\Desktop\location_privacy_final\tdrive\fbleau_40\train"',

#    r' python split_train_test_fbleau.py C:\Users\ss6365\Desktop\location_privacy_final\tdrive\machine_learning\attack50 C:\Users\ss6365\Desktop\location_privacy_final\tdrive\fbleau_50\train C:\Users\ss6365\Desktop\location_privacy_final\tdrive\fbleau_50\test',
#    r' python check.py "C:\Users\ss6365\Desktop\location_privacy_final\tdrive\fbleau_50\train" "C:\Users\ss6365\Desktop\location_privacy_final\tdrive\fbleau_50\train"',
  
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
