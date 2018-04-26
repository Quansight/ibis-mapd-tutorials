hosts = __import__('configparser').ConfigParser()
hosts.read('connections.ini');