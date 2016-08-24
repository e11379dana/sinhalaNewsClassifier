import ConfigParser
import os

class ConfigSectionMap:

    def _get_config(self):
        Config = ConfigParser.ConfigParser()
        return Config

    def GetConfigSections(self):
        Config = self._get_config()
        absPath = os.path.join(os.path.dirname(__file__), 'config.ini')
        Config.read(absPath)

        return Config.sections()


    def ConfigSectionMap(self,section):
        Config = self._get_config()
        absPath = os.path.join(os.path.dirname(__file__), 'config.ini')

        Config.read(absPath)
        dict1 = {}
        options = Config.options(section)
        for option in options:
            try:
                dict1[option] = Config.get(section, option)
                if dict1[option] == -1:
                    print("skip: %s" % option)
            except:
                print("exception on %s!" % option)
                dict1[option] = None
        return dict1

