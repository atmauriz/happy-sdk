import logging
import requests


class Robot:
    NGROK_SERVER = "https://REPLACEWITHCURRENTAVAILABLENGROK.ngrok.io"
    JOINTS = {"j1": 0, "j2": 0, "j3": 0, "j4": 0, "j5": 0, "j6": 0, "j7": 0}

    def compose_payload(self, joint, degree):
        if joint == "1a":
            self.JOINTS["j1"] = degree
        elif joint == "seconda" or joint == "2a":
            self.JOINTS["j2"] = degree
        elif joint == "3a":
            self.JOINTS["j3"] = degree
        elif joint == "4a":
            self.JOINTS["j4"] = degree
        elif joint == "5a":
            self.JOINTS["j5"] = degree
        elif joint == "6a":
            self.JOINTS["j6"] = degree
        elif joint == "7a":
            self.JOINTS["j7"] = degree
        else:
            raise KeyError(f"{joint} is not available")

    def compose_url(self, endpoint: str):
        return f"{self.NGROK_SERVER}/{endpoint}"


class Edo(Robot):

    def __init__(self, debug: bool = False) -> None:
        self.debug = debug
        super().__init__()

    def set_joint_state(self, joint, degree):
        self.compose_payload(joint, degree)
        logging.info(list(self.JOINTS.values()))
        if self.debug:
            requests.post(url=self.compose_url(endpoint="/setJointState"), data=list(self.JOINTS.values()))

    def pick_phone(self):
        if self.debug:
            requests.post(url=self.compose_url(endpoint="/pickPhone"))

    def cancel(self):
        if self.debug:
            requests.post(url=self.compose_url(endpoint="/cancel"))

    def candle(self):
        if self.debug:
            requests.post(url=self.compose_url(endpoint="/candle"))
