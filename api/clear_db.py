import subprocess

script_name = "clear_db.sh"

subprocess.run(["bash", script_name])
print("Database cleared")