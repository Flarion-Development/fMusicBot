from colorama import Fore, Style
import datetime

class Logger:
    @staticmethod
    def _get_time():
        return datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    @staticmethod
    def _get_module_name(module):
        return module.__class__.__name__ if hasattr(module, '__class__') else str(module)

    @staticmethod
    def log(message: str, source: str = "General"):
        print(f"{Style.BRIGHT}{Fore.GREEN}[Log]{Style.RESET_ALL} | {Logger._get_time()} | Source: {source} | {message}")

    @staticmethod
    def warn(message: str, source: str = "General"):
        print(f"{Style.BRIGHT}{Fore.YELLOW}[Warn]{Style.RESET_ALL} | {Logger._get_time()} | Source: {source} | {message}")

    @staticmethod
    def error(message: str, source: str = "General"):
        print(f"{Style.BRIGHT}{Fore.RED}[Error]{Style.RESET_ALL} | {Logger._get_time()} | Source: {source} | {message}")


Logger.warn("Bu Bir Uyarı Mesajıdır", source="TestModule")
Logger.error("Bu Bir Hata Mesajıdır", source="TestModule")
Logger.log("Bu Bir Bilgi Mesajıdır", source="TestModule")