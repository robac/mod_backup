from include.const import *

try:
    import syslog
except:
    SYSLOG = False


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
    sys.exit()
    return
# --END def exit_with_mail(msg)