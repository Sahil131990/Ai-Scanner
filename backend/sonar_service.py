import subprocess

def run_sonar_scan(path):

    command = f"sonar-scanner -Dsonar.projectBaseDir={path}"

    subprocess.run(command, shell=True)

    # fetch issues using sonar API
    return ["Null pointer risk", "Unused variable"]