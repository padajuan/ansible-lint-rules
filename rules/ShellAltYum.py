from ansiblelint import AnsibleLintRule

class ShellAltYum(AnsibleLintRule):
    id = 'E516'
    shortdesc = 'Use package module instead of Shell or Command execution'
    description = ''
    tags = ['shell', 'command']

    def matchtask(self, file, task):
        if task['action']['__ansible_module__'] not in ['shell', 'command']:
            return False
        if 'yum' in task['action']['__ansible_arguments__']:
            return True
        return False
