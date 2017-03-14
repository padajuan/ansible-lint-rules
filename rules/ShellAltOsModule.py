from ansiblelint import AnsibleLintRule

class ShellAltOsModule(AnsibleLintRule):
    id = 'E513'
    shortdesc = 'Avoid to use Shell with an Openstack command instead of os_module'
    description = ''
    tags = ['shell', 'command']

    def matchtask(self, file, task):
        command_list = ['cinder', 'glance', 'neutron', 'nova', 'ceilometer', 'keystone', 'heat' ]
        if task['action']['__ansible_module__'] not in ['shell', 'command']:
            return False

        for shell_command in command_list:
            if shell_command in task['action']['__ansible_arguments__']:
                return True
        return False
