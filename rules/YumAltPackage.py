from ansiblelint import AnsibleLintRule

class YumAltPackage(AnsibleLintRule):
    id = 'E403'
    shortdesc = 'Use Package module instead of Yum module'
    description = ''
    tags = ['yum']

    def matchtask(self, file, task):
        if task['action']['__ansible_module__'] == 'yum':
            return True
        return False
