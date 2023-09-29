import win32serviceutil  
import win32service  
import win32event  
import servicemanager  
import socket  
import sys  
  
def main():  
    # 禁用无关的服务  
    services = ['RemoteRegistry', 'SyncHost', 'P2PUpnP', 'Netproofer']  
    for service in services:  
        try:  
            win32serviceutil.ChangeServiceConfig(service, starttype=win32service.SERVICE_DISABLED)  
            print(f'Service {service} disabled')  
        except Exception as e:  
            print(f'Error disabling service {service}: {e}')  
  
if __name__ == '__main__':  
    main()
