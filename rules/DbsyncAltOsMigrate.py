from ansiblelint import AnsibleLintRule

class DbsyncAltOsMigrate(AnsibleLintRule):
    id = 'E514'
    shortdesc = 'Avoid to use x-manage db sync instead of openstack-db --service x --update'
    description = ''
    tags = ['shell', 'command']

    def match(self, file, text):
        if 'db sync' in text:
            return True
        return False
