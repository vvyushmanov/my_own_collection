#!/usr/bin/python

# Copyright: (c) 2018, Terry Jones <terry.jones@example.org>
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
from __future__ import (absolute_import, division, print_function)
__metaclass__ = type
from os.path import exists
import os

DOCUMENTATION = r'''
---
module: create_text

short_description: This is a module to create text file on a remote host based on filename and path.

# If this is part of a collection, you need to use semantic versioning,
# i.e. the version is of the form "2.5.0" and not "2.4".
version_added: "1.0.0"

description: This module is a test module for a Netology DevOps course homework.

options:
    content:
        description: This is the content to be put into the file
        required: true
        type: str
    path:
        description:
            - Full path to the file on the host
            - Must include both the folder structure and the resulting filename
        required: ture
        type: str


author:
    - Vadim Yushmanov
'''

EXAMPLES = r'''
# Create a file with the given content
    - name: Test
      my_own_module:
        content: "This is a test content"
        path: "./test/test.txt"
'''

RETURN = r'''
# These are examples of possible return values, and in general should use other names for return values.
content:
    description: Contents read from the resulting file
    type: str
file_path:
    description: Location where the file is placed
    type: str
'''

from ansible.module_utils.basic import AnsibleModule


def run_module():
    # define available arguments/parameters a user can pass to the module
    module_args = dict(
        path=dict(type='str', required=True),
        content=dict(type='str', required=True)
    )

    # seed the result dict in the object
    # we primarily care about changed and state
    # changed is if this module effectively modified the target
    # state will include any data that you want your module to pass back
    # for consumption, for example, in a subsequent task
    result = dict(
        changed=False,
        content='',
        file_path=''
    )

    # the AnsibleModule object will be our abstraction working with Ansible
    # this includes instantiation, a couple of common attr would be the
    # args/params passed to the execution, as well as if the module
    # supports check mode
    module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=True
    )

    # if the user is working with this module in only check mode we do not
    # want to make any changes to the environment, just return the current
    # state with no modifications
    if module.check_mode:
        module.exit_json(**result)

    # manipulate or modify the state as needed (this is going to be the
    # part where your module will do what it needs to do)

    directory = os.path.dirname(module.params['path'])

    def write_file ():
        file = open(module.params['path'], "w")
        file.write(module.params['content'])
        result['changed'] = True         
    
    if exists(module.params['path']):
        curr_content = open(module.params['path'], "r").read()
        if curr_content != module.params['content']:
            write_file()
    else: 
        if not os.path.exists(directory):
            os.makedirs(directory)
        write_file()


    result['file_path'] = module.params['path']
    result['content'] = open(module.params['path'], "r").read()


    # in the event of a successful module execution, you will want to
    # simple AnsibleModule.exit_json(), passing the key/value results
    module.exit_json(**result)


def main():
    run_module()


if __name__ == '__main__':
    main()