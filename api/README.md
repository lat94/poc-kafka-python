
<h3 align="center">poc-kafka-python</h3>


---


### **Installing dependencies**
run `pip install -r api/requirements.txt` to the install the dependencies.

### **Running the service**
run with `docker-compose up --build` to get it up and running.

### **Testing the flow**
to test the flow, just call the endpoint `[GET] /test/`, this should produce a message which should get consumed by kafka consumer.

### **Details**
details of the configuration of the service can be found with `.env` file, which as default, should not be versioned, but for the sake of the experiment, I decided to add this file to the repo.