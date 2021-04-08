from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint
from configuration import Configuration
# create an instance of the API class
def border_msg(msg):
    row = len(msg)
    print("         ")
    h = ''.join(['+'] + ['-' *row] + ['+'])
    result= h + '\n'"|"+msg+"|"'\n' + h
    print(result)
    print("         ")
    time.sleep(0.5)

config=Configuration(ip="172.27.232.233")
api_instance = swagger_client.SystemApi(swagger_client.ApiClient(config))

### Testing API
## Testing Wifi
border_msg("TESTING API>SYSTEM>List WIFIs")
try:
    # Retrives an pose overlay image with a timestamp
    api_response = api_instance.list_wifis()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling list_wifis: %s\n" % e)


border_msg("TESTING API>SYSTEM>Connect WIFI BELL630_Ext")
wifi_config = swagger_client.ConnectWifi(bssid="58:EF:68:CD:92:B6",ssid="BELL630_Ext",password="6312E767D569") # ConnectWifi | BSSID, SSID, and Password (optional)
try:
    # Connect to WIFI network
    api_response = api_instance.set_wifi(wifi_config=wifi_config)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemApi->set_wifi: %s\n" % e)


border_msg("TESTING API>SYSTEM>Delete WIFI")
wifi_name = swagger_client.WifiName("BELL630_Ext") # WifiName | Status object that needs to be added to the database (optional)
try:
    # Delete WIFI network from the saved list
    api_response = api_instance.delete_wifi(wifi_name=wifi_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemApi->delete_wifi: %s\n" % e)


border_msg("TESTING API>SYSTEM>Get Status")
try:
    # Retreive the entire status of AXIBO
    api_response = api_instance.get_progress()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemApi->get_progress: %s\n" % e)


## Testing Motion
api_instance = swagger_client.MotionApi(swagger_client.ApiClient(config))
border_msg("TESTING API>Move>Home")
motorConfig = swagger_client.MotorHome(pan=True,tilt=True) # MotorHome | Home AXIBO motors (optional)
try:
    # Home AXIBO to set defualt limits
    api_response = api_instance.set_homing(motor_config=motorConfig)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MotionApi->set_homing: %s\n" % e)

border_msg("TESTING API>Move>Config +/-25 +/-10 ")
time.sleep(10)
motorConfig = swagger_client.MotorConfig(pan_min=-25,pan_max=25,tilt_max=10,tilt_min=-10) # MotorConfig | Specify the position and the speed to move AXIBO (optional)
try:
    # Move AXIBO to relative position
    api_response = api_instance.config_motors(motor_config=motorConfig)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MotionApi->config_motors: %s\n" % e)

border_msg("TESTING API>Move>Relative 20 20")
time.sleep(30)
position = swagger_client.ControlCMDPosition(pan=[50],tilt=[20])
velocity = swagger_client.ControlCMDPosition(pan=[5],tilt=[5])

motorConfig = swagger_client.ControlCMD(position=position,velocity=velocity) # ControlCMD | Specify the position and the speed to move AXIBO (optional)
try:
    # Move AXIBO to relative position
    api_response = api_instance.move_relative(motor_config=motorConfig)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MotionApi->move_relative: %s\n" % e)
    
border_msg("TESTING API>Move>Absolute 0 0 ")
time.sleep(20)
position = swagger_client.ControlCMDPosition(pan=[0],tilt=[0])
velocity = swagger_client.ControlCMDPosition(pan=[5],tilt=[5])

motorConfig = swagger_client.ControlCMD(position=position,velocity=velocity) # ControlCMD | Specify the position and the speed to move AXIBO (optional)
try:
    # Move AXIBO to absolute position
    api_response = api_instance.move_absolute(motor_config=motorConfig)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MotionApi->move_absolute: %s\n" % e)

border_msg("TESTING API>Move>Timed pan:10>20 tilt:5>10 times:1000ms,1000ms")
time.sleep(20)
position = swagger_client.ControlCMDPosition(pan=[10,20],tilt=[5,5])
timestamp = swagger_client.ControlCMDPosition(pan=[500,500],tilt=[1000,1000])

motorConfig = swagger_client.ControlCMD(position=position,timestamp=velocity) # ControlCMD | Specify the position and the speed to move AXIBO (optional)
try:
    api_response = api_instance.move_timed_abs(motor_config=motorConfig)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MotionApi->move_timed_abs: %s\n" % e)
