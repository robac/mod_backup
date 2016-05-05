  #IMPORT SECTION
import sys;
import json;
import os;
import os.path;
import pprint;

try:
    import syslog
    SYSLOG = True
except:
    SYSLOG = False

sys.path.append('modules')

#CONSTANTS SECTION
ARGUMENT_TEST = '-t'
ARGUMENT_MAIL = '-m'

SECTION_GLOBAL = 'global';


#GLOBAL VARIABLES SECTION
arguments = {
    'test_mode' : False,
    'config_file' : '',
    'mail_address' : ''
}

config = {
}


#FUNCTIONS SECTION
def log(*args):
    if (len(args) == 0):
        return
    elif (len(args) == 1):
        msg = args[0]
    else:
        msg = args[0] % args[1:]
    if (SYSLOG or arguments['test_mode']):
        syslog.syslog(msg)
    else:
        print(msg)
# --END def log(msg):


def die_with_message(*args):
    log(*args)
    sys.exit();
    return
# --END def exit_with_mail(msg)


def check_arguments():
    index = 1
    while (index < len(sys.argv)):
        item = sys.argv[index]
        if (item == ARGUMENT_TEST):
            arguments['test_mode'] = True
        elif (item == ARGUMENT_MAIL):
            if (index+1 < len(sys.argv)):
                index += 1
                arguments['mail_address'] = sys.argv[index]
            else:
                die_with_message("Missing argument (mail address)!")
        else:
            arguments['config_file'] = item

        index += 1

    if (arguments['config_file'] == ''):
        arguments['config_file'] = create_main_config_file_path()
# --END def check_arguments()


def create_main_config_file_path():
    root, ext = os.path.splitext(sys.argv[0]);
    return root + '.conf';
# --END def generate_config_file_name()


def create_sub_config_file_path(partial_path):
    global arguments
    if (os.path.exists(partial_path)):
        return partial_path;
    else:
        path, tmp = os.path.split(arguments['config_file'])
        path = os.path.join(path, partial_path);
        if (os.path.exists(path)):
            return path;
        else:
            die_with_message('Can not find sub configuration file %s!', partial_path);
    return
# --END def create_sub_config_file_path()


def load_config(path):
    if ( not os.path.exists(path)):
        die_with_message('Configuration file %s does not exists!', path);
    try:
        with open(path) as conf_file:
            config = json.load(conf_file)
            #config.
    except:
        log(sys.exc_info()[0]);
        log(sys.exc_info()[1]);
        die_with_message('Error proccessing config file %s!', arguments['config_file'])

    return config
# --END def load_config()


def compose_config():
    global config;
    for section in config.keys():
        if (section == SECTION_GLOBAL):
            continue
        elif (isinstance(config[section], dict)):
            continue
        elif (isinstance(config[section], str)):
            path = create_sub_config_file_path(config[section]);
            config[section] = load_config(path);
        else:
            die_with_message('Unknow configuration file format in section %s!', section);
# --END def discover_config()


def main():
    global config;
    check_arguments();
    config = load_config(arguments['config_file']);
    compose_config();
# --END def main()

#PROGRAM
main()
xx = __import__('var_backup_scp');
xx.test()







