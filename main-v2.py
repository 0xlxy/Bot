import threading
from time import time

import requests


def send_req():
    cookies = {
        "ASP.NET_SessionId": "z0f52og3lpjw1x0myaj1foyt",
        "__RequestVerificationToken": "6K6HZmRkNoSMhTaZwQEKGH9ymGZebPBIDoDHbobN3-1WW2EJJKaMZ5dymyKnBP6J2SgN4o0XZE1F1d8GyExd5Zhj-xzvxmndd8_JAkMea7E1",
    }
    headers = {
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:105.0) Gecko/20100101 Firefox/105.0",
        "Accept": "*/*",
        "Accept-Language": "en-US,en;q=0.5",
        "Referer": "https://www.toutoupiao.com/VoteItem/428720",
        "Origin": "https://www.toutoupiao.com",
        "Connection": "keep-alive",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "no-cors",
        "Sec-Fetch-Site": "same-origin",
        "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
        "X-Requested-With": "XMLHttpRequest",
        "Pragma": "no-cache",
        "Cache-Control": "no-cache",
    }
    data = {
        "voteID": "51164",
        "groupID": "0",
        "checkedVote": "428720",
        "cookieNameSendVote": "sendVote_51164",
        "cookieNameSendVoteTime": "sendVoteTime_51164",
        "__RequestVerificationToken": "Y9ETs2gwau9wxXmbzTwE3znqkTo0QCva_L6vMsLQ7AWPgEfjA0kjld-s3Xx45PayxSKd9iyH01tYwiIBeCTDclzfVRwx2kK09UiUoo9nvlw1",
    }
    response = requests.post(
        "https://www.toutoupiao.com/Ajax/SaveSendVote",
        cookies=cookies,
        headers=headers,
        data=data,
    )
    print(f"timestamp: {time()}\noutput: {response.text}\n")


while True:
    threads = []
    for i in range(100):
        thread = threading.Thread(target=send_req)
        thread.start()
        threads.append(thread)
    for thread in threads:
        thread.join()