import paho.mqtt.client as paho  		    #mqtt library
import os
import json
import time
from datetime import datetime
import random

ACCESS_TOKEN='O4G4nbwK2XIOIf2Ido3e'                 #Token of your device 
broker="demo.thingsboard.io"   			    #host name
port=1883 					    #data listening port
def on_publish(client,userdata,result):             #create function for callback
    print("data published to thingsboard \n")
    pass
client1= paho.Client("control1")                    #create client object
client1.on_publish = on_publish                     #assign function to callback
client1.username_pw_set(ACCESS_TOKEN)               #access token from thingsboard device
client1.connect(broker,port,keepalive=60)           #establish connection
btstatus=float(100)

while btstatus > 5:
    a=random.randint(0,80)
    b=random.randint(5,50)
    #x1=round(random.uniform(30,50),2)
    #y1=round(random.uniform(45,55),2)
    #x2=round(random.uniform(30,50),2)
    #y2=round(random.uniform(45,55),2)
    xref=18.499880
    yref=73.858743
    ##------------------------------------------------------------------
    '''
    18.499818,73.858651 swargaate ref

    18.520503,73.855677 shaniwar
    18.508278,73.831258 erandwane
    18.490892,73.845184 sahakar
    18.507008,73.87938  camp
    18.468872,73.863895 KK
    '''
    '''
    x=[18.520503,18.508278,18.490892,18.507008,18.468872]
    y=[73.855677,73.831258,73.845184,73.87938,73.863895]
    '''
    x=[18.520503,18.508278,18.490892,18.507008,18.468872]
    y=[73.855677,73.831258,73.845184,73.87938,73.863895]
    
    uid=[121,122,123,124,125]
    issues=['facing_connectivity_issue','network_issue','battery_drain_detected','error_sending_telemetry','rotar_issue_detected','temperature_exceeding_threshold']
    issuecode=[0,1,2,3,4,5]

    for i in range(len(x)-1):
        xmid=[]
        ymid=[]
        a=x[i+1]-x[i]
        b=y[i+1]-y[i]
        #--------------------------------------
        def split_equal(value, parts):
            value = float(value)
            c=[i*value/parts for i in range(1,parts+1)]
            return c

            d=split_equal(a,3)
            e=split_equal(b,3)
            for j in range(3):
                x[i]+=d[j]
                y[i]+=d[j]
                xmid.append(x[i])
                ymid.append(y[i])
                #print(xmid,ymid)
        #--------------------------------------

        #for i in range(2):
        drstatus=random.randint(0,50)
        btdiff=round(random.uniform(0,4),2)
        btstatus=round((btstatus-btdiff),2)
        #payload ="{"+"\"x\":"+str(x[i])+",\"y\":"+str(y[i])+",\"uid\":"+str(uid[i])+",\"drone_status\":"+str(drstatus)+",\"battery_status\":"+str(btstatus)+","
        #payload+="\"xref\":"+str(xref)+",\"yr ef\":"+str(yref)+"}"
        payload ="{"+"\"x\":"+str(x[i])+",\"y\":"+str(y[i])+",\"uid\":"+str(uid[i])+",\"drone_status\":"+str(drstatus)+",\"battery_status\":"+str(btstatus)+",\"fault\":"+str(random.choice(issues))+","#+","
        payload+="\"delivery\":"+str('package_delivered')+"}"#"\"xref\":"+str(xref)+",\"yref\":"+str(yref)+",\"xmid\":"+str(xmid[i])+",\"ymid\":"+str(ymid[i])+"}"
        ret= client1.publish("v1/devices/me/telemetry",payload) #topic-v1/devices/me/telemetry
        print(payload);
        time.sleep(5)
        payload ="{"+"\"x\":"+str((x[i]+x[i+1])/2)+",\"y\":"+str((y[i]+y[i+1])/2)+",\"uid\":"+str(uid[i])+",\"drone_status\":"+str(drstatus)+",\"battery_status\":"+str(btstatus)+","#"}"
        payload+="\"delivery\":"+str('estimated_arrival_in_'+str(drstatus)+'_mins')+"}"#"\"xref\":"+str(xref)+",\"yref\":"+str(yref)+",\"xmid\":"+str(xmid[i])+",\"ymid\":"+str(ymid[i])+"}"
        ret= client1.publish("v1/devices/me/telemetry",payload) #topic-v1/devices/me/telemetry
        print(payload);
        time.sleep(5)
        
    payload ="{"+"\"x\":"+str(x[4])+",\"y\":"+str(y[4])+",\"uid\":"+str(uid[4])+",\"drone_status\":"+str(drstatus)+",\"battery_status\":"+str(btstatus)+",\"delivery\":"+str('package_delivered')+"}"#+","
    #payload+="\"xref\":"+str(xref)+",\"yref\":"+str(yref)+",\"xmid\":"+str(xmid[i])+",\"ymid\":"+str(ymid[i])+"}"
    ret= client1.publish("v1/devices/me/telemetry",payload) #topic-v1/devices/me/telemetry
    print(payload);
    time.sleep(5)
    
print("Battery exhausted, safely landing to ground")












   
