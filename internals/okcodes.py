def ok(okcode, add_msg=None):
    if okcode == 100:
        print(f"[EXTD] Recieved: Continuing (100) \n{add_msg}")
    elif okcode == 101:
        print(f"[EXTD] Switching Protocols (101) \n{add_msg}")
    elif okcode == 102:
        print(f"[EXTD] Processing (102) \n{add_msg}")
    elif okcode == 103:
        print(f"[EXTD] Early Hints (103) \n{add_msg}")
    elif okcode == 200:
        print(f"[EXTD] OK (200) \n{add_msg}")
    elif okcode == 201:
        print(f"[EXTD] Created (201) \n{add_msg}") 
    elif okcode == 202:
        print(f"[EXTD] Accepted (202) \n{add_msg}") 
    elif okcode == 203:
        print(f"[EXTD] Non-Authoriative Information (203) \n{add_msg}")
    elif okcode == 204:
        print(f"[EXTD] No Content (204) \n{add_msg}")
    elif okcode == 205:
        print(f"[EXTD] Reset Content (205) \n{add_msg}")
    elif okcode == 206:
        print(f"[EXTD] Partial Content (206) \n{add_msg}")
    elif okcode == 207:
        print(f"[EXTD] Multi-Status (207) \n{add_msg}")
    elif okcode == 208:
        print(f"[EXTD] Already Reported (208) \n{add_msg}")
    elif okcode == 226:
        print(f"[EXTD] IM Used (226) \n{add_msg}")
    elif okcode == 300:
        print(f"[EXTD] Multiple Choices (300) \n{add_msg}")
    elif okcode == 301:
        print(f"[EXTD] Moved Permanently (301) \n{add_msg}")
    elif okcode == 302:
        print(f"[EXTD] Found (Moved Temporarily) (302) \n{add_msg}")
    elif okcode == 303:
        print(f"[EXTD] See Other (303) \n{add_msg}")
    elif okcode == 304:
        print(f"[EXTD] Not Modified (304) \n{add_msg}")
    elif okcode == 305:
        print(f"[EXTD] Use Proxy [Deprecated] (305) \n{add_msg}")
    elif okcode == 306:
        print(f"[EXTD] unused/reserved (306) \n{add_msg}")
    elif okcode == 307:
        print(f"[EXTD] Temporary Redirect (307) \n{add_msg}")
    elif okcode == 308:
        print(f"[EXTD] Permanent Redirect (308) \n{add_msg}")
    else:
        print(f"[EXTD] Generic Code - See project GitHub for more details ({okcode}) \n{add_msg}")