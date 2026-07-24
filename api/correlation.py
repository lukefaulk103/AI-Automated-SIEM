from datetime import datetime, timedelta


def check_bruteforce(events):
    """
    Detects possible brute force attacks.

    Looks for:
    - Multiple failed logins
    - Same user
    - Same IP
    - Within time window
    """


    failed_logins = []


    for event in events:

        if event.get("event_type") == "failed_login":

            failed_logins.append(event)



    if len(failed_logins) < 5:

        return {
            "incident": False
        }



    usernames = [
        event["details"].get("username")
        for event in failed_logins
    ]


    ips = [
        event["details"].get("ip")
        for event in failed_logins
    ]



    if len(set(usernames)) == 1 and len(set(ips)) == 1:

        return {

            "incident": True,

            "incident_type":
                "Brute Force Attack",


            "username":
                usernames[0],


            "source_ip":
                ips[0],


            "event_count":
                len(failed_logins),


            "severity":
                "critical",


            "recommendation":
                "Investigate possible credential compromise"

        }



    return {
        "incident": False
    }