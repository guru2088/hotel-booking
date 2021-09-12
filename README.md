# HOTEL RESERVATION

This sample code involves using a simple Flask API to serve

• A method for requesting for room assignment, which reply with the assigned room number upon success.

http://localhost:5000/main/api/checkin/1/1

• A method to check out of a room.

http://localhost:5000/main/api/checkout/1/1

• A method to mark a room cleaned (Available).

http://localhost:5000/main/api/cleaned/1/1

• A method to mark a room for repair.

http://localhost:5000/main/api/mark-repair/1/1
http://localhost:5000/main/api/completed-repair/1/1

• A method to list all the available rooms.

http://localhost:5000/main/api/available

## Required Dependencies

* [Python 3](https://www.python.org/downloads/)
* [pip](https://packaging.python.org/tutorials/installing-packages/) to install the python packages for the project


## Installation

The API can then be run by using:
```
pip install -r main/requirements.txt
```
or

```
pip3 install -r main/requirements.txt
```


## Start

The API can then be run by using:
```
python run.py
```
or

```
python3 run.py
```


## Testing

The API can tested by using:
```
pytest --cov=. tests.py
```
