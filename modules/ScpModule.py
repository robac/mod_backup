from include import BaseModule

DEFAULT_CONFIG = {
    'module' : 'scp'
}


class ScpModule(BaseModule.BaseModule):
    def test(self):
        print ("module scp");
        return

    def get_default_config(self):
        return DEFAULT_CONFIG;

    def proccess_configuration(self):
        raise NotImplementedError()
        return

    def do_backup(self):
        raise NotImplementedError()
        return

