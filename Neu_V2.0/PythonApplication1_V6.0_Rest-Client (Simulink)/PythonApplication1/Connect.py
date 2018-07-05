import requests
import time
import json

class Input():
    
    def save_to_rest(self,Stellwerte):

        self.Stellwerte=Stellwerte;
        data_values=self.Stellwerte;
        url = 'http://localhost:8000/input/'
        data = dict(zip(data_values[0:8],data_values[8:16]))
        response = requests.post(url, json=data)
        return response.status_code 


class Output():

    def get_from_rest(self):

        url = 'http://localhost:8000/output/'
        r = requests.get(url)
        if r.status_code == 200:       
            json_list = r.json()
            for i in range(0,len(json_list)):
                data.append(json_list[u'Value'+str(i+1)]);
        return r.status_code 