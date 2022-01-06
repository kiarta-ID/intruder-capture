import requests
from bs4 import BeautifulSoup
import time
# import the opencv library
import cv2

url = 'http://127.0.0.1:8000/up'
r = requests.get(url) #url is create form 
soup = BeautifulSoup(r.text, 'html.parser')
links = soup.find_all('input')
token = links[0].get('value')
print(token)
# print(soup.find_all('input'))
# print()
jar = requests.cookies.RequestsCookieJar()
jar.set('XSRF-TOKEN', r.cookies['XSRF-TOKEN'])
jar.set('laravel_session', r.cookies['laravel_session'])

data = {
        "_token": token
    }

# files = {'img': open('test.png','rb')}
# upload = requests.post(url, files=files, data=data, cookies=jar, verify=False)
# print(upload.status_code)
# print(r.text)

# define a video capture object
vid = cv2.VideoCapture(0)
i = 1
previous = time.time()
delta = 0
framerate = 1
while(True):
    
    # Get the current time, increase delta and update the previous variable
    current = time.time()
    delta += current - previous
    previous = current
	# Capture the video frame
	# by frame
    ret, frame = vid.read()

    if delta > 2:
        delta = 0
        # Display the resulting frame
        # cv2.imshow('frame', frame)
        filename = f'cap_{i}.jpg'
        cv2.imwrite(filename, frame)
        img = open(f'cap_{i}.jpg', 'rb')
        files = {'img': img}
        upload = requests.post(url, files=files, data=data, cookies=jar, verify=False)

	# the 'q' button is set as the
	# quitting button you may use any
	# desired button of your choice
    # cv2.waitKey(1)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    
# After the loop release the cap object
vid.release()
# Destroy all the windows
cv2.destroyAllWindows()
