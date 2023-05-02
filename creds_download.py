# copy config-env as config
from shutil import copy2
import sys
from os import path

# copy the tools config by default
if len(sys.argv) < 2:
    env = 'tools'
else:
    env = sys.argv[1]

home_dir = path.expanduser('~')
print(f'copy {home_dir}\Downloads\credentials to {home_dir}\.aws\credentials-{env}')
copy2(f'{home_dir}\Downloads\credentials',f'{home_dir}\.aws\credentials-{env}')
print(f'copy {home_dir}\.aws\credentials-{env} to {home_dir}\.aws\credentials')
copy2(f'{home_dir}\.aws\credentials-{env}', f'{home_dir}\.aws\credentials')
