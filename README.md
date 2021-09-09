# HOTEL RESERVATION

This sample code involves using a simple Flask API to serve

• A method for requesting for room assignment, which reply with the assigned room number upon success.
• A method to check out of a room.
• A method to mark a room cleaned (Available).
• A method to mark a room for repair.
• A method to list all the available rooms.

## Required Dependencies

* [Python 3](https://www.python.org/downloads/)
* [pip](https://packaging.python.org/tutorials/installing-packages/) to install the python packages for the project


## Installation

The API can then be run by using:
```
pip -r requirements.txt
```
or

```
pip3 -r requirements.txt
```


## Start

The API can then be run by using:
```
python app.py
```
or

```
python3 app.py
```


## Testing

The API can tested by using:
```
pytest --cov=. tests.py
```
