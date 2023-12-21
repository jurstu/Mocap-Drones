
import cv2 as cv
import numpy as np


class Cameras_raw:
    def __init__(self, paths):
        self.paths = paths
        self.caps = []
        for p in paths:
            c = cv.VideoCapture(p)
            self.caps.append(c)
            if not c.isOpened():
                print("error opening", p)
                exit()

    def read(self):
        out = []
        for c in self.caps:
            ret, frame = c.read()
            if(not ret):
                print("error reading cam")
                break
            out.append(frame )
        return out, 1


if __name__ == "__main__":

    
    a = Cameras(["/dev/video0"])
    while(1):
        f, _ = a.read()
        f[0] = cv.cvtColor(f[0], cv.COLOR_BGR2GRAY)
        cv.imshow("gray", f[0])
        if cv.waitKey(1) == ord('q'):
            break

