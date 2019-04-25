class STModule:
    def __init__(self):
        self.name = 'ipy/persistence'
        self.language = 'ipy'
        self.description = 'Persistence'
        self.author = '@maximemf'
        self.options = {}

    def payload(self):
        with open('modules/ipy/src/persistence.py', 'r') as module_src:
            src = module_src.read()
            return src
