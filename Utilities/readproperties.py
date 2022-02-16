import configparser

config=configparser.RawConfigParser()
config.read("D:\python Q\e-commerce\configuration\config.ini")

class reading():

     @staticmethod
     def getappurl():
         url=config.get('common info','baseurl')
         return url

     @staticmethod
     def getusername():
         username = config.get('common info', 'username')
         return username

     @staticmethod
     def getpassword():
         password = config.get('common info', 'password')
         return password
