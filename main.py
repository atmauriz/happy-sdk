from flask import Flask, render_template
from flask_ask import Ask, statement, question, session
import json
import requests
import time

from edo import Edo

app = Flask("Contest")
ask = Ask(app, "/")
edo = Edo(debug=True)


@ask.launch
def launch_skill():
    # todo verify if exists the device
    ping = True
    welcome_message = None
    if ping:
        welcome_message = render_template("positive_launch.txt")
    else:
        welcome_message = render_template("negative_launch.txt")
    return question(welcome_message)


@ask.intent("AskOperationsIntent")
def ask_operations():
    return question(render_template("ask_operations.txt"))


@ask.intent("SelectOperationIntent", convert={'arm_operation': str})
def select_operation(arm_operation):
    operation_description_message = None
    if arm_operation == "rodeo":
        operation_description_message = render_template("rodeo_description.txt")
    elif arm_operation == "calibrazione":
        operation_description_message = render_template("calibration_description.txt")
    elif arm_operation == "prendi telefono":
        operation_description_message = render_template("pick_phone_description.txt")
    else:
        print("Operazione non disponibile")
    return question(operation_description_message)


@ask.intent("MoveJointIntent", convert={'joint': str, 'degree': int})
def select_joint_degree(joint, degree):
    print(joint, degree)
    global edo
    edo.set_joint_state(joint, degree)
    return question("ok")


@ask.intent("AMAZON.YesIntent")
def yes_intent():
    return statement(render_template("yes.txt"))


@ask.intent("AMAZON.NoIntent")
def no_intent():
    return statement(render_template("no.txt"))


if __name__ == '__main__':
    app.run(debug=True)
