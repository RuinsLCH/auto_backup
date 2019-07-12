import sys
from subprocess import Popen, PIPE


def execute_command(command, description):
    print(description),
    sys.stdout.flush()  # update message
    execution = Popen(command, shell=True, stdout=PIPE, stderr=PIPE)  # ecxcute command and print ouput
    output, error = execution.communicate()
    if len(output.decode('utf-8')) >= 1:
        print(output.decode('utf-8'))
    if execution.returncode:  # return true or false
        print ('/n')
        print(error.decode("utf-8")) #decode translate to utf-8
        sys.stdout.flush()
        print('not Done')
        exit(1)
    print('Done')
    sys.stdout.flush()



execute_command("cd C:/Users/iDisplay/Desktop/auto_backup/auto_backup", "cd to project path")
execute_command("git add --all", "add all")
execute_command("git commit -m \"push test\"","test for commit")
execute_command("git push", "push to github")