# Remote Health Care Using IOT

### Table of Contents
1. Objective
2. Problems
3. Literature Review
4. Proposed Solution
5. Tools and Technologies Used
6. Prototyping on Breadboard
7. Final PCB
8. Website
9. Project Demonstration
10. Output of ECG graph
11. Further Work
12. Conclusion
13. References

### Objective
- To create a system where the patient can send their health related data (here, ECG data is used) from sensor to a doctor for checkup over the internet for remote health care.

### Problems
- Doctor to population ratio in rural areas of Nepal = 1:150000
- Difficult for disabled and elderly people to visit hospital regularly.
- People do not have spare time to visit hospital for their regular health check-up.
- Carrying all the previous medical records for health check-up is tedious for a person.

## Literature Review
- Pilot program was launched in Gulmi District of Nepal where health workers were provided with a free phone number to call three General Practitioner Doctors in the District Hospital.
- In some district hospitals of Nepal, an Internet connection, computer and camera is provided so that they can request a hospital in Kathmandu for consultations on medical problems.

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
### Prototyping on Breadboard
![breadboard](https://user-images.githubusercontent.com/29419943/70081939-85125080-1631-11ea-95ef-a6ad0648298c.png)
### Final PCB
![PCB](https://user-images.githubusercontent.com/29419943/70082025-abd08700-1631-11ea-8122-d6cd493da6da.png)
### Website to provide recommendations to the patient by the doctor.
![website](https://user-images.githubusercontent.com/29419943/70082090-c99dec00-1631-11ea-9141-00c5a67a0176.png)
### Demonstration of the project in a national technological festival.
![Demo](https://user-images.githubusercontent.com/29419943/70082162-e6d2ba80-1631-11ea-84c0-ea44df50467a.png)
### Output of ECG sensor on Arduino IDE.
![ArduinoOutput](https://user-images.githubusercontent.com/29419943/70082224-036ef280-1632-11ea-9f09-bb7861a3448c.png)
### ECG graph displayed on a webpage from  the data received from NodeMCU.
![WithoutFilter](https://user-images.githubusercontent.com/29419943/70082270-1c77a380-1632-11ea-99ef-14b2f1a47eb7.png)
### ECG graph after using exponential smoothing in the data.(Parameters of exponential smoothing were tuned manually.)
![AfterFilter](https://user-images.githubusercontent.com/29419943/70082315-3b763580-1632-11ea-9f1a-39781bf6bb9f.png)
### Further Work
- Later, we used a deep convolutional neural network to classify irregular heartbeats obtained from ECG sensor data.
- The model architecture was taken from a research paper[1] and trained on our dataset.
- It was able to classify five different classes of arrhythmias (irregular heartbeat).
![model](https://user-images.githubusercontent.com/29419943/70082598-dc64f080-1632-11ea-80c4-4ea1fb5063e1.png)
#### Confusion matrix
<img width="401" alt="ConfusionMatrix" src="https://user-images.githubusercontent.com/29419943/70082661-00283680-1633-11ea-833f-b633d7745192.png">

### Conclusion
- We were successful in building a system that can transfer ECG data coming from sensor over the internet for remote health care. Later, we also trained a convolutional neural network to classify five different classes of arrhythmia.

### References
1. [M. Kachuee, S. Fazeli and M. Sarrafzadeh "ECG Heartbeat Classification: A Deep Transferable Representation," University of California, Los Angeles, 2018.](https://arxiv.org/pdf/1805.00794.pdf)

