# Remote Health Care Using IOT

### Objective
- To create a system where the patient can send their health related data (here, ECG data is used) from sensor to a doctor for checkup over the internet for remote health care.

### Proposed Solution
![solution](https://user-images.githubusercontent.com/29419943/70080836-68751900-162f-11ea-9810-29d1103a0949.png)

### Tools and Technologies Used
##### Hardware
1. NodeMCU
- Microcontroller with built-in wifi-module.
- Programming can be done in Arduino IDE.
- It is used to send ECG data to web server in this project.
2. ECG sensor (AD8232)
- It measures electrical activity of the heart.
- Data obtained from it can be used to plot ECG graph.
- Patient’s data obtained from this sensor is sent to NodeMCU.
##### Software
1. Django
- Python based web framework
- Used for backend development
2. HTML, CSS, Javascript and Bootstrap
- Used for frontend development
3. MySQL
- Used for database management
4. Amazon Web Services (AWS)
- Used for hosting website
5. Arduino IDE
- Used for programming NodeMCU
