import os
import subprocess

class TerraformManager:
    def provision_resource(self, config_file):
        command = f"terraform apply -auto-approve {config_file}"
        process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE)
        process.wait()
        return f"Resource provisioned using config: {config_file}"
