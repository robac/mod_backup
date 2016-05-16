class BaseModule:
    config = None;


    def __init__(self, config):
        self.config = config;
        return


    def get_default_config(self):
        raise NotImplementedError()
        return


    def proccess_configuration(self):
        raise NotImplementedError()
        return


    def do_backup(self):
        raise NotImplementedError()
        return
