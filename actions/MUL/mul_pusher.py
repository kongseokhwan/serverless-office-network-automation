import smtplib
import sys
import getopt
import elasticsearch
from oslo_log import log as logging
from oslo_config import cfg
from elk_event_mapper import elk_event_mapper
import schema.ELK_EVENT_CONSTANTS as ELK_EVENT_CONSTANTS

LOG = logging.getLogger(__name__)
CONFIG_FILE = 'etc/mul_action.conf'

class mul_agent():
    def __init__(self):


def main(argv):
    # TODO : Define Action & Make API

    # Configuration Mapper
    opt_default_group = cfg.OptGroup(name='default', title='A default informations')
    default_opts = [
        cfg.StrOpt('sflow_index', default='kulcloud-error-*',
                    help=('Define Elastic Search Index Name')),
        cfg.StrOpt('sflow_type', default='logs',
                    help=('Define Elastic Search Type Name')),
        cfg.StrOpt('elk_addr', default='10.1.190.31:9200',
                    help=('Define Elastic Search Engine IP Address'))

    ]
    CONF = cfg.CONF
    CONF.register_group(opt_default_group)
    CONF.register_opts(default_opts, opt_default_group)
    CONF(default_config_files=[CONFIG_FILE])

    event = ''
    message = ''

    try:
        opts, args = getopt.getopt(argv,"hu:m:",["user_mail=","msg="])
    except getopt.GetoptError:
        print 'test.py -t <event_type> -m <message>'
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print 'test.py -t <event_type> -m <message>'
            sys.exit()
        elif opt in ("-t", "--event"):
            event = arg
        elif opt in ("-m", "--message"):
            message = arg

    if event not in ELK_EVENT_CONSTANTS.ELK_EVENT_LIST:
        print 'event is not defined'
        sys.exit(1)

    try:
        agent = mul_agent(CONF.default.elk_addr,
                           CONF.default.sflow_index,
                           CONF.default.sflow_type)
        agent.action_send_elk_log(event, message)

    except RuntimeError as e:
        LOG.error("%s SMTP Agent terminated!", e)
        sys.exit(1)

    sys.exit(1)

if __name__ == '__main__':
    main(sys.argv[1:])







