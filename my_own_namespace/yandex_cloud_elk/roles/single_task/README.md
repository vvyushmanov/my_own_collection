single_task
=========

This role creates a simple text file based on parameters.

Requirements
------------

No requirements.

Role Variables
--------------

| Variable | Description |
|----------|-------------|
| path  | Full path to a file to create |
| contents | String value to be written to the file |


Example Playbook
----------------

Including an example of how to use your role (for instance, with variables passed in as parameters) is always nice for users too:

    - hosts: localhost
      roles:
         - { role: single_task, contents: "Sample text" }

License
-------

MIT
