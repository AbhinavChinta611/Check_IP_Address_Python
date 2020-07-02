import socket as s
hostname = s.gethostname()    
IPAddr = s.gethostbyname(hostname)    
print("Your Computer Name is : " + hostname)    
print("Your Computer IP Address is : " + IPAddr)  
